#!/usr/bin/env python3
import argparse
import re
from pathlib import Path

IMAGE_LINE_RE = re.compile(r'^\s*!\[[^\]]*\]\([^)]+\)')

def process_text(text: str) -> str:
    lines = text.splitlines(keepends=True)
    output = []

    for line in lines:
        if IMAGE_LINE_RE.match(line):
            if output and output[-1].strip() != "":
                output.append("\n")
            output.append(line)
        else:
            output.append(line)

    return "".join(output)

def process_file(path: Path, in_place: bool = True):
    original = path.read_text(encoding="utf-8")
    modified = process_text(original)

    if in_place:
        path.write_text(modified, encoding="utf-8")
    else:
        print(f"\n--- {path} ---\n")
        print(modified)

def collect_all_md_files():
    return list(Path(".").rglob("*.md"))

def main():
    parser = argparse.ArgumentParser(
        description="Insert blank lines before Markdown image lines."
    )

    parser.add_argument(
        "files",
        nargs="*",
        help="Markdown files to process",
    )

    parser.add_argument(
        "--all",
        action="store_true",   # <-- FIXED HERE
        help="Process ALL .md files in current directory recursively.",
    )

    parser.add_argument(
        "--no-in-place",
        action="store_true",
        help="Print output instead of modifying files in place.",
    )

    args = parser.parse_args()

    files_to_process = []

    # Add user-provided files
    for f in args.files:
        p = Path(f)
        if p.is_file():
            files_to_process.append(p)
        else:
            print(f"Skipping {f}: not a file")

    # Add *all* markdown files if flag enabled
    if args.all:
        files_to_process.extend(collect_all_md_files())

    # Deduplicate
    files_to_process = list(dict.fromkeys(files_to_process))

    if not files_to_process:
        print("No files to process.")
        return

    for path in files_to_process:
        process_file(path, in_place=not args.no_in_place)

if __name__ == "__main__":
    main()
