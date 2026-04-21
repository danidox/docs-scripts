#!/usr/bin/env python3
r"""
Curate HTML tables in all Markdown/MDX files under the current root folder.

Scope:
- Operates ONLY inside <table>...</table> blocks.
  (Everything outside, including native Markdown code fences ```...```, is untouched.)

Behavior inside <table>:
- Remove any <style>...</style> blocks that appear inside <td> or <th>.
- Normalize whitespace around inline tags (<strong>, <em>, <code>) and inside <td>, <th>, <p>, <li>.
- Escape all left braces `{` in text nodes using the HTML entity (&#123;).
- Never modify tag names or attributes.
- Ensure each <table> starts at the beginning of its line (no leading spaces).

Usage:
  python tables.py           # update files in place
  python tables.py --dry     # preview changes only (no writes)
"""

import argparse
import re
import sys
from pathlib import Path

# --- 1) Match <table> blocks, capturing any leading indentation on the line ---
TABLE_RE = re.compile(r"(?mi)^([ \t]*)<table\b[\s\S]*?</table>")

# --- 2) Tags to normalize inside tables ---
CONTAINER_TAGS = ("td", "th", "p", "li")
INLINE_TAGS = ("strong", "em", "code")
INLINE_RE_FRAGMENT = "(?:" + "|".join(INLINE_TAGS) + ")"

# --- 3) Regex helpers ---
RE_NEWLINES = re.compile(r"\r?\n+")
RE_SPACES = re.compile(r"[ \t]{2,}")
RE_TRIM_OPEN = re.compile(rf"<({INLINE_RE_FRAGMENT})(\b[^>]*)>\s+", re.IGNORECASE)
RE_TRIM_CLOSE = re.compile(rf"\s+</({INLINE_RE_FRAGMENT})>", re.IGNORECASE)
RE_SPACE_BEFORE_OPEN = re.compile(rf"([^\s>])<({INLINE_RE_FRAGMENT})(\b[^>]*)>", re.IGNORECASE)
RE_SPACE_AFTER_CLOSE = re.compile(
    rf"</({INLINE_RE_FRAGMENT})>([^ \t\r\n<\.,;:!\?\)\]]|&[a-zA-Z0-9#]+;)",
    re.IGNORECASE,
)
RE_TAG_GAP = re.compile(r">\s+<")
RE_TABLE_OPEN = re.compile(r"<table\b([^>]*)>", re.IGNORECASE)
RE_DROP_TABLE_ATTRS = re.compile(
    r'\s+(?:style|class|id|summary)\s*=\s*(?:"[^"]*"|\'[^\']*\'|[^\s>]+)',
    re.IGNORECASE
)

# --- 4) List indentation helpers ---
RE_LIST_BLOCK = re.compile(r"(<(ul|ol)\b[^>]*>)([\s\S]*?)(</\2>)", re.IGNORECASE)
RE_LIST_ITEM = re.compile(r"<li\b[^>]*>[\s\S]*?</li>", re.IGNORECASE)

from bs4 import BeautifulSoup

def rewrite_table_block(table_html: str) -> str:
    # Parse the HTML fragment safely
    soup = BeautifulSoup(table_html, "html.parser")
    table = soup.find("table")
    if not table:
        return table_html

    # --- Clean unwanted table attributes ---
    for attr in ["style", "class", "id", "summary"]:
        if attr in table.attrs:
            del table.attrs[attr]

    # --- Clean <td> and <th> attributes ---
    for cell in table.find_all(["td", "th"]):
        # Drop unwanted attrs, keep rowspan/colspan
        cell.attrs = {k: v for k, v in cell.attrs.items() if k.lower() in ("rowspan", "colspan")}
        # Remove <style> tags inside cells
        for st in cell.find_all("style"):
            st.decompose()

        # Wrap "Note:" text in <p> if needed
        if cell.string and re.search(r"\bNote:\s*", cell.string, re.IGNORECASE):
            new_p = soup.new_tag("p")
            new_p.string = cell.string.strip()
            cell.clear()
            cell.append(new_p)

    # --- Escape { braces in text nodes ---
    for text_node in soup.find_all(string=True):
        if "{" in text_node:
            text_node.replace_with(text_node.replace("{", "&#123;"))

    # --- Re-indent lists cleanly ---
    for ol in soup.find_all(["ol", "ul"]):
        for li in ol.find_all("li"):
            li.string = li.get_text(strip=True)

    # BeautifulSoup pretty-print
    pretty_html = soup.prettify(formatter="html")

    # Ensure <table> starts flush-left
    return "\n".join(line.rstrip() for line in pretty_html.splitlines())


def indent_lists(html: str, indent: str = "  ") -> str:
    """Indent <ul>/<ol> blocks and their <li> items without breaking table cells."""
    def _block_repl(m: re.Match) -> str:
        open_tag, inner, close_tag = m.group(1).strip(), m.group(3).strip(), m.group(4).strip()

        # Indent each <li> by +2 spaces
        inner_lines = []
        for li_m in RE_LIST_ITEM.finditer(inner):
            li_html = li_m.group(0).strip()
            inner_lines.append(f"{indent}{indent}{li_html}")

        if not inner_lines:
            return m.group(0)  # leave unchanged if no <li>

        # Build the nicely formatted list
        formatted = "\n".join(inner_lines)
        return f"\n{indent}{open_tag}\n{formatted}\n{indent}{close_tag}\n"

    # Apply recursively to handle nested lists
    for _ in range(3):
        new_html = RE_LIST_BLOCK.sub(_block_repl, html)
        if new_html == html:
            break
        html = new_html

    # Remove redundant blank lines between tags
    html = re.sub(r"\n{3,}", "\n\n", html)
    return html


# --- 5) Inline whitespace normalization ---
def normalize_inline_html(inner: str) -> str:
    s = inner
    s = RE_NEWLINES.sub(" ", s)
    s = RE_SPACES.sub(" ", s)
    s = RE_TRIM_OPEN.sub(r"<\1\2>", s)
    s = RE_TRIM_CLOSE.sub(r"</\1>", s)
    s = RE_SPACE_BEFORE_OPEN.sub(r"\1 <\2\3>", s)
    s = RE_SPACE_AFTER_CLOSE.sub(r"</\1> \2", s)
    s = RE_SPACES.sub(" ", s)
    s = RE_TAG_GAP.sub("><", s)
    return s

# --- 6) Remove disallowed table attributes ---
def strip_disallowed_table_attrs(html: str) -> str:
    def _repl(m):
        attrs = m.group(1) or ""
        attrs = RE_DROP_TABLE_ATTRS.sub("", attrs)
        attrs = re.sub(r"\s+", " ", attrs).rstrip()
        return f"<table{attrs}>"
    return RE_TABLE_OPEN.sub(_repl, html)

def make_container_re(tag: str) -> re.Pattern:
    return re.compile(rf"<{tag}(\b[^>]*)>([\s\S]*?)</{tag}>", re.IGNORECASE)

# --- 7) Normalize container tags ---
def normalize_container_tag(html: str, tag: str):
    pattern = make_container_re(tag)
    changed = False

    def repl(m):
        nonlocal changed
        attrs, inner = m.group(1), m.group(2)

        if tag in ("td", "th"):
            inner = re.sub(r"<style\b[^>]*>[\s\S]*?</style>", "", inner, flags=re.IGNORECASE)
            if attrs:
                attrs = "".join(
                    re.findall(
                        r'\s+(?:rowspan|colspan)\s*=\s*(?:"[^"]*"|\'[^\']*\'|[^\s>]+)',
                        attrs,
                        flags=re.IGNORECASE
                    )
                )
            else:
                attrs = ""

        normalized = normalize_inline_html(inner)

        if tag == "td":
            already_wrapped = re.search(r"<p>\s*Note:", normalized, re.IGNORECASE)
            if not already_wrapped:
                mnote = re.search(r"\bNote:\s*", normalized, re.IGNORECASE)
                if mnote:
                    head = normalized[:mnote.start()].rstrip()
                    tail = normalized[mnote.start():].strip()
                    normalized = f"{head} <p>{tail} </p>"

        if normalized != inner:
            changed = True
        return f"<{tag}{attrs}>{normalized}</{tag}>"

    out = pattern.sub(repl, html)
    return out, changed

# --- 8) Escape left braces safely ---
def escape_left_braces_in_text_nodes(html: str) -> str:
    r"""
    Escape '{' as '&#123;' in text nodes (outside tags).
    """
    ALREADY = "__LBRACE_ESC__"
    html = html.replace("&#123;", ALREADY)

    parts = re.split(r"(<[^>]+>)", html)
    for i, chunk in enumerate(parts):
        if not chunk or chunk.startswith("<"):
            continue
        parts[i] = chunk.replace("{", "&#123;")

    return "".join(parts).replace(ALREADY, "&#123;")

# --- 9) Rewrite a single <table>...</table> block ---
def rewrite_table_block(table_html: str) -> str:
    html = strip_disallowed_table_attrs(table_html)

    # normalize inner containers
    for _ in range(3):
        round_changed = False
        for tag in CONTAINER_TAGS:
            html, ch = normalize_container_tag(html, tag)
            round_changed = round_changed or ch
        if not round_changed:
            break

    # format lists nicely
    html = indent_lists(html)

    # escape braces
    html = escape_left_braces_in_text_nodes(html)
    return html

# --- 10) File processing ---
def process_file(path: Path, dry: bool) -> bool:
    try:
        src = path.read_text(encoding="utf-8")
    except Exception as e:
        print(f"Cannot read {path}: {e}", file=sys.stderr)
        return False

    changed = False

    def replace_table(m):
        nonlocal changed
        indent = m.group(1)
        full_match = m.group(0)
        block = full_match[len(indent):]
        updated = rewrite_table_block(block)
        if updated != block:
            changed = True
            return updated
        return full_match

    out = TABLE_RE.sub(replace_table, src)

    if not changed:
        return False

    if dry:
        print(f"[DRY] Would update: {path}")
        return True

    path.write_text(out, encoding="utf-8")
    print(f"Updated: {path}")
    return True

# --- 11) CLI ---
def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--dry", action="store_true", help="Preview changes without writing")
    args = parser.parse_args()

    root = Path(".").resolve()
    files = list(root.rglob("*.md")) + list(root.rglob("*.mdx"))

    if not files:
        print("No .md or .mdx files found.")
        return 0

    touched = 0
    for f in files:
        if process_file(f, args.dry):
            touched += 1

    print(f"Done. {touched} file(s) {'would be' if args.dry else 'were'} updated.")
    return 0

if __name__ == "__main__":
    sys.exit(main())
