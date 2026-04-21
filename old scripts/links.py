import re
import argparse
from pathlib import Path
from datetime import datetime

# -------- Patterns --------

# Bare URLs to convert (not including quotes/brackets that suggest attributes)
URL_PATTERN = re.compile(
    r'(?<!\]\()(?<!\])(?<!\()\bhttps?://[^\s<>()"\'\]]+',
    re.IGNORECASE
)

# Fenced code blocks and inline code (kept verbatim)
# Fenced blocks (``` or ~~~) and inline code spans with any number of backticks
CODE_BLOCK_PATTERN = re.compile(
    r"(?s)"                                 # dot matches newlines
    r"(?:"
    r"```[\s\S]*?```"                       # fenced backticks
    r"|~~~[\s\S]*?~~~"                      # fenced tildes
    r"|(?<!`)(`+)(?!`)[\s\S]*?(?<!`)\1(?!`)"# inline: same-count backticks
    r")"
)


# HTML <code>...</code> and <pre>...</pre> blocks (kept verbatim)
HTML_CODELIKE_PATTERN = re.compile(r"(?is)(<code\b[\s\S]*?</code>|<pre\b[\s\S]*?</pre>)")

# Existing Markdown links/images (kept verbatim): [label](url) or ![alt](url)
MARKDOWN_LINK_PATTERN = re.compile(r"(!?\[[^\]]*\]\([^)\n]*\))")

# Any HTML tag with href/src attributes (the tag itself is kept verbatim)
HTML_TAG_PATTERN = re.compile(r"(?is)<[^>]+?\b(?:href|src)\s*=\s*['\"]https?://[^>]*?>")

# Trailing punctuation we don't want inside the link
TRAILING_PUNCTUATION = '.,!?);:'


# -------- Helpers --------

def _convert_bare_urls(text: str, counter) -> str:
    """
    Convert bare URLs in plain text (not inside code/HTML/markdown link).
    Preserves trailing punctuation outside the link.
    """
    def count_and_replace(m: re.Match) -> str:
        url = m.group(0)
        trailing = ''
        while url and url[-1] in TRAILING_PUNCTUATION:
            trailing = url[-1] + trailing
            url = url[:-1]
        counter['total'] += 1
        return f"[{url}]({url}){trailing}"

    # Avoid touching any HTML tags with href/src: split & preserve tags verbatim
    parts = []
    last = 0
    for tag in HTML_TAG_PATTERN.finditer(text):
        pre = text[last:tag.start()]
        pre = URL_PATTERN.sub(count_and_replace, pre)
        parts.append(pre)
        parts.append(tag.group(0))  # keep tag untouched
        last = tag.end()
    tail = text[last:]
    tail = URL_PATTERN.sub(count_and_replace, tail)
    parts.append(tail)
    return "".join(parts)


def _process_non_code_segment(segment: str, counter) -> str:
    """
    In a non-code segment, skip HTML <code>/<pre> blocks and existing Markdown links,
    converting only truly bare URLs elsewhere.
    """
    output = []
    last = 0
    # First, protect HTML code-like blocks (<code>, <pre>)
    for htmlcode in HTML_CODELIKE_PATTERN.finditer(segment):
        before_html = segment[last:htmlcode.start()]
        output.append(_process_outside_links(before_html, counter))
        output.append(htmlcode.group(0))  # keep verbatim
        last = htmlcode.end()
    remaining = segment[last:]
    output.append(_process_outside_links(remaining, counter))
    return "".join(output)


def _process_outside_links(text: str, counter) -> str:
    """
    In plain text (already outside code-like HTML), protect existing Markdown links/images
    and convert bare URLs elsewhere.
    """
    parts = []
    last = 0
    for mdlink in MARKDOWN_LINK_PATTERN.finditer(text):
        pre = text[last:mdlink.start()]
        parts.append(_convert_bare_urls(pre, counter))
        parts.append(mdlink.group(0))  # keep existing [label](url) or ![alt](url)
        last = mdlink.end()
    tail = text[last:]
    parts.append(_convert_bare_urls(tail, counter))
    return "".join(parts)


def convert_links_in_text(text: str) -> tuple[str, int]:
    """
    Convert bare URLs to Markdown links [url](url) outside code, HTML code/pre,
    HTML tags, and existing Markdown links/images.
    """
    out = []
    counter = {'total': 0}
    pos = 0

    for m in CODE_BLOCK_PATTERN.finditer(text):
        # Process non-code text before this code block
        out.append(_process_non_code_segment(text[pos:m.start()], counter))
        # Keep the code block or inline code unchanged
        out.append(m.group(0))
        pos = m.end()

    # Process the tail after the last code block
    out.append(_process_non_code_segment(text[pos:], counter))

    return "".join(out), counter['total']



# -------- File/dir processing & logging --------

def process_file(file_path: Path, dry_run: bool = False) -> int:
    with open(file_path, "r", encoding="utf-8") as f:
        content = f.read()

    updated, count = convert_links_in_text(content)

    if count > 0:
        if dry_run:
            print(f"🔎 (dry-run) Would update {file_path} — {count} link(s)")
        else:
            with open(file_path, "w", encoding="utf-8") as f:
                f.write(updated)
            print(f"✅ Updated {file_path} — {count} link(s)")
    else:
        print(f"➖ No changes: {file_path}")

    return count


def process_directory(directory: Path, dry_run: bool = False) -> tuple[int, list[tuple[Path, int]]]:
    total = 0
    changed: list[tuple[Path, int]] = []
    for file_path in sorted(directory.rglob("*.mdx")):
        cnt = process_file(file_path, dry_run=dry_run)
        total += cnt
        if cnt > 0:
            changed.append((file_path, cnt))
    return total, changed


def write_log(total: int, changed: list[tuple[Path, int]]):
    ts = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    log_path = Path.cwd() / "convert_links.log"
    lines = [
        f"# convert_links_safe log",
        f"timestamp: {ts}",
        f"total_links_converted: {total}",
        f"files_changed: {len(changed)}",
        "",
        "## details",
    ]
    for fp, cnt in changed:
        lines.append(f"{cnt}\t{fp}")
    log_path.write_text("\n".join(lines) + "\n", encoding="utf-8")
    print(f"📝 Log written to: {log_path}")


def main():
    parser = argparse.ArgumentParser(
        description="Convert bare hyperlinks in MDX to [url](url), skipping code, HTML code/pre, existing markdown links, and tag attributes."
    )
    parser.add_argument(
        "path",
        nargs="?",
        default=".",
        help="Path to an MDX file or directory (default: current directory)."
    )
    parser.add_argument(
        "--dry-run",
        action="store_true",
        help="Preview changes without modifying files or writing a log."
    )
    args = parser.parse_args()

    target = Path(args.path).resolve()
    if target.is_file() and target.suffix.lower() == ".mdx":
        total = process_file(target, dry_run=args.dry_run)
        changed = [(target, total)] if total > 0 else []
    elif target.is_dir():
        total, changed = process_directory(target, dry_run=args.dry_run)
    else:
        print("❌ Please provide a valid MDX file or directory.")
        return

    print("\n──────── Summary ────────")
    print(f"Files changed: {len(changed)}")
    print(f"Links converted: {total}")

    if not args.dry_run and total > 0:
        write_log(total, changed)
    elif args.dry_run:
        print("🛈 Dry run: no files modified, no log written.")


if __name__ == "__main__":
    main()
