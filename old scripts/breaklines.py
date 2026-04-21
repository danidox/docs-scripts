#!/usr/bin/env python3
import os
import re

def remove_soft_linebreaks(content: str) -> str:
    """
    Removes single line breaks within Markdown/MDX paragraphs,
    while keeping code blocks, lists, headings, JSX, and blank-line spacing intact.
    """
    lines = content.splitlines()
    output = []
    buffer = []
    in_code_block = False

    for line in lines:
        # Detect start or end of fenced code block
        if re.match(r"^```", line.strip()):
            in_code_block = not in_code_block
            if buffer:
                output.append(" ".join(buffer))
                buffer = []
            output.append(line)
            continue

        if in_code_block:
            output.append(line)
            continue

        # Blank line = paragraph break
        if line.strip() == "":
            if buffer:
                output.append(" ".join(buffer))
                buffer = []
            output.append("")  # keep the blank line
            continue

        # Preserve lists, headings, blockquotes, JSX, etc.
        if re.match(r"^(\s*[-*+]\s|\s*\d+\.\s|#|>|<)", line):
            if buffer:
                output.append(" ".join(buffer))
                buffer = []
            output.append(line)
            continue

        # Otherwise, accumulate lines to merge softly
        buffer.append(line.strip())

    # Flush any remaining buffered paragraph
    if buffer:
        output.append(" ".join(buffer))

    return "\n".join(output)


def process_file(filepath: str):
    with open(filepath, "r", encoding="utf-8") as f:
        original = f.read()

    cleaned = remove_soft_linebreaks(original)

    if cleaned != original:
        with open(filepath, "w", encoding="utf-8") as f:
            f.write(cleaned)
        print(f"✅ Cleaned: {filepath}")
    else:
        print(f"⚪ No changes: {filepath}")


def find_mdx_files(root_dir: str):
    """Recursively find all .mdx files."""
    mdx_files = []
    for dirpath, _, filenames in os.walk(root_dir):
        for filename in filenames:
            if filename.lower().endswith(".mdx"):
                mdx_files.append(os.path.join(dirpath, filename))
    return mdx_files


def main():
    root = os.getcwd()
    mdx_files = find_mdx_files(root)

    if not mdx_files:
        print("No .mdx files found in this directory or subdirectories.")
        return

    print(f"🔍 Found {len(mdx_files)} .mdx file(s). Processing...\n")
    for file_path in mdx_files:
        process_file(file_path)

    print("\n✅ Done. All .mdx files processed.")


if __name__ == "__main__":
    main()
