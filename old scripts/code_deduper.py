#!/usr/bin/env python3
"""
Improved dedupe script for .mdx files.

Find triple-backtick fences (allows optional leading whitespace and language tags),
detect repeated content inside a fence (by repeated lines or repeated characters),
and replace with a single copy of the repeated block.

Backs up modified files with a .bak suffix.

Usage:
    python scripts/fix_duplicate_codeblocks.py --dir <root>
"""
import os
import argparse
import re


def reduce_by_lines(s: str):
    lines = s.splitlines(True)
    n = len(lines)
    if n <= 1:
        return None
    # Try to find smallest repeating block of lines
    for k in range(1, n // 2 + 1):
        if n % k != 0:
            continue
        block = lines[:k]
        if block * (n // k) == lines:
            return ''.join(block)
    return None


def reduce_by_chars(s: str):
    n = len(s)
    if n <= 1:
        return None
    for p in range(1, n // 2 + 1):
        if n % p != 0:
            continue
        sub = s[:p]
        if sub * (n // p) == s:
            return sub
    return None


# Match any triple-backtick fence pair (inline or multiline).
# Group 1: opening fence including optional language / attributes
# Group 2: body (non-greedy)
# Group 3: closing fence
FENCE_RE = re.compile(r'(```[^\n]*\n?)(.*?)(```)', re.S)


def process_text(text: str):
    changed = False

    def repl(m: re.Match):
        nonlocal changed
        start = m.group(1)
        body = m.group(2)
        end = m.group(3)

        # keep original leading/trailing newlines within body
        stripped = body.strip('\r\n')
        if not stripped:
            return m.group(0)

        reduced = None
        rb = reduce_by_lines(stripped)
        if rb is not None and rb != stripped:
            reduced = rb
        else:
            rc = reduce_by_chars(stripped)
            if rc is not None and rc != stripped:
                reduced = rc

        if reduced is None:
            return m.group(0)

        # preserve one leading newline if original had one, and trailing newline
        lead = '\n' if body.startswith('\n') or body.startswith('\r\n') else ''
        trail = '\n' if body.endswith('\n') or body.endswith('\r\n') else ''
        new_body = lead + reduced + trail
        changed = True
        return start + new_body + end

    new_text = FENCE_RE.sub(repl, text)
    return new_text, changed


def process_file(path: str):
    with open(path, 'r', encoding='utf-8') as f:
        text = f.read()

    new_text, changed = process_text(text)
    if changed and new_text != text:
        bak = path + '.bak'
        with open(bak, 'w', encoding='utf-8') as f:
            f.write(text)
        with open(path, 'w', encoding='utf-8') as f:
            f.write(new_text)
        return True
    return False


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--dir', required=False,
                    default=r"C:\Users\daniela.craciun\OneDrive - UiPath\1docs-as-code\uipath-docs-content\integration-service",
                    help='Root directory to scan (defaults to the integration-service folder)')
    args = ap.parse_args()
    root = args.dir
    changed_files = []
    for dirpath, dirnames, filenames in os.walk(root):
        for fn in filenames:
            if fn.lower().endswith('.mdx'):
                path = os.path.join(dirpath, fn)
                try:
                    if process_file(path):
                        changed_files.append(path)
                except Exception as e:
                    print(f"ERROR processing {path}: {e}")
    if changed_files:
        print('Modified files:')
        for p in changed_files:
            print(' - ' + p)
    else:
        print('No changes made.')


if __name__ == '__main__':
    main()
