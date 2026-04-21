import os
import re
from typing import List, Tuple

ADMONITIONS = ("note", "warning", "danger", "tip", "info")

ADMONITION_LINE_RE = re.compile(
    rf"^(?P<indent>\s*)(?P<type>{'|'.join(ADMONITIONS)}):\s*(?P<text>.*)$",
    flags=re.IGNORECASE
)
FENCED_START_RE = re.compile(
    rf"^(?P<indent>\s*):::\s*(?P<type>{'|'.join(ADMONITIONS)})\s*$",
    flags=re.IGNORECASE
)
CODE_FENCE_RE = re.compile(r'^\s{0,3}(```|~~~)')
BLOCK_START_RE = re.compile(
    r"""^(
        \s{0,3}\#{1,6}\s+              |  # heading
        \s{0,3}(```|~~~)               |  # code fence
        \s{0,3}[-*_]\s*[-*_]\s*[-*_]\s*$ |  # hr
        \s{0,3}(\d+[\.)])\s+           |  # ordered list
        \s{0,3}[-+*]\s+                |  # unordered list
        \s{0,3}>\s+                    |  # blockquote
        \s{0,3}\|                      |  # table row
        \s*<[^>]+>                     |  # HTML block
        \s*:::\s*\w+                   |  # fenced admonition
        \s*(?:note|warning|danger|tip|info):\s+  # another admonition
    )""",
    flags=re.IGNORECASE | re.VERBOSE
)

def convert_lines(lines: List[str]) -> Tuple[List[str], int]:
    out: List[str] = []
    i = 0
    n = len(lines)
    converted = 0
    in_code_fence = False

    while i < n:
        line = lines[i]

        # Track code fences
        if CODE_FENCE_RE.match(line):
            in_code_fence = not in_code_fence
            out.append(line)
            i += 1
            continue

        # Skip already fenced admonitions
        if FENCED_START_RE.match(line):
            out.append(line)
            i += 1
            while i < n:
                out.append(lines[i])
                if lines[i].strip() == ":::":  # close
                    i += 1
                    break
                i += 1
            continue

        if in_code_fence:
            out.append(line)
            i += 1
            continue

        m = ADMONITION_LINE_RE.match(line)
        if not m:
            out.append(line)
            i += 1
            continue

        indent = m.group("indent")
        typ = m.group("type").lower()
        first_text = m.group("text")

        # Gather block content
        content = []
        if first_text:
            content.append(indent + first_text.rstrip())

        i += 1
        while i < n:
            peek = lines[i]
            if BLOCK_START_RE.match(peek):
                break
            if peek.strip() == "":
                content.append(peek.rstrip("\n"))
                i += 1
                continue
            content.append(peek.rstrip("\n"))
            i += 1

        # Write fenced block (preserve indentation)
        out.append(f"{indent}:::{typ}")
        for c in content:
            if c.strip() == "":
                out.append("")
            else:
                out.append(indent + c.lstrip())  # keep same indent as fence
        out.append(f"{indent}:::")

        converted += 1

    return [l + ("\n" if not l.endswith("\n") else "") for l in out], converted


def convert_file(path: str) -> int:
    with open(path, "r", encoding="utf-8") as f:
        lines = f.readlines()

    new_lines, count = convert_lines(lines)
    if count > 0:
        with open(path, "w", encoding="utf-8") as f:
            f.writelines(new_lines)
        print(f"✅ {path}: converted {count} block(s)")
    else:
        print(f"➡️  {path}: no changes")
    return count


def run_from_cwd() -> None:
    root = os.getcwd()
    print(f"🔍 Scanning recursively from: {root}\n")
    total_files = 0
    total_blocks = 0
    for dirpath, _, filenames in os.walk(root):
        for name in filenames:
            if name.lower().endswith(".md"):
                total_files += 1
                total_blocks += convert_file(os.path.join(dirpath, name))
    print("\n—— Summary ——")
    print(f"Files scanned: {total_files}")
    print(f"Blocks converted: {total_blocks}")
    print("🎉 Done!")

if __name__ == "__main__":
    run_from_cwd()

