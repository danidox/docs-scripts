#!/usr/bin/env python3
"""
replace_images_png_to_webp.py

Scans .mdx files and rewrites .png → .webp for any path matching:
/images/<product>/<file>.<ext>[?#optional]

- Works in Markdown image links and plain text.
- ALSO updates <img ... src="..."> and JSX-style src={"..."} or src={`...`}.
- Requires exactly one segment after /images/<product>/ (no deeper subdirs).
- Preserves ?query / #hash suffixes.
- Skips fenced code blocks (``` or ~~~) by default.

Usage:
  python replace_images_png_to_webp.py path/to/dir
  python replace_images_png_to_webp.py . --dry-run
  python replace_images_png_to_webp.py . --include-code
"""

import argparse
import pathlib
import re
import sys

FENCE_START_RE = re.compile(r"""^(\s*)(`{3,}|~{3,})""")

# Core path matcher: /images/<product>/<file>.<ext>[?#...]
PATH_CORE = r"""
/images/
(?P<product>[^/\s'")>\]}]+)
/
(?P<name>[^/\s'")>\]}?#]+?)
\.
(?P<ext>[A-Za-z0-9]+)
(?P<suffix>(?:[?#][^\s'")>\]}]*)?)"""

PATH_CORE_RE = re.compile(PATH_CORE, re.VERBOSE)

# Matches src attribute values in HTML/JSX: src="..."/'...'/{"..."}/{'...'}/ {`...`}
# We capture the full attr value (including quotes/braces) as 'wrapper' and the inner as 'inner'
SRC_ATTR_RE = re.compile(
    r"""
    \bsrc\s*=\s*
    (?P<wrapper>
        (?P<quote>["'])                # src="..."/'...'
        (?P<inner>[^"']*)
        (?P=quote)
      |
        \{\s*(?P<bq>["'`])            # src={"..."} / {'...'} / {`...`}
        (?P<inner_bq>[^"'`]*)
        (?P=bq)\s*\}
    )
    """,
    re.VERBOSE,
)

def _replace_path(path_text: str) -> str:
    """Within a string, rewrite .png to .webp for matching /images/<product>/<file> paths."""
    def _sub(m: re.Match) -> str:
        ext = m.group("ext")
        if ext.lower() == "png":
            return f"/images/{m.group('product')}/{m.group('name')}.webp{m.group('suffix') or ''}"
        return m.group(0)
    return PATH_CORE_RE.sub(_sub, path_text)

def _replace_in_src_attr(match: re.Match) -> str:
    wrapper = match.group("wrapper")
    if match.group("inner") is not None:
        inner = match.group("inner")
        replaced = _replace_path(inner)
        # Rebuild with the same quote type
        q = match.group("quote")
        return f'src={q}{replaced}{q}'
    else:
        inner = match.group("inner_bq")
        replaced = _replace_path(inner)
        bq = match.group("bq")
        return f'src={{{bq}{replaced}{bq}}}'

def replace_in_line(line: str) -> str:
    # First, handle src="..."/src={...} explicitly
    line2 = SRC_ATTR_RE.sub(_replace_in_src_attr, line)
    # Then, catch any remaining bare /images/<product>/<file>.png occurrences (e.g., Markdown ![]())
    line3 = _replace_path(line2)
    return line3

def process_text(text: str, include_code: bool) -> str:
    if include_code:
        return replace_in_line(text)

    lines = text.splitlines(keepends=True)
    out = []
    in_fence = False
    fence_marker = None
    for ln in lines:
        stripped = ln.strip()
        m = FENCE_START_RE.match(stripped)
        if m:
            token = m.group(2)
            if not in_fence:
                in_fence = True
                fence_marker = token
            elif token == fence_marker:
                in_fence = False
                fence_marker = None
            out.append(ln)
            continue
        out.append(ln if in_fence else replace_in_line(ln))
    return "".join(out)

def process_file(path: pathlib.Path, dry_run: bool, include_code: bool) -> bool:
    try:
        original = path.read_text(encoding="utf-8")
    except UnicodeDecodeError:
        print(f"[SKIP] Non-UTF8 file: {path}", file=sys.stderr)
        return False

    updated = process_text(original, include_code=include_code)
    if updated != original:
        if dry_run:
            print(f"[DRY] Would update: {path}")
        else:
            path.write_text(updated, encoding="utf-8")
            print(f"[OK ] Updated: {path}")
        return True
    return False

def main():
    ap = argparse.ArgumentParser(description="Replace .png with .webp for /images/<product>/<file> paths in MDX files, including <img src>.")
    ap.add_argument("root", type=pathlib.Path, help="Directory to scan")
    ap.add_argument("--dry-run", action="store_true", help="Show changes without writing files")
    ap.add_argument("--include-code", action="store_true", help="Also modify inside fenced code blocks")
    args = ap.parse_args()

    if not args.root.exists() or not args.root.is_dir():
        print(f"Error: {args.root} is not a directory", file=sys.stderr)
        sys.exit(1)

    changed = 0
    for mdx_path in args.root.rglob("*.mdx"):
        try:
            if process_file(mdx_path, args.dry_run, args.include_code):
                changed += 1
        except Exception as e:
            print(f"[ERR ] {mdx_path}: {e}", file=sys.stderr)

    print(f"Done. Files changed: {changed}")

if __name__ == "__main__":
    main()
