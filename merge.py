#!/usr/bin/env python3
"""
Interactive merge script.

It will ask you to provide:
1) the path to the automation-cloud only content
2) the path to the automation-suite only content
3) the name of the output folder (it will be created under the common root BEFORE 'automation-cloud'/'automation-suite')

Behavior:
- If same filename + same content -> deduplicate (keep one) and LOG the skipped duplicate.
- If same filename + different content:
  - If the ONLY difference is docs.uipath.com links where the path segment alternates between
    https://docs.uipath.com/<product>/automation-cloud/... and
    https://docs.uipath.com/<product>/automation-suite/... ,
    then prefer the Automation Cloud copy as the plain filename (no suffix) and discard/overwrite the suite copy.
    Log the suite discard.
  - Otherwise, keep both with suffixes based on source root:
      /automation-cloud/  -> -acloud
      /automation-suite/  -> -asuite
- If filenames differ, keep both “as is”.
- If a plain file had been written first and later a conflict is found, it gets renamed to add the origin suffix.

A log file is written in the output folder:
  - 'merge_log.log' : includes both "suite discarded by link-only logic" entries and "exact duplicate skipped" entries.
"""

import hashlib
import os
import re
import shutil
from pathlib import Path
from typing import Iterable, Tuple, Dict, Set, List, Optional

# ---------- Basic helpers ----------

def iter_files(folder: Path, recursive: bool = True):
    if recursive:
        yield from (p for p in folder.rglob("*") if p.is_file())
    else:
        yield from (p for p in folder.iterdir() if p.is_file())

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
    new_name = f"{stem}{suffix}{ext}"

    # If the suffix is -asuite, prefix with underscore
    if suffix == "-asuite":
        new_name = "_" + new_name

    return new_name

def safe_copy(src: Path, dest: Path) -> Path:
    if dest.exists():
        dest = unique_dest_name(dest.parent, dest.name)
    shutil.copy2(src, dest)
    return dest

# ---------- Origins & link normalization ----------

_DOCS_UIPATH_LINK_SEGMENT = re.compile(
    r"(https?://docs\.uipath\.com/[^/\s)]+/automation-)(cloud|suite)(/)",
    flags=re.IGNORECASE
)

def normalize_docs_links(text: str) -> str:
    def _sub(m):
        return f"{m.group(1)}__ANY__{m.group(3)}"
    return _DOCS_UIPATH_LINK_SEGMENT.sub(_sub, text)

def prefer_cloud_if_only_link_diff(path_a: Path, path_b: Path, a_origin: str, b_origin: str) -> str:
    a_txt = read_text_safe(path_a)
    b_txt = read_text_safe(path_b)
    if normalize_docs_links(a_txt) != normalize_docs_links(b_txt):
        return "none"
    # Meaningful only if they represent cloud vs suite
    if a_origin == "-acloud" and b_origin == "-asuite":
        return "cloud"
    if a_origin == "-asuite" and b_origin == "-acloud":
        return "cloud"
    return "none"

# ---------- Merge core ----------

def copy_unique_files(
    sources: Iterable[Tuple[str, Path]],  # (label, path) where label is "A" or "B"
    out_dir: Path,
    log_path: Path
):
    seen_name_hash: Set[Tuple[str, str]] = set()
    by_name: Dict[str, Dict] = {}
    log_lines: List[str] = []

    counts = {
        "written": 0,
        "from_A": 0,
        "from_B": 0,
        "duplicates_skipped": 0,
        "suite_discarded_by_link_only": 0
    }

    out_dir.mkdir(parents=True, exist_ok=True)

    for label, path in sources:
        file_hash = sha256_of_file(path)
        base_name = path.name
        key = (base_name, file_hash)
        o_tag = "-acloud" if label == "A" else "-asuite"

        if key in seen_name_hash:
            counts["duplicates_skipped"] += 1
            # Log duplicate skip with reference to an existing kept variant if available
            if base_name in by_name and file_hash in by_name[base_name]["variants"]:
                kept_path = by_name[base_name]["variants"][file_hash]["path"]
                log_lines.append(f"{base_name}: exact duplicate skipped -> {path} (same as kept {kept_path})")
            else:
                log_lines.append(f"{base_name}: exact duplicate skipped -> {path}")
            continue

        if base_name not in by_name:
            dest_plain = out_dir / base_name
            if dest_plain.exists():
                if sha256_of_file(dest_plain) != file_hash:
                    desired = with_suffix(base_name, o_tag) if o_tag else base_name
                    dest = safe_copy(path, out_dir / desired)
                    by_name[base_name] = {
                        "variants": {file_hash: {"path": dest, "suffix": o_tag or "", "origin_suffix": o_tag}},
                        "have_conflict": True
                    }
                else:
                    counts["duplicates_skipped"] += 1
                    log_lines.append(f"{base_name}: exact duplicate skipped -> {path} (same content as existing {dest_plain})")
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

        # Same filename encountered before; check for hash match
        info = by_name[base_name]
        if file_hash in info["variants"]:
            counts["duplicates_skipped"] += 1
            kept_path = info["variants"][file_hash]["path"]
            log_lines.append(f"{base_name}: exact duplicate skipped -> {path} (same as kept {kept_path})")
            continue

        # Conflict: same name, different hash
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
                    # Overwrite or replace with cloud as plain
                    shutil.copy2(path, dest_plain)

                    # If existing variant is separate file, remove it
                    if existing_path != dest_plain and existing_path.exists():
                        try:
                            existing_path.unlink()
                        except Exception:
                            pass

                    new_hash = sha256_of_file(dest_plain)
                    info["variants"] = {
                        new_hash: {"path": dest_plain, "suffix": "", "origin_suffix": "-acloud"}
                    }
                    info["have_conflict"] = False

                    counts["written"] += 1
                    counts["from_A"] += (1 if label == "A" else 0)
                    counts["from_B"] += (1 if label == "B" else 0)
                    counts["suite_discarded_by_link_only"] += 1
                    log_lines.append(f"{base_name}: suite discarded by link-only logic -> discarded {existing_path}, kept cloud {path}")
                    seen_name_hash.add((base_name, new_hash))
                    resolved_by_cloud_pref = True
                    break

                elif existing_is_cloud and not current_is_cloud:
                    counts["duplicates_skipped"] += 1
                    counts["suite_discarded_by_link_only"] += 1
                    log_lines.append(f"{base_name}: suite discarded by link-only logic -> skipped {path}, cloud already kept as {existing_path}")
                    resolved_by_cloud_pref = True
                    break

        if resolved_by_cloud_pref:
            continue

        # Fallback: real content conflict -> suffix both
        info["have_conflict"] = True

        # Rename any plain existing variant to its origin suffix if known
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
                        shutil.copy2(v["path"], new_dest)
                        try:
                            v["path"].unlink()
                        except Exception:
                            pass
                    info["variants"][h]["path"] = new_dest
                    info["variants"][h]["suffix"] = existing_origin_suffix

        desired_name = with_suffix(base_name, o_tag) if o_tag else base_name
        dest = safe_copy(path, out_dir / desired_name)
        info["variants"][file_hash] = {"path": dest, "suffix": o_tag or "", "origin_suffix": o_tag}

        counts["written"] += 1
        counts["from_A"] += (1 if label == "A" else 0)
        counts["from_B"] += (1 if label == "B" else 0)
        seen_name_hash.add(key)

    # Write log
    try:
        with log_path.open("w", encoding="utf-8") as f:
            if log_lines:
                f.write("# Merge log\n")
                for line in log_lines:
                    f.write(line + "\n")
            else:
                f.write("# No duplicates or link-only discards.\n")
    except Exception:
        pass

    return counts, log_lines

# ---------- Root computation & interactive CLI ----------

def find_root_before_segment(path: Path, marker: str) -> Optional[Path]:
    parts = list(path.parts)
    lowered = [p.lower() for p in parts]
    try:
        idx = lowered.index(marker)
        return Path(*parts[:idx]) if idx > 0 else Path(parts[0])
    except ValueError:
        return None

def compute_output_root(cloud_path: Path, suite_path: Path) -> Path:
    cloud_root = find_root_before_segment(cloud_path, "automation-cloud")
    suite_root = find_root_before_segment(suite_path, "automation-suite")
    if cloud_root and suite_root and cloud_root == suite_root:
        return cloud_root
    try:
        common = Path(os.path.commonpath([str(cloud_path), str(suite_path)]))
        return common
    except Exception:
        return cloud_path.parent

def main():
    print("=== Merge Automation Cloud/Suite ===")
    cloud_str = input("1) Enter the path to the automation-cloud ONLY content: ").strip().strip('"')
    suite_str = input("2) Enter the path to the automation-suite ONLY content: ").strip().strip('"')
    out_name = input("3) Enter the NAME of the output folder (will be created under the common root): ").strip()

    cloud_path = Path(cloud_str)
    suite_path = Path(suite_str)

    if not cloud_path.is_dir():
        raise SystemExit(f"Not a directory: {cloud_path}")
    if not suite_path.is_dir():
        raise SystemExit(f"Not a directory: {suite_path}")

    root = compute_output_root(cloud_path, suite_path)
    out_dir = root / out_name
    out_dir.mkdir(parents=True, exist_ok=True)

    print(f"\nComputed root: {root}")
    print(f"Output folder will be: {out_dir}\n")

    sources: List[Tuple[str, Path]] = []
    def gather(label: str, root_dir: Path):
        files = list(iter_files(root_dir, recursive=True))
        files.sort(key=lambda p: str(p.relative_to(root_dir)).lower())
        for p in files:
            sources.append((label, p))

    gather("A", cloud_path)
    gather("B", suite_path)

    log_path = out_dir / "merge_log.log"
    counts, logs = copy_unique_files(sources, out_dir, log_path=log_path)
    
    # -------- Summary of output file types --------
    acloud_count = 0
    asuite_count = 0
    common_count = 0

    for f in iter_files(out_dir):
        name = f.name

        # Suite-origin files may have both a leading "_" and "-asuite" suffix
        if name.startswith("_") and "-asuite" in name:
            asuite_count += 1
        elif "-asuite" in name:
            asuite_count += 1
        elif "-acloud" in name:
            acloud_count += 1
        else:
            common_count += 1

    # Print summary to stdout
    print("\n=== Output Summary ===")
    print(f"Common files (no suffix): {common_count}")
    print(f"Cloud-only (-acloud):     {acloud_count}")
    print(f"Suite-only (-asuite):     {asuite_count}")
    print("========================\n")

    # Append summary to merge_log.log
    try:
        with log_path.open("a", encoding="utf-8") as f:
            f.write("\n\n# Summary\n")
            f.write(f"Common files (no suffix): {common_count}\n")
            f.write(f"Cloud-only (-acloud):     {acloud_count}\n")
            f.write(f"Suite-only (-asuite):     {asuite_count}\n")
    except Exception:
        pass


    print("Done.")
    print(f"Written: {counts['written']} (from A: {counts['from_A']}, from B: {counts['from_B']})")
    print(f"Exact duplicates skipped: {counts['duplicates_skipped']}")
    print(f"Suite discarded by link-only preference: {counts['suite_discarded_by_link_only']}")
    print(f"Log file: {log_path}")
    

if __name__ == "__main__":
    main()
