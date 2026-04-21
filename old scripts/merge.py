#!/usr/bin/env python3
"""
Merge two folders while de-duplicating only when BOTH filename and content match.

Usage:
    python merge_by_name_and_hash.py /path/to/folderA /path/to/folderB /path/to/output
"""

import argparse
import hashlib
import shutil
from pathlib import Path
from typing import Iterable, Tuple, Dict, Set

def iter_files(folder: Path, exts: Set[str], recursive: bool) -> Iterable[Path]:
    if recursive:
        yield from (p for p in folder.rglob("*") if p.is_file() and (not exts or p.suffix.lower() in exts))
    else:
        yield from (p for p in folder.iterdir() if p.is_file() and (not exts or p.suffix.lower() in exts))

def sha256_of_file(path: Path, chunk_size: int = 1024 * 1024) -> str:
    h = hashlib.sha256()
    with path.open("rb") as f:
        for chunk in iter(lambda: f.read(chunk_size), b""):
            h.update(chunk)
    return h.hexdigest()

def unique_dest_name(out_dir: Path, desired_name: str) -> Path:
    base = Path(desired_name).stem
    ext = Path(desired_name).suffix
    candidate = out_dir / (base + ext)
    i = 1
    while candidate.exists():
        candidate = out_dir / f"{base}-{i}{ext}"
        i += 1
    return candidate

def copy_unique_files(
    sources: Iterable[Tuple[str, Path]],
    out_dir: Path
) -> Tuple[int, int, int, int]:
    """
    sources: iterable of (label, Path) where label is "A" or "B"
    Returns: (count_from_A, count_from_B, duplicates_skipped, total_written)
    """
    # Track seen (filename, hash) pairs; that's our duplicate key now.
    seen_name_hash: Set[Tuple[str, str]] = set()
    # Track which basenames are already used in the output to avoid overwrites.
    used_names: Set[str] = set()

    written = 0
    from_a = 0
    from_b = 0
    duplicates = 0

    for label, path in sources:
        file_hash = sha256_of_file(path)
        key = (path.name, file_hash)

        if key in seen_name_hash:
            # Exact duplicate by BOTH filename and content
            duplicates += 1
            continue

        # Decide destination filename:
        # - If the same name has already been written BUT with a different hash,
        #   this is NOT a duplicate, so we suffix to avoid overwrite.
        dest = out_dir / path.name
        if dest.exists() and sha256_of_file(dest) != file_hash:
            dest = unique_dest_name(out_dir, path.name)

        shutil.copy2(path, dest)
        seen_name_hash.add(key)
        used_names.add(dest.name)

        written += 1
        if label == "A":
            from_a += 1
        else:
            from_b += 1

    return from_a, from_b, duplicates, written

def main():
    parser = argparse.ArgumentParser(description="Merge two folders; de-dupe only when filename AND content match.")
    parser.add_argument("folder_a", type=Path, help="Path to Folder A")
    parser.add_argument("folder_b", type=Path, help="Path to Folder B")
    parser.add_argument("output_folder", type=Path, help="Where to write the merged files")
    parser.add_argument("--ext", action="append", default=[".mdx"],
                        help="Include only files with these extensions (repeatable). Default: .mdx")
    parser.add_argument("--recursive", action="store_true", help="Recurse into subdirectories")
    parser.add_argument("--prefer", choices=["A", "B"], default="A",
                        help="Order preference when encountering exact duplicates (same name + hash). Default: A")
    args = parser.parse_args()

    folder_a: Path = args.folder_a.resolve()
    folder_b: Path = args.folder_b.resolve()
    out_dir: Path = args.output_folder.resolve()
    exts = {e.lower() for e in args.ext} if args.ext else set()

    if not folder_a.is_dir():
        raise SystemExit(f"Folder A not found or not a directory: {folder_a}")
    if not folder_b.is_dir():
        raise SystemExit(f"Folder B not found or not a directory: {folder_b}")

    out_dir.mkdir(parents=True, exist_ok=True)

    files_a = list(iter_files(folder_a, exts, recursive=args.recursive))
    files_b = list(iter_files(folder_b, exts, recursive=args.recursive))

    ordered = (
        [("A", p) for p in files_a] + [("B", p) for p in files_b]
        if args.prefer == "A"
        else [("B", p) for p in files_b] + [("A", p) for p in files_a]
    )

    from_a, from_b, duplicates, written = copy_unique_files(ordered, out_dir)

    total_input = len(files_a) + len(files_b)
    print("=== Merge Summary ===")
    print(f"Folder A files considered: {len(files_a)}")
    print(f"Folder B files considered: {len(files_b)}")
    print(f"Exact duplicates skipped (same filename AND hash): {duplicates}")
    print(f"Total input files: {total_input}")
    print(f"Total written to output: {written}")
    print(f"Output folder: {out_dir}")

if __name__ == "__main__":
    main()
