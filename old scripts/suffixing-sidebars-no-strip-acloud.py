#!/usr/bin/env python3
"""
Fully interactive suffix-aware reference updater with logging (press Enter to finish)

This script:
1. Asks for the content directory (where *-acloud.* and *-asuite.* files are located)
2. Scans for variant Markdown files (e.g., overview-acloud.md, _overview-asuite.md)
3. Asks repeatedly for target files (like sidebar JSONs) to update
4. Automatically determines the variant (Cloud or Suite) based on the filename, or asks if uncertain
5. Replaces unsuffixed references (overview.md / overview.mdx) with the correct variant:
   - Cloud: uses the exact filename (e.g., overview-acloud.md)
   - Suite: uses the filename WITHOUT a leading underscore in references
     (e.g., _overview-asuite.md on disk → overview-asuite.md in the sidebar)
6. Logs each action and reports:
   - Distinct bases (pages) changed
   - Total number of references actually updated

Press **Enter** on an empty line when done entering target files.
Use `--apply` to write changes (default is dry run).
"""

from __future__ import annotations
import argparse
import difflib
import re
import shutil
from dataclasses import dataclass
from pathlib import Path
from typing import Dict, List, Tuple
from datetime import datetime

ACLOUD = "acloud"
ASUITE = "asuite"
VALID_VARIANTS = {ACLOUD, ASUITE}

SUFFIXES = {
    ACLOUD: f"-{ACLOUD}",
    ASUITE: f"-{ASUITE}",
}

# We support both .mdx and .md files on disk
MD_EXTS = [".mdx", ".md"]
# Pattern for matching references in text (either .mdx or .md)
REF_EXT_PATTERN = r"\.(?:mdx|md)"

LOG_FILE = "suffix_update_log.txt"


@dataclass
class Mapping:
    base: str
    variants: Dict[str, str]  # variant ("acloud"/"asuite") -> filename as it exists on disk


def find_mdx_variants(content_dir: Path) -> Dict[str, Mapping]:
    """
    Scan the content directory for *-acloud.* and *-asuite.* files
    (both .mdx and .md) and build a base -> {variant: filename} mapping.

    IMPORTANT:
    - For files like "_overview-asuite.md" and "overview-acloud.md", we normalize
      the base to "overview" so they are treated as variants of the same base.
    """
    variants: Dict[str, Mapping] = {}

    for path in content_dir.rglob("*"):
        if not path.is_file():
            continue

        if path.suffix.lower() not in MD_EXTS:
            continue

        name = path.name
        lower = name.lower()

        for variant, suf in SUFFIXES.items():
            # e.g. name: "_overview-asuite.md", suf: "-asuite"
            if not lower.endswith(suf + path.suffix.lower()):
                continue

            # Strip extension, keep original case
            stem = name[: -len(path.suffix)]

            # Check that stem ends with variant suffix (case-insensitive)
            if not stem.lower().endswith(suf):
                continue

            # Remove suffix from stem to get raw base (still may have leading "_" or trailing "-")
            base_len = len(stem) - len(suf)
            base = stem[:base_len]

            # Normalize base:
            # - strip leading "_" so "_overview" and "overview" map together
            # - strip trailing "-" just in case (e.g. "overview-" -> "overview")
            base = base.lstrip("_").rstrip("-")

            key = base
            variants.setdefault(key, Mapping(base=key, variants={}))
            # Store the filename exactly as it exists on disk
            variants[key].variants[variant] = name
            break

    return variants


def detect_variant_from_filename(target: Path) -> str | None:
    """
    Try to infer variant (acloud/asuite) from the target file path/name.
    """
    lower = target.name.lower()
    if "automation-cloud" in lower:
        return ACLOUD
    if "automation-suite" in lower:
        return ASUITE

    plower = str(target.parent).lower()
    if "automation-cloud" in plower or "cloud" in plower:
        return ACLOUD
    if "automation-suite" in plower or "suite" in plower:
        return ASUITE

    return None


def plan_replacements(
    text: str,
    variant: str,
    mapping: Dict[str, Mapping],
) -> Tuple[str, List[Tuple[str, str]], int]:
    """
    For a given variant (acloud/asuite), replace occurrences of
    base.(md|mdx) with the appropriate variant filename.

    Returns:
      updated_text,
      pairs: list of (base, replacement_name) for bases that had at least one replacement,
      total_references_replaced: total number of individual replacements performed.

    - Matches ANYWHERE in the text, including paths like:
      /studio-web/automation-suite/latest/everyone-user-guide/overview.md

    - Special behavior:
      For ASUITE:
        If the variant filename on disk starts with "_", the replacement
        text will NOT include the leading underscore.
        Example: "_overview-asuite.md" (on disk) -> "overview-asuite.md" (in href)
      For ACLOUD:
        Filenames are used as-is.

    - Does NOT touch already suffixed links such as:
      overview-acloud.md, overview-asuite.md
    """
    replaced_pairs: List[Tuple[str, str]] = []
    updated = text
    total_references_replaced = 0

    for base, mp in mapping.items():
        if variant not in mp.variants:
            continue

        target_name_on_disk = mp.variants[variant]

        # Strip a leading "_" in the reference text for all variants, not on disk.
        # For acloud, also strip the -acloud suffix so the reference is just the base filename.
        # "_overview-acloud.md" -> "overview.md"
        # "_overview-asuite.md" -> "overview-asuite.md"
        replacement_name = target_name_on_disk.lstrip("_")
        if variant == ACLOUD:
            ext = Path(replacement_name).suffix
            stem = Path(replacement_name).stem  # e.g. "overview-acloud"
            stem = re.sub(rf"-{ACLOUD}$", "", stem, flags=re.IGNORECASE)
            replacement_name = stem + ext

        # Pattern:
        #   \b<base>(-acloud|-asuite)?\.(mdx|md)\b
        # We only replace when the optional suffix group is empty,
        # i.e., plain "overview.md" but NOT "overview-asuite.md" / "overview-acloud.md".
        pattern = re.compile(
            rf"(?<![0-9A-Za-z_-])"        # char before base is NOT a filename char
            rf"{re.escape(base)}"
            rf"(?P<suffix>-a(?:cloud|suite))?"  # optional -acloud / -asuite, still ignored if present
            rf"{REF_EXT_PATTERN}"
            rf"(?![0-9A-Za-z_-])",        # char after extension is NOT a filename char
            re.IGNORECASE,
        )

        count_for_base = 0

        def _repl(m: re.Match) -> str:
            nonlocal count_for_base, total_references_replaced
            # If already has -acloud or -asuite, leave it alone
            if m.group("suffix"):
                return m.group(0)
            count_for_base += 1
            total_references_replaced += 1
            return replacement_name

        new_updated = pattern.sub(_repl, updated)

        if count_for_base > 0:
            replaced_pairs.append((base, replacement_name))
            updated = new_updated

    return updated, replaced_pairs, total_references_replaced


def _strip_wrapping_quotes(s: str) -> str:
    s = s.strip()
    if (s.startswith('"') and s.endswith('"')) or (s.startswith("'") and s.endswith("'")):
        return s[1:-1].strip()
    return s


def _normalize_path_text(s: str) -> Path:
    import os

    s = _strip_wrapping_quotes(s)
    s = os.path.expandvars(s)
    p = Path(s).expanduser()
    try:
        return p.resolve(strict=False)
    except Exception:
        return p


def process_target_file(
    target: Path,
    variant: str,
    mapping: Dict[str, Mapping],
    apply: bool,
    log_handle,
) -> Tuple[List[str], int, int]:
    """
    Process a single target file.

    Returns:
      actions: list of log/print lines
      bases_changed: how many distinct bases had at least one replacement
      references_changed: how many individual references were actually updated
    """
    actions: List[str] = []

    if not target.exists():
        return [f"SKIP: {target} (not found)"], 0, 0

    original = target.read_text(encoding="utf-8")
    updated, pairs, references_changed = plan_replacements(original, variant, mapping)

    bases_changed = len(pairs)

    if bases_changed == 0:
        actions.append(f"NO CHANGES: {target} (no matching unsuffixed refs found)")
        return actions, 0, 0

    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    log_handle.write(f"[{timestamp}] Processed: {target}\n")

    if apply:
        backup = target.with_suffix(target.suffix + ".bak")
        shutil.copy2(target, backup)
        target.write_text(updated, encoding="utf-8")
        actions.append(
            f"UPDATED: {target} (backup at {backup.name}) — "
            f"{bases_changed} bases, {references_changed} references"
        )
        for frm, to in pairs:
            actions.append(f"  - {frm}.* -> {to}")
            log_handle.write(f"  Replaced {frm}.* -> {to}\n")
    else:
        actions.append(
            f"DRY RUN for {target}: {bases_changed} bases, "
            f"{references_changed} references would be updated"
        )
        for frm, to in pairs:
            actions.append(f"  - would replace {frm}.* -> {to}")
            log_handle.write(f"  Would replace {frm}.* -> {to}\n")

        diff = difflib.unified_diff(
            original.splitlines(keepends=True),
            updated.splitlines(keepends=True),
            fromfile=str(target),
            tofile=f"{target} (proposed)",
        )
        actions.append("  --- diff start ---")
        actions.extend(["  " + line.rstrip("\n") for line in diff])
        actions.append("  --- diff end ---")

    log_handle.write(
        f"  Distinct bases changed: {bases_changed}, "
        f"total references updated: {references_changed}\n\n"
    )
    log_handle.flush()
    return actions, bases_changed, references_changed


def main():
    p = argparse.ArgumentParser(
        description="Fully interactive suffix-aware Markdown reference updater with logging."
    )
    p.add_argument(
        "--apply",
        action="store_true",
        help="Write changes in place (default is dry run)",
    )
    args = p.parse_args()

    # Ask for content directory interactively
    while True:
        content_input = input("Enter content directory path: ").strip()
        if not content_input:
            print("You must enter a content directory.")
            continue
        content_dir = _normalize_path_text(content_input)
        if not content_dir.exists() or not content_dir.is_dir():
            print(f"Directory '{content_dir}' not found or not a directory.")
            continue
        break

    mapping = find_mdx_variants(content_dir)
    if not mapping:
        print(f"No suffixed Markdown files found under {content_dir}. Nothing to do.")
        return

    print("Discovered variant mapping:")
    for base, mp in sorted(mapping.items()):
        variants_desc = ", ".join(f"{k}:{v}" for k, v in sorted(mp.variants.items()))
        print(f"  - {base} -> {variants_desc}")

    total_bases_changed = 0
    total_references_changed = 0

    with open(LOG_FILE, "a", encoding="utf-8") as log_handle:
        log_handle.write(
            f"===== Run started at {datetime.now().strftime('%Y-%m-%d %H:%M:%S')} =====\n"
        )
        print("\nEnter target files one by one (press Enter with no input to finish):")

        while True:
            user_input = input("Target file path: ").strip()
            if user_input == "":
                print(
                    f"All done.\n"
                    f"  Distinct bases (pages) touched across all files: {total_bases_changed}\n"
                    f"  Total references updated across all files: {total_references_changed}"
                )
                log_handle.write(
                    f"Distinct bases changed across all files: {total_bases_changed}\n"
                )
                log_handle.write(
                    f"Total references updated across all files: {total_references_changed}\n"
                )
                log_handle.write("===== Run ended =====\n\n")
                break

            target = _normalize_path_text(user_input)
            if not target.exists():
                print(
                    f"SKIP: {target} (not found). Tip: you can paste paths WITH quotes—I'll strip them."
                )
                continue

            chosen = detect_variant_from_filename(target)
            if not chosen:
                chosen = input(
                    "Could not infer variant. Enter variant (acloud/asuite): "
                ).strip().lower()
                if chosen not in VALID_VARIANTS:
                    print("Invalid variant. Skipping.")
                    continue

            print(f"\nProcessing {target} with variant '{chosen}'...")
            actions, bases_changed, refs_changed = process_target_file(
                target, chosen, mapping, apply=args.apply, log_handle=log_handle
            )
            total_bases_changed += bases_changed
            total_references_changed += refs_changed
            for line in actions:
                print(line)


if __name__ == "__main__":
    main()
