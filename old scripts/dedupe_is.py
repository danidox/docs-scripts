#!/usr/bin/env python3
# dedupe_asuite_acloud.py

import argparse
import hashlib
import logging
import sys
from pathlib import Path
from collections import defaultdict

SUFFIXES = ("-asuite", "-acloud")

def sha256sum(path: Path, chunk_size: int = 1024 * 1024) -> str:
    h = hashlib.sha256()
    with path.open("rb") as f:
        for chunk in iter(lambda: f.read(chunk_size), b""):
            h.update(chunk)
    return h.hexdigest()

def iter_files(root: Path):
    for p in root.rglob("*"):
        if p.is_file():
            yield p

def base_stem(stem: str):
    for s in SUFFIXES:
        if stem.endswith(s):
            return stem[: -len(s)], s
    return stem, ""

def pretty_name(p: Path) -> str:
    return p.name  # only filename, no path

def plan_actions_for_dir(hash_val: str, files: list[Path], apply: bool, logger: logging.Logger):
    by_dir: dict[Path, list[Path]] = defaultdict(list)
    for p in files:
        by_dir[p.parent].append(p)

    for parent, paths in by_dir.items():
        candidates = defaultdict(lambda: {"base": None, "suffixed": []})

        for p in paths:
            b, suf = base_stem(p.stem)
            entry = candidates[(b, p.suffix)]
            if suf:
                entry["suffixed"].append((p, suf))
            else:
                if entry["base"] is None:
                    entry["base"] = p
                else:
                    logger.warning(f"✋ Multiple base files in {parent}: {pretty_name(entry['base'])} & {pretty_name(p)}")
                    entry["base"] = None

        for (b, ext), entry in candidates.items():
            base_name = f"{b}{ext}"
            base_path = parent / base_name
            suffixed = entry["suffixed"]
            has_base = entry["base"] is not None

            if not suffixed and not has_base:
                continue

            if has_base:
                for p, suf in suffixed:
                    logger.info(f"🗑️ DELETE duplicate: {pretty_name(p)} (identical to {base_name})")
                    if apply:
                        try:
                            p.unlink()
                        except Exception as e:
                            logger.error(f"❌ Failed to delete {pretty_name(p)}: {e}")
                continue

            if suffixed:
                def rank(s): return {"-asuite": 0, "-acloud": 1}.get(s, 2)
                suffixed.sort(key=lambda t: (rank(t[1]), t[0].name))
                keep_path, keep_suffix = suffixed[0]
                others = [p for p, _ in suffixed[1:]]

                if base_path.exists() and base_path not in paths:
                    logger.warning(f"✋ SKIP rename: {pretty_name(keep_path)} -> {base_name} (base exists)")
                    for p in others:
                        logger.info(f"🗑️ DELETE duplicate: {pretty_name(p)}")
                        if apply:
                            try:
                                p.unlink()
                            except Exception as e:
                                logger.error(f"❌ Failed to delete {pretty_name(p)}: {e}")
                    continue

                if keep_path.name != base_name:
                    logger.info(f"✅ RENAME: {pretty_name(keep_path)} → {base_name}")
                    if apply:
                        try:
                            keep_path.rename(base_path)
                            keep_path = base_path
                        except Exception as e:
                            logger.error(f"❌ Failed to rename {pretty_name(keep_path)}: {e}")
                            continue

                for p in others:
                    logger.info(f"🗑️ DELETE duplicate: {pretty_name(p)}")
                    if apply:
                        try:
                            p.unlink()
                        except Exception as e:
                            logger.error(f"❌ Failed to delete {pretty_name(p)}: {e}")

def main():
    parser = argparse.ArgumentParser(description="Find identical files and clean up -asuite / -acloud duplicates.")
    parser.add_argument("root", nargs="?", default=".", help="Root directory (default: .)")
    parser.add_argument("--apply", action="store_true", help="Actually perform rename/delete (default: dry run)")
    parser.add_argument("--log-file", default="dedupe_asuite_acloud.log", help="Log file (default: dedupe_asuite_acloud.log)")
    args = parser.parse_args()

    logger = logging.getLogger("dedupe")
    logger.setLevel(logging.INFO)
    fmt = logging.Formatter("%(message)s")  # Clean minimal log format
    fh = logging.FileHandler(args.log_file, encoding="utf-8")
    fh.setFormatter(fmt)
    logger.addHandler(fh)
    sh = logging.StreamHandler(sys.stdout)
    sh.setFormatter(fmt)
    logger.addHandler(sh)

    root = Path(args.root).resolve()
    if not root.exists() or not root.is_dir():
        print(f"Invalid root directory: {root}", file=sys.stderr)
        sys.exit(1)

    logger.info(f"🔍 Scanning {root} (dry run={not args.apply})")

    hash_map = defaultdict(list)
    count = 0
    for p in iter_files(root):
        try:
            h = sha256sum(p)
            hash_map[h].append(p)
            count += 1
        except Exception as e:
            logger.error(f"❌ Error hashing {pretty_name(p)}: {e}")

    logger.info(f"📦 {count} files scanned, checking duplicates...")

    dups = 0
    for h, paths in hash_map.items():
        if len(paths) > 1:
            dups += 1
            plan_actions_for_dir(h, paths, args.apply, logger)

    logger.info(f"✅ Done! Duplicate sets: {dups}. Log saved to {args.log_file}.")

if __name__ == "__main__":
    main()
