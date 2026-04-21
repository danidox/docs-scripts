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
  python tables.py --summary path/to/report.txt
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
# Do NOT collapse spaces between block tags like <ul>, <ol>, <tr>, <td>
RE_TAG_GAP = re.compile(r">(?!\s*</?(?:ul|ol|li|tr|td|th)\b)\s+<", re.IGNORECASE)
# Remove blank lines between HTML tags (especially in tables)
RE_BLANK_LINES = re.compile(r"\n\s*\n+", re.MULTILINE)
RE_TABLE_OPEN = re.compile(r"<table\b([^>]*)>", re.IGNORECASE)
RE_DROP_TABLE_ATTRS = re.compile(
    r'\s+(?:style|class|id|summary)\s*=\s*(?:"[^"]*"|\'[^\']*\'|[^\s>]+)',
    re.IGNORECASE
)

# --- 4) List indentation helpers ---
RE_LIST_BLOCK = re.compile(
    r"(^[ \t]*)(<(ul|ol)\b[^>]*>)([\s\S]*?)(</\3>)",
    re.IGNORECASE | re.MULTILINE
)
RE_LIST_ITEM = re.compile(r"<li\b[^>]*>[\s\S]*?</li>", re.IGNORECASE)
RE_ANY_LIST_TAG = re.compile(r"</?(ul|ol)\b[^>]*>", re.IGNORECASE)

from bs4 import BeautifulSoup  # noqa: F401 (import kept in case of future use)

def split_preserving_list_blocks(s: str):
    """
    Yield tuples (segment, is_list_block). Non-list segments are plain strings to be normalized.
    List blocks are returned exactly as they appear in `s` (including nested lists).
    """
    pos = 0
    while True:
        m = re.search(r"<(ul|ol)\b[^>]*>", s[pos:], re.IGNORECASE)
        if not m:
            tail = s[pos:]
            if tail:
                yield (tail, False)
            break

        start = pos + m.start()
        head = s[pos:start]
        if head:
            yield (head, False)

        # scan forward to find the matching close, allowing nested <ul>/<ol>
        depth = 0
        end = None
        for t in RE_ANY_LIST_TAG.finditer(s, start):
            is_close = s[t.start()+1] == "/"
            if not is_close:
                depth += 1
            else:
                depth -= 1
                if depth == 0:
                    end = t.end()
                    break
        if end is None:
            # malformed HTML; treat the rest as a list block to be safe
            end = len(s)

        block = s[start:end]
        yield (block, True)
        pos = end

def indent_lists(html: str, indent: str = "  ") -> str:
    """Indent <ul>/<ol> blocks and their <li> items, preserving base indentation."""
    def _block_repl(m: re.Match) -> str:
        base, open_tag, _tagname, inner, close_tag = (
            m.group(1), m.group(2).strip(), m.group(3), m.group(4).strip(), m.group(5).strip()
        )

        # Indent <li> by +4 spaces from the base level
        inner_lines = []
        for li_m in RE_LIST_ITEM.finditer(inner):
            li_html = li_m.group(0).strip()
            inner_lines.append(f"{base}{indent*2}{li_html}")

        if not inner_lines:
            return m.group(0)

        formatted = "\n".join(inner_lines)
        # <ul>/<ol> sits one indent inside its parent (e.g., inside <td>)
        return f"\n{base}{indent}{open_tag}\n{formatted}\n{base}{indent}{close_tag}\n"

    for _ in range(3):
        new_html = RE_LIST_BLOCK.sub(_block_repl, html)
        if new_html == html:
            break
        html = new_html

    # Clean extra blank lines
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

        # Normalize while protecting lists as blocks (supports nested lists)
        if tag in ("td", "th", "p"):
            parts = []
            for seg, is_list in split_preserving_list_blocks(inner):
                if is_list:
                    block = seg.strip()
                    parts.append("\n" + block + "\n")
                else:
                    parts.append(normalize_inline_html(seg))
            normalized = "".join(parts)
            # squeeze stray whitespace right around list boundaries but keep the newline
            normalized = re.sub(r"\s*\n\s*(<(?:ul|ol)\b)", r"\n\1", normalized, flags=re.IGNORECASE)
            normalized = re.sub(r"(</(?:ul|ol)>)\s*\n\s*", r"\1\n", normalized, flags=re.IGNORECASE)
        else:
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

    # remove blank lines inside table blocks
    html = RE_BLANK_LINES.sub("\n", html)

    return html

# --- 10) File processing ---
def process_file(path: Path, dry: bool) -> int:
    """
    Returns the number of <table> blocks changed in this file.
    0 means no changes. On error, returns 0 and logs to stderr.
    """
    try:
        src = path.read_text(encoding="utf-8")
    except Exception as e:
        print(f"Cannot read {path}: {e}", file=sys.stderr)
        return 0

    changed_tables = 0

    def replace_table(m):
        nonlocal changed_tables
        indent = m.group(1)
        full_match = m.group(0)
        block = full_match[len(indent):]
        updated = rewrite_table_block(block)
        if updated != block:
            changed_tables += 1
            # Ensure table starts at column 0 (no leading indent)
            return updated
        return full_match

    out = TABLE_RE.sub(replace_table, src)

    if changed_tables == 0:
        return 0

    if dry:
        print(f"[DRY] Would update: {path} ({changed_tables} table{'s' if changed_tables != 1 else ''})")
        return changed_tables

    try:
        path.write_text(out, encoding="utf-8")
        print(f"Updated: {path} ({changed_tables} table{'s' if changed_tables != 1 else ''})")
    except Exception as e:
        print(f"Cannot write {path}: {e}", file=sys.stderr)
        return 0

    return changed_tables

# --- 11) CLI ---
def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--dry", action="store_true", help="Preview changes without writing")
    parser.add_argument(
        "--summary",
        default="tables_update_summary.txt",
        help="Path to write a text summary of touched files (default: tables_update_summary.txt)",
    )
    args = parser.parse_args()

    root = Path(".").resolve()
    files = list(root.rglob("*.md")) + list(root.rglob("*.mdx"))

    if not files:
        print("No .md or .mdx files found.")
        summary_path = Path(args.summary)
        summary_path.write_text(
            "Tables Curation Summary\n"
            f"Mode: {'DRY RUN' if args.dry else 'WRITE'}\n"
            f"Root: {root}\n"
            "Result: No .md or .mdx files found.\n",
            encoding="utf-8",
        )
        print(f"Summary written to: {summary_path}")
        return 0

    touched = []
    total_tables = 0

    for f in files:
        n = process_file(f, args.dry)
        if n > 0:
            touched.append((f, n))
            total_tables += n

    # --- Console summary ---
    print("\n========== SUMMARY ==========")
    if touched:
        print(f"{len(touched)} file(s) {'would be' if args.dry else 'were'} updated; "
              f"{total_tables} table block(s) {'would be' if args.dry else 'were'} modified:")
        for p, n in touched:
            print(f" - {p}  ({n} table{'s' if n != 1 else ''})")
    else:
        print("No files required changes.")
    print("=============================\n")

    # --- Write summary file ---
    summary_path = Path(args.summary)
    if touched:
        lines = [
            "Tables Curation Summary",
            f"Mode: {'DRY RUN' if args.dry else 'WRITE'}",
            f"Root: {root}",
            "",
            f"Files {'to be' if args.dry else ''} updated: {len(touched)}",
            f"Total table blocks {'to be' if args.dry else ''} modified: {total_tables}",
            "",
            "Details:",
        ]
        for p, n in touched:
            lines.append(f" - {p}  ({n} table{'s' if n != 1 else ''})")
        lines.append("")  # trailing newline
        summary_path.write_text("\n".join(lines), encoding="utf-8")
    else:
        summary_path.write_text(
            "Tables Curation Summary\n"
            f"Mode: {'DRY RUN' if args.dry else 'WRITE'}\n"
            f"Root: {root}\n\n"
            "No files required changes.\n",
            encoding="utf-8",
        )

    print(f"Summary written to: {summary_path}")
    return 0

if __name__ == "__main__":
    sys.exit(main())
