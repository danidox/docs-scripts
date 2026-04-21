#!/usr/bin/env python3
"""
Merge two folders while de-duplicating only when BOTH filename and content match.

Rules:
1) If same filename + same content hash -> keep one (deduplicate).
2) If same filename + different content hash:
   2a) If the ONLY difference is links where the path segment alternates between
       https://docs.uipath.com/<product>/automation-cloud/... and
       https://docs.uipath.com/<product>/automation-suite/...
       -> Prefer the Automation Cloud version:
          - Keep the cloud copy as the PLAIN filename (no suffix)
          - Discard/overwrite the suite copy
          - Log the discarded suite copy in a log file.
   2b) Otherwise -> keep BOTH with suffixes based on source root:
          - /automation-cloud/  -> -acloud
          - /automation-suite/  -> -asuite
       If a suffixed name already exists, fall back to -1, -2, ...

3) If filenames differ (regardless of content) -> keep both "as is" (no suffixing).

Additionally:
- If we first wrote a plain filename and later detect a conflict (2b), we retroactively
  rename the first variant to the appropriate suffix so both are present.
- The link-only difference detection is *exact-match after normalization* of the
  "automation-cloud/automation-suite" segment under the docs.uipath.com domain.

A discard log is written listing files skipped due to the link-only preference for cloud.
By default the log is placed in the output directory as "discarded_by_link_logic.log",
but you can override via --discard-log.
"""

import argparse
import hashlib
import re
import shutil
from pathlib import Path
from typing import Iterable, Tuple, Dict, Set, List, Optional

# ---------- Helpers: IO & hashing ----------

def iter_files(folder: Path, exts: Set[str], recursive: bool):
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

def read_text_safe(p: Path) -> str:
    try:
        return p.read_text(encoding="utf-8", errors="ignore")
    except Exception:
        return ""

def unique_dest_name(out_dir: Path, desired_name: str) -> Path:
    base = Path(desired_name).stem
    ext = Path(desired_name).suffix
    candidate = out_dir / (base + ext)
    i = 1
    while candidate.exists():
        candidate = out_dir / f"{base}-{i}{ext}"
        i += 1
    return candidate

def with_suffix(base_name: str, suffix: str) -> str:
    p = Path(base_name)
    stem, ext = p.stem, p.suffix
    return f"{stem}{suffix}{ext}"

def safe_copy(src: Path, dest: Path) -> Path:
    # Ensure we don't overwrite unintentionally; if dest exists, increment -1, -2, ...
    if dest.exists():
        dest = unique_dest_name(dest.parent, dest.name)
    shutil.copy2(src, dest)
    return dest

# ---------- Origin & link normalization ----------

def origin_tag_for(path: Path) -> str:
    """
    Identify origin based on presence of 'automation-cloud' or 'automation-suite' in the path parts.
    Returns '-acloud', '-asuite', or '' when not identifiable.
    """
    parts = set(path.parts)
    if "automation-cloud" in parts:
        return "-acloud"
    if "automation-suite" in parts:
        return "-asuite"
    return ""

# Regex to target ONLY the /automation-cloud/ or /automation-suite/ segment
# *within* docs.uipath.com URLs, preserving product name and the rest of the path.
_DOCS_UIPATH_LINK_SEGMENT = re.compile(
    r"(https?://docs\.uipath\.com/[^/\s)]+/automation-)(cloud|suite)(/)",
    flags=re.IGNORECASE
)

def normalize_docs_links(text: str) -> str:
    """
    Normalize docs.uipath.com URLs that differ only by 'automation-cloud' vs 'automation-suite'
    so that they compare equal for the purpose of link-only difference detection.
    """
    def _sub(m):
        prefix = m.group(1)  # up to 'automation-'
        # m.group(2) is cloud|suite
        tail = m.group(3)    # trailing '/'
        return f"{prefix}__ANY__{tail}"
    return _DOCS_UIPATH_LINK_SEGMENT.sub(_sub, text)

def prefer_cloud_if_only_link_diff(path_a: Path, path_b: Path, a_origin: str, b_origin: str) -> str:
    """
    Compare file contents ignoring 'automation-cloud' vs 'automation-suite' in docs.uipath.com URLs.
    Return:
      'cloud' if normalized contents match and the two files correspond to cloud vs suite.
      'none'  otherwise.
    """
    a_txt = read_text_safe(path_a)
    b_txt = read_text_safe(path_b)

    if normalize_docs_links(a_txt) != normalize_docs_links(b_txt):
        return "none"

    # Only meaningful if comparing cloud vs suite origins
    if a_origin == "-acloud" and b_origin == "-asuite":
        return "cloud"
    if a_origin == "-asuite" and b_origin == "-acloud":
        return "cloud"
    return "none"

# ---------- Core merge ----------

def copy_unique_files(
    sources: Iterable[Tuple[str, Path]],  # (label, path) where label is "A" or "B"
    out_dir: Path,
    discard_log_path: Optional[Path] = None
):
    """
    Returns: dict with counts and a list of discarded entries
    """
    seen_name_hash: Set[Tuple[str, str]] = set()

    # Track by output plain filename: info about variants we wrote for that base name
    # Structure:
    # by_name[name] = {
    #   "variants": {
    #       file_hash: {"path": <out_path>, "suffix": "", "origin_suffix": "-acloud"|" -asuite"|""}
    #   },
    #   "have_conflict": bool
    # }
    by_name: Dict[str, Dict] = {}

    counts = {
        "written": 0,
        "from_A": 0,
        "from_B": 0,
        "duplicates_skipped": 0,
        "suite_discarded_by_link_logic": 0
    }
    discarded_log: List[str] = []

    out_dir.mkdir(parents=True, exist_ok=True)

    for label, path in sources:
        file_hash = sha256_of_file(path)
        base_name = path.name
        key = (base_name, file_hash)

        if key in seen_name_hash:
            counts["duplicates_skipped"] += 1
            continue

        o_tag = origin_tag_for(path)

        if base_name not in by_name:
            # First time we see this filename — write as plain (unless something already exists with different hash)
            dest_plain = out_dir / base_name
            if dest_plain.exists():
                # If exists with different hash, use suffix immediately
                if sha256_of_file(dest_plain) != file_hash:
                    desired = with_suffix(base_name, o_tag) if o_tag else base_name
                    dest = safe_copy(path, out_dir / desired)
                    by_name[base_name] = {
                        "variants": {file_hash: {"path": dest, "suffix": o_tag or "", "origin_suffix": o_tag}},
                        "have_conflict": True
                    }
                else:
                    # Same hash as existing plain file -> dedupe
                    counts["duplicates_skipped"] += 1
                    seen_name_hash.add(key)
                    continue
            else:
                dest = safe_copy(path, dest_plain)
                by_name[base_name] = {
                    "variants": {file_hash: {"path": dest, "suffix": "", "origin_suffix": o_tag}},
                    "have_conflict": False
                }

            counts["written"] += 1
            counts["from_A"] += (1 if label == "A" else 0)
            counts["from_B"] += (1 if label == "B" else 0)
            seen_name_hash.add(key)
            continue

        # There is at least one variant already for this filename.
        info = by_name[base_name]

        # If exact same hash already captured for this name -> dedupe
        if file_hash in info["variants"]:
            counts["duplicates_skipped"] += 1
            continue

        # Conflict: same filename, different content hash.
        # 1) First try the link-only difference preference for cloud.
        # Check against each existing variant — if any match the normalization criteria, apply the policy.
        resolved_by_cloud_pref = False

        for existing_hash, existing_variant in list(info["variants"].items()):
            existing_path = existing_variant["path"]
            existing_origin = existing_variant.get("origin_suffix", existing_variant.get("suffix",""))

            cloud_choice = prefer_cloud_if_only_link_diff(existing_path, path, existing_origin, o_tag)
            if cloud_choice == "cloud":
                dest_plain = out_dir / base_name
                current_is_cloud = (o_tag == "-acloud")
                existing_is_cloud = (existing_origin == "-acloud")

                if current_is_cloud and not existing_is_cloud:
                    # Overwrite suite/plain (or suite-suffixed) with cloud as plain name.
                    # If existing variant is suffixed, remove it; if it's plain, overwrite it.
                    # Write cloud content to plain filename:
                    shutil.copy2(path, dest_plain)

                    # Remove the existing suite variant file on disk if it's not the same plain path
                    if existing_path != dest_plain and existing_path.exists():
                        try:
                            existing_path.unlink()
                        except Exception:
                            pass

                    # Reset bookkeeping to a single cloud variant
                    new_hash = sha256_of_file(dest_plain)
                    info["variants"] = {
                        new_hash: {"path": dest_plain, "suffix": "", "origin_suffix": "-acloud"}
                    }
                    info["have_conflict"] = False

                    # Update counters and logs
                    counts["written"] += 1
                    counts["from_A"] += (1 if label == "A" else 0)
                    counts["from_B"] += (1 if label == "B" else 0)
                    counts["suite_discarded_by_link_logic"] += 1
                    discarded_log.append(f"{base_name}: discarded suite variant {existing_path} in favor of cloud {path} (link-only difference)")

                    # Track seen
                    seen_name_hash.add((base_name, new_hash))
                    resolved_by_cloud_pref = True
                    break

                elif existing_is_cloud and not current_is_cloud:
                    # Cloud is already the winner; skip this suite file
                    counts["duplicates_skipped"] += 1
                    counts["suite_discarded_by_link_logic"] += 1
                    discarded_log.append(f"{base_name}: skipped suite variant {path} because cloud variant {existing_path} already kept (link-only difference)")
                    resolved_by_cloud_pref = True
                    break
                # If both are cloud or both suite (unexpected for this branch), ignore and continue checking.
        if resolved_by_cloud_pref:
            continue

        # 2) Fallback: real content conflict -> suffixing behavior.
        info["have_conflict"] = True

        # If any previously-written variant lacks suffix, rename it now using stored origin_suffix if possible.
        for h, v in list(info["variants"].items()):
            if v.get("suffix", "") == "":
                existing_origin_suffix = v.get("origin_suffix", "")
                if existing_origin_suffix:
                    target_name = with_suffix(base_name, existing_origin_suffix)
                    new_dest = out_dir / target_name
                    if new_dest.exists():
                        new_dest = unique_dest_name(out_dir, target_name)
                    try:
                        v["path"].rename(new_dest)
                    except Exception:
                        # If rename fails (e.g., across FS), copy then remove old file
                        shutil.copy2(v["path"], new_dest)
                        try:
                            v["path"].unlink()
                        except Exception:
                            pass
                    info["variants"][h]["path"] = new_dest
                    info["variants"][h]["suffix"] = existing_origin_suffix

        # Now write the current conflicting file using its origin-based suffix (if any)
        desired_name = with_suffix(base_name, o_tag) if o_tag else base_name
        dest = safe_copy(path, out_dir / desired_name)
        info["variants"][file_hash] = {"path": dest, "suffix": o_tag or "", "origin_suffix": o_tag}

        counts["written"] += 1
        counts["from_A"] += (1 if label == "A" else 0)
        counts["from_B"] += (1 if label == "B" else 0)
        seen_name_hash.add(key)

    # Write discard log if requested or default path is provided
    if discard_log_path is not None:
        try:
            discard_log_path.parent.mkdir(parents=True, exist_ok=True)
            with discard_log_path.open("w", encoding="utf-8") as f:
                if discarded_log:
                    f.write("# Files discarded based on link-only cloud preference\n")
                    for line in discarded_log:
                        f.write(line + "\n")
                else:
                    f.write("# No files were discarded by the link-only logic.\n")
        except Exception:
            pass

    return counts, discarded_log

# ---------- CLI ----------

def main():
    ap = argparse.ArgumentParser(
        description="Merge two folders with smart de-duplication and link-based cloud preference."
    )
    ap.add_argument("dir_a", type=Path, help="Path to automation-cloud folder")
    ap.add_argument("dir_b", type=Path, help="Path to automation-suite folder")
    ap.add_argument("out_dir", type=Path, help="Output folder for merged files")
    ap.add_argument("--exts", type=str, default="", help="Comma-separated list of file extensions to include (e.g. .mdx,.md). Leave empty for all files.")
    ap.add_argument("--recursive", action="store_true", help="Recurse into subdirectories")
    ap.add_argument("--discard-log", type=Path, default=None, help="Optional path for the discard log file")

    args = ap.parse_args()

    if not args.dir_a.is_dir() or not args.dir_b.is_dir():
        raise SystemExit("Both input arguments must be valid directories.")

    args.out_dir.mkdir(parents=True, exist_ok=True)

    exts = set(e.strip().lower() for e in args.exts.split(",") if e.strip())
    sources: List[Tuple[str, Path]] = []

    def gather(label: str, root: Path):
        files = list(iter_files(root, exts, recursive=args.recursive))
        files.sort(key=lambda p: str(p.relative_to(root)).lower())
        for p in files:
            sources.append((label, p))

    gather("A", args.dir_a)
    gather("B", args.dir_b)

    discard_log_path = args.discard_log or (args.out_dir / "discarded_by_link_logic.log")

    counts, discarded = copy_unique_files(sources, args.out_dir, discard_log_path=discard_log_path)

    print("Done.")
    print(f"Written: {counts['written']} (from A: {counts['from_A']}, from B: {counts['from_B']})")
    print(f"Duplicates skipped: {counts['duplicates_skipped']}")
    print(f"Suite discarded by link-only preference: {counts['suite_discarded_by_link_logic']}")
    print(f"Discard log: {discard_log_path}")


if __name__ == "__main__":
    main()
