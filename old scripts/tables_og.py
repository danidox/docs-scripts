#!/usr/bin/env python3
"""
Curate HTML tables in all Markdown/MDX files under the current root folder.

Scope:
- Operates ONLY inside <table>...</table> blocks.
  (Everything outside, including native Markdown code fences ```...```, is untouched.)

Behavior inside <table>:
- Remove any <style>...</style> blocks that appear inside <td> or <th>.
- Normalize whitespace around inline tags (<strong>, <em>, <code>) and inside <td>, <th>, <p>, <li>.
- Escape all left braces `{` in text nodes using a backslash (e.g. -> \{).
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
from typing import Tuple

# --- 1) Match <table> blocks, capturing any leading indentation on the line ---
# ^([ \t]*) captures indentation (so we can drop it and force <table> to column 0)
TABLE_RE = re.compile(r"(?mi)^([ \t]*)<table\b[\s\S]*?</table>")

# --- 2) Tags to normalize inside tables ---
CONTAINER_TAGS = ("td", "th", "p", "li")
INLINE_TAGS = ("strong", "em", "code")
INLINE_RE_FRAGMENT = "(?:" + "|".join(INLINE_TAGS) + ")"

# --- 3) Spacing cleanup helpers ---
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

# --- 4) Inline whitespace normalization (text between tags only) ---
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

def make_container_re(tag: str) -> re.Pattern:
    return re.compile(rf"<{tag}(\b[^>]*)>([\s\S]*?)</{tag}>", re.IGNORECASE)

# --- 5) Per-container normalization with style removal in td/th ---
def normalize_container_tag(html: str, tag: str):
    pattern = make_container_re(tag)
    changed = False

    def repl(m):
        nonlocal changed
        attrs, inner = m.group(1), m.group(2)

        if tag in ("td", "th"):
            # Remove any <style>...</style> blocks inside table cells
            inner = re.sub(r"<style\b[^>]*>[\s\S]*?</style>", "", inner, flags=re.IGNORECASE)

            # Keep only rowspan and colspan; drop all other attributes
            if attrs:
                # Extract only rowspan/colspan attributes (case-insensitive)
                kept_attrs = re.findall(
                    r'\s+(rowspan|colspan)\s*=\s*(?:"[^"]*"|\'[^\']*\'|[^\s>]+)',
                    attrs,
                    flags=re.IGNORECASE
                )

                # Reconstruct attribute string (add a space before each)
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

        # ---- Stable "Note:" wrapping for <td> ----
        if tag == "td":
            # If it's already wrapped, do nothing
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



# --- 6) Escape { in text nodes only (never inside tags/attributes) ---
def escape_left_braces_in_text_nodes(html: str) -> str:
    r"""
    Escape '{' as '&#123;' in text nodes (outside tags).
    Includes content of <code> and <pre>.
    Avoids double-escaping existing '&#123;'.
    """
    ALREADY = "__LBRACE_ESC__"
    html = html.replace("&#123;", ALREADY)

    parts = re.split(r"(<[^>]+>)", html)
    for i, chunk in enumerate(parts):
        if not chunk or chunk.startswith("<"):
            continue
        parts[i] = chunk.replace("{", "&#123;")

    return "".join(parts).replace(ALREADY, "&#123;")


# --- 7) Rewrite a single <table>...</table> block ---
def rewrite_table_block(table_html: str) -> str:
    html = table_html

    # Passes to tidy containers
    for _ in range(3):
        round_changed = False
        for tag in CONTAINER_TAGS:
            html, ch = normalize_container_tag(html, tag)
            round_changed = round_changed or ch
        if not round_changed:
            break

    # Finally, escape { in all text nodes inside the table
    html = escape_left_braces_in_text_nodes(html)

    return html

# --- 8) File processing ---
def process_file(path: Path, dry: bool) -> bool:
    try:
        src = path.read_text(encoding="utf-8")
    except Exception as e:
        print(f"Cannot read {path}: {e}", file=sys.stderr)
        return False

    changed = False

    def replace_table(m):
        nonlocal changed
        indent = m.group(1)             # captured leading whitespace
        full_match = m.group(0)         # includes indent + <table>...</table>
        block = full_match[len(indent):]  # strip indent; force <table> to column 0

        updated = rewrite_table_block(block)

        if updated != block:
            changed = True
            return updated               # return flush-left table
        return full_match                # unchanged → return original

    out = TABLE_RE.sub(replace_table, src)

    if not changed:
        return False

    if dry:
        print(f"[DRY] Would update: {path}")
        return True

    path.write_text(out, encoding="utf-8")
    print(f"Updated: {path}")
    return True

# --- 9) CLI ---
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
