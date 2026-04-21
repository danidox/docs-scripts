#!/usr/bin/env python3
"""
Count topic GUID reuse from DITA .ditamap files (maps-only) while skipping any map
whose filename contains 'Guide' (case-insensitive). Also records the submap GUID
(or file path fallback) for each occurrence.

Topic filename pattern (example):
  Setting up directory roles and permissions=GUID-1A31F2EF-AF43-434C-9BA1-A5879471AF61=3=en=.xml

Map filename pattern (if present):
  My Map=GUID-ABCDEF0123=1=en=.ditamap
If no GUID is present in the map filename, we fall back to 'FILE:<relative path>'.

Output:
  CSV columns: GUID, Title, Version, Count, SubmapGUIDs
  JSON: [{ "GUID", "Title", "Version", "Count", "SubmapGUIDs": [...] }]

Usage:
  python find_guid_reuse.py . --out-csv reused_topics.csv --out-json reused_topics.json
  python find_guid_reuse.py /path/to/dita --products ProductA ProductB
"""

import argparse
import csv
import json
import os
import sys
import xml.etree.ElementTree as ET
from collections import defaultdict

MAP_EXT = ".ditamap"

def ditamap_is_excluded(path: str) -> bool:
    """Exclude any .ditamap whose *filename* contains 'guide' (case-insensitive)."""
    return "guide" in os.path.basename(path).lower()

def strip_fragment(href: str) -> str:
    """Remove any #fragment from href."""
    return href.split("#", 1)[0]

def is_ditamap(path: str) -> bool:
    return path.lower().endswith(MAP_EXT)

def safe_parse_xml(path):
    try:
        return ET.parse(path)
    except ET.ParseError:
        return None

def norm_rel(root, path):
    ap = os.path.normpath(os.path.abspath(path))
    ar = os.path.normpath(os.path.abspath(root))
    try:
        rel = os.path.relpath(ap, ar)
    except ValueError:
        rel = ap
    return rel.replace("\\", "/")

def find_all_maps(product_dir):
    """Return all eligible .ditamap files under product_dir (excluding '*Guide*.ditamap')."""
    maps = []
    for dirpath, _, filenames in os.walk(product_dir):
        for fn in filenames:
            if fn.lower().endswith(MAP_EXT):
                full = os.path.join(dirpath, fn)
                if not ditamap_is_excluded(full):
                    maps.append(full)
    return maps

def gather_product_dirs(root, specific_products=None):
    """Detect product folders: subfolders that contain at least one eligible .ditamap."""
    if specific_products:
        candidates = [os.path.join(root, p) for p in specific_products]
    else:
        candidates = [os.path.join(root, d) for d in os.listdir(root)
                      if os.path.isdir(os.path.join(root, d))]
    product_dirs = []
    for d in candidates:
        has_map = False
        for _, _, filenames in os.walk(d):
            if any(fn.lower().endswith(MAP_EXT) and "guide" not in fn.lower() for fn in filenames):
                has_map = True
                break
        if has_map:
            product_dirs.append(d)
    return product_dirs

def parse_guid_title_version_from_filename(filename: str):
    """
    Given a topic file name like:
      Title=GUID-...=Version=en=.xml
    return (GUID, Title, Version) or (None, None, None) if not matched.
    """
    base = os.path.basename(filename)
    if base.lower().endswith(".xml"):
        core = base[:-4]
    else:
        core = base
    tokens = core.split("=")
    guid_idx = None
    for i, tok in enumerate(tokens):
        if tok.startswith("GUID-"):
            guid_idx = i
            break
    if guid_idx is None:
        return (None, None, None)
    title = "=".join(tokens[:guid_idx]).strip()
    guid = tokens[guid_idx].strip()
    version = None
    if guid_idx + 1 < len(tokens):
        candidate = tokens[guid_idx + 1].strip()
        if candidate != "":
            version = candidate
    if not title or not guid:
        return (None, None, None)
    return (guid, title, version)

def parse_map_guid_from_filename(map_path: str):
    """
    Try to extract a GUID from a .ditamap filename using the same pattern:
      Name=GUID-...=...=.ditamap
    Returns the GUID string or None if not present.
    """
    base = os.path.basename(map_path)
    if base.lower().endswith(".ditamap"):
        core = base[:-8]  # remove '.ditamap'
    else:
        core = base
    tokens = core.split("=")
    for tok in tokens:
        if tok.startswith("GUID-"):
            return tok.strip()
    return None

def collect_keydefs_from_map(map_path):
    """
    Return:
      keydefs: dict key -> absolute topic path (from href targets that are NOT .ditamap)
      submaps: list of absolute submap paths (eligible only)
    """
    keydefs = {}
    submaps = []
    tree = safe_parse_xml(map_path)
    if tree is None:
        return keydefs, submaps

    root = tree.getroot()
    for elem in root.iter():
        href = elem.attrib.get("href") or elem.attrib.get("{*}href")
        keys = elem.attrib.get("keys") or elem.attrib.get("{*}keys")
        fmt = (elem.attrib.get("format") or elem.attrib.get("{*}format") or "").lower()

        if href:
            href_no_frag = strip_fragment(href)
            if not href_no_frag:
                continue
            tgt_abs = os.path.normpath(os.path.join(os.path.dirname(map_path), href_no_frag))
            # Submaps
            if fmt == "ditamap" or href_no_frag.lower().endswith(MAP_EXT):
                if os.path.isfile(tgt_abs) and not ditamap_is_excluded(tgt_abs):
                    submaps.append(tgt_abs)
            else:
                # Keydef: keys + href to a topic file
                if keys and os.path.isfile(tgt_abs):
                    for k in keys.split():
                        keydefs[k] = tgt_abs
    return keydefs, submaps

def gather_map_tree_keydefs(root_map):
    """DFS over map tree (skipping '*Guide*.ditamap') to merge keydefs."""
    merged = {}
    seen = set()
    stack = [root_map]
    while stack:
        mp = stack.pop()
        if mp in seen or ditamap_is_excluded(mp):
            continue
        seen.add(mp)
        kd, subs = collect_keydefs_from_map(mp)
        for k, v in kd.items():
            if k not in merged:
                merged[k] = v
        for sm in subs:
            if not ditamap_is_excluded(sm):
                stack.append(sm)
    return merged

def count_guid_refs_in_map_tree(root_map, counts, submaps_by_guid, root_dir):
    """
    Traverse the map tree, collecting GUID counts from:
      - <topicref href="..."> to topic files (non-.ditamap)
      - <topicref keyref="..."> resolved via keydefs
    Also record, for each occurrence, the GUID (or fallback) of the *map* where it was found.
    """
    keydefs = gather_map_tree_keydefs(root_map)
    seen_maps = set()
    stack = [root_map]

    while stack:
        mp = stack.pop()
        if mp in seen_maps or ditamap_is_excluded(mp):
            continue
        seen_maps.add(mp)

        tree = safe_parse_xml(mp)
        if tree is None:
            continue
        root = tree.getroot()

        # Determine the "map id" to record for occurrences from this map
        map_guid = parse_map_guid_from_filename(mp)
        if map_guid is None:
            map_guid = f"FILE:{norm_rel(root_dir, mp)}"

        # Collect submaps while iterating this map
        local_submaps = []

        for elem in root.iter():
            href = elem.attrib.get("href") or elem.attrib.get("{*}href")
            keyref = elem.attrib.get("keyref") or elem.attrib.get("{*}keyref")
            fmt = (elem.attrib.get("format") or elem.attrib.get("{*}format") or "").lower()

            # Submaps for traversal
            if href:
                href_no_frag = strip_fragment(href)
                if href_no_frag and (fmt == "ditamap" or href_no_frag.lower().endswith(MAP_EXT)):
                    sm_abs = os.path.normpath(os.path.join(os.path.dirname(mp), href_no_frag))
                    if os.path.isfile(sm_abs) and not ditamap_is_excluded(sm_abs):
                        local_submaps.append(sm_abs)

            # Direct href to a topic file
            if href:
                href_no_frag = strip_fragment(href)
                if href_no_frag:
                    tgt_abs = os.path.normpath(os.path.join(os.path.dirname(mp), href_no_frag))
                    if os.path.isfile(tgt_abs) and not is_ditamap(tgt_abs):
                        guid, title, version = parse_guid_title_version_from_filename(tgt_abs)
                        if guid:
                            if guid not in counts:
                                counts[guid] = [title, version, 0]
                            counts[guid][2] += 1
                            submaps_by_guid[guid].append(map_guid)

            # keyref -> resolve to a topic target
            if keyref:
                tgt = keydefs.get(keyref)
                if tgt and os.path.isfile(tgt) and not is_ditamap(tgt):
                    guid, title, version = parse_guid_title_version_from_filename(tgt)
                    if guid:
                        if guid not in counts:
                            counts[guid] = [title, version, 0]
                        counts[guid][2] += 1
                        submaps_by_guid[guid].append(map_guid)

        # Continue traversal
        for sm in local_submaps:
            stack.append(sm)

def main():
    ap = argparse.ArgumentParser(description="Count GUID reuse from DITA .ditamap files (skip '*Guide*.ditamap') and record submap GUIDs per occurrence.")
    ap.add_argument("root", help="Path to DITA root (use '.' if running inside the root)")
    ap.add_argument("--products", nargs="*", help="Limit to these product folder names (relative to root)")
    ap.add_argument("--out-csv", default="reused_topics.csv", help="CSV output path")
    ap.add_argument("--out-json", default="reused_topics.json", help="JSON output path")
    args = ap.parse_args()

    root_dir = os.path.abspath(args.root)
    if not os.path.isdir(root_dir):
        print(f"Root not found: {root_dir}", file=sys.stderr)
        sys.exit(2)

    product_dirs = gather_product_dirs(root_dir, args.products)
    if not product_dirs:
        print("No product folders with eligible .ditamap files found.", file=sys.stderr)
        sys.exit(1)

    # GUID -> [Title, Version, Count]
    counts = {}
    # GUID -> [map_guid_or_file, map_guid_or_file, ...] (one entry per occurrence)
    submaps_by_guid = defaultdict(list)

    for pdir in product_dirs:
        start_maps = find_all_maps(pdir)
        for mp in start_maps:
            count_guid_refs_in_map_tree(mp, counts, submaps_by_guid, root_dir)

    # Prepare rows
    rows = []
    for guid, (title, version, cnt) in counts.items():
        submap_guids = submaps_by_guid.get(guid, [])
        rows.append({
            "GUID": guid,
            "Title": title or "",
            "Version": version or "",
            "Count": cnt,
            "SubmapGUIDs": submap_guids,
        })

    # Sort by Count desc, then GUID
    rows.sort(key=lambda r: (-int(r["Count"]), r["GUID"]))

    # Write CSV (SubmapGUIDs as semicolon-separated, preserving duplicates)
    csv_path = os.path.abspath(args.out_csv)
    with open(csv_path, "w", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames=["GUID", "Title", "Version", "Count", "SubmapGUIDs"])
        w.writeheader()
        for r in rows:
            r_out = r.copy()
            r_out["SubmapGUIDs"] = ";".join(r["SubmapGUIDs"])
            w.writerow(r_out)

    # Write JSON (array of objects)
    json_path = os.path.abspath(args.out_json)
    with open(json_path, "w", encoding="utf-8") as jf:
        json.dump(rows, jf, indent=2, ensure_ascii=False)

    print(f"Wrote CSV: {csv_path}")
    print(f"Wrote JSON: {json_path}")

if __name__ == "__main__":
    main()
