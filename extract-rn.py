#!/usr/bin/env python3
"""Extract embedded release-note pages from a user-guide publication into a
sibling release-notes publication, generating the required metadata, sidebar,
and redirect CSV files."""

from __future__ import annotations

import argparse
import json
import re
import sys
from dataclasses import dataclass
from pathlib import Path


def get_desktop_path() -> Path:
    """Return the actual Desktop path, handling OneDrive folder redirection on Windows."""
    try:
        import winreg
        with winreg.OpenKey(
            winreg.HKEY_CURRENT_USER,
            r"Software\Microsoft\Windows\CurrentVersion\Explorer\Shell Folders",
        ) as key:
            desktop, _ = winreg.QueryValueEx(key, "Desktop")
        return Path(desktop)
    except Exception:
        return Path.home() / "Desktop"


# ---------------------------------------------------------------------------
# JSON helpers
# ---------------------------------------------------------------------------

def read_json(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def write_json(path: Path, value: dict) -> None:
    path.write_text(json.dumps(value, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")


def update_frontmatter_slug(path: Path, slug: str, frontmatter_id: str) -> None:
    content = path.read_text(encoding="utf-8")
    match = re.match(r"^(---\r?\n)(.*?)(\r?\n---\r?\n)", content, re.DOTALL)
    if not match:
        raise ValueError(f"Missing YAML frontmatter in: {path}")

    frontmatter = match.group(2)
    if re.search(r"(?m)^slug:\s*.*$", frontmatter):
        frontmatter = re.sub(r"(?m)^slug:\s*.*$", f"slug: '{slug}'", frontmatter, count=1)
    else:
        frontmatter = frontmatter.rstrip() + f"\nslug: '{slug}'"

    if re.search(r"(?m)^id:\s*.*$", frontmatter):
        frontmatter = re.sub(r"(?m)^id:\s*.*$", f"id: {frontmatter_id}", frontmatter, count=1)
    else:
        frontmatter = frontmatter.rstrip() + f"\nid: {frontmatter_id}"

    updated = match.group(1) + frontmatter + match.group(3) + content[match.end():]
    path.write_text(updated, encoding="utf-8")


# ---------------------------------------------------------------------------
# Sidebar helpers
# ---------------------------------------------------------------------------

def get_descendant_hrefs(node: dict) -> list[str]:
    hrefs = []
    if href := node.get("href"):
        hrefs.append(href)
    for child in node.get("children") or []:
        hrefs.extend(get_descendant_hrefs(child))
    return hrefs


def get_release_section_info(sidebar: dict, embedded_basenames: set[str]) -> dict:
    children = sidebar.get("children") or []
    if not children:
        raise ValueError("Sidebar does not contain top-level children.")

    candidates = []
    for index, child in enumerate(children):
        title = child.get("title", "")
        hrefs = get_descendant_hrefs(child)
        matched = [h for h in hrefs if Path(h).name in embedded_basenames]

        if re.match(r"^Release Notes?$", title) or matched:
            candidates.append({
                "index": index,
                "node": child,
                "title": title,
                "hrefs": hrefs,
                "matched_hrefs": matched,
            })

    matching = [c for c in candidates if c["matched_hrefs"]]
    if len(matching) == 1:
        return matching[0]
    if len(matching) > 1:
        raise ValueError("Multiple top-level sidebar sections reference embedded release-note files.")
    if len(candidates) == 1:
        return candidates[0]
    if len(candidates) > 1:
        raise ValueError("Multiple top-level sidebar sections look like release-note sections.")
    raise ValueError("No top-level release-note section found in the user-guide sidebar.")


# ---------------------------------------------------------------------------
# Filename normalization
# ---------------------------------------------------------------------------

def normalize_release_note_basename(basename: str) -> str:
    stem = Path(basename).stem
    ext = Path(basename).suffix

    # Strip release-notes- prefix
    stem = re.sub(r"^release-notes-", "", stem)

    # Expand compact 8-digit date YYYYMMDD → YYYY-MM-DD
    if re.match(r"^\d{8}$", stem):
        stem = f"{stem[:4]}-{stem[4:6]}-{stem[6:]}"

    return stem + ext


# ---------------------------------------------------------------------------
# Repo helpers
# ---------------------------------------------------------------------------

def find_repo_root(start: Path) -> Path:
    current = start.resolve()
    for candidate in (current, *current.parents):
        if (candidate / ".git").exists():
            return candidate
    raise ValueError(f"Could not determine git repo root for: {start}")


# ---------------------------------------------------------------------------
# Scan
# ---------------------------------------------------------------------------

def find_eligible_doc_roots(root: Path) -> list[Path]:
    eligible = []
    for metadata_file in root.rglob("user-guide-metadata.json"):
        doc_root = metadata_file.parent
        user_guide = doc_root / "user-guide"
        release_notes_dir = doc_root / "release-notes"

        if not (doc_root / "user-guide-sidebar.json").exists():
            continue
        if not user_guide.is_dir():
            continue
        if (doc_root / "release-notes-metadata.json").exists():
            continue
        if release_notes_dir.exists() and any(release_notes_dir.iterdir()):
            continue

        embedded_files = list(user_guide.rglob("release-notes-*.md"))
        if not embedded_files:
            continue

        # Require a dedicated top-level "Release Notes" parent section in the sidebar
        # whose title matches "Release Notes" and which has children.
        # Skips doc roots where release-note files are scattered across product sections.
        try:
            sidebar = read_json(doc_root / "user-guide-sidebar.json")
            embedded_basenames = {f.name for f in embedded_files}
            section = get_release_section_info(sidebar, embedded_basenames)
            title = section["node"].get("title", "")
            if not re.match(r"^Release Notes?$", title, re.IGNORECASE):
                continue
            if not section["node"].get("children"):
                continue
        except (ValueError, KeyError):
            continue

        eligible.append(doc_root)
    return eligible


# ---------------------------------------------------------------------------
# Core extraction
# ---------------------------------------------------------------------------

@dataclass
class FileMove:
    relative_path: str          # original relative path inside user-guide
    normalized_relative_path: str
    source_path: Path
    target_path: Path


def extract(doc_root: Path, dry_run: bool) -> dict:
    root = doc_root.resolve()
    repo_root = find_repo_root(root)
    user_guide = root / "user-guide"
    user_guide_metadata_path = root / "user-guide-metadata.json"
    user_guide_sidebar_path = root / "user-guide-sidebar.json"
    release_notes_dir = root / "release-notes"
    release_notes_metadata_path = root / "release-notes-metadata.json"
    release_notes_sidebar_path = root / "release-notes-sidebar.json"

    # Validate prerequisites
    if not user_guide.is_dir():
        raise FileNotFoundError(f"Missing user-guide directory: {user_guide}")
    if not user_guide_metadata_path.exists():
        raise FileNotFoundError(f"Missing metadata file: {user_guide_metadata_path}")
    if not user_guide_sidebar_path.exists():
        raise FileNotFoundError(f"Missing sidebar file: {user_guide_sidebar_path}")

    embedded_files = list(user_guide.rglob("release-notes-*.md"))
    if not embedded_files:
        raise FileNotFoundError(f"No embedded release-note files found under {user_guide}")

    if release_notes_metadata_path.exists():
        raise FileExistsError(f"release-notes-metadata.json already exists: {release_notes_metadata_path}")
    if release_notes_sidebar_path.exists():
        raise FileExistsError(f"release-notes-sidebar.json already exists: {release_notes_sidebar_path}")
    if release_notes_dir.exists() and any(release_notes_dir.iterdir()):
        raise FileExistsError(f"release-notes directory already exists and is not empty: {release_notes_dir}")

    metadata = read_json(user_guide_metadata_path)
    sidebar = read_json(user_guide_sidebar_path)
    release_value = str(metadata["release"]).replace(".", "-")
    embedded_basenames = {f.name for f in embedded_files}
    release_section = get_release_section_info(sidebar, embedded_basenames)

    release_hrefs = list(dict.fromkeys(
        h for h in release_section["hrefs"]
        if "/user-guide/" in h and h.endswith(".md")
    ))
    if not release_hrefs:
        raise ValueError(
            f"The release-note sidebar section does not reference Markdown files "
            f"under user-guide: {user_guide_sidebar_path}"
        )

    # Build file move list
    files_to_move: list[FileMove] = []
    for href in release_hrefs:
        m = re.search(r"/user-guide/(.+\.md)$", href)
        if not m:
            raise ValueError(f"Release-note href does not point to a Markdown file under user-guide: {href}")
        relative_path = m.group(1)
        source_path = user_guide / relative_path
        if not source_path.exists():
            raise FileNotFoundError(f"Sidebar href points to a missing file: {source_path}")

        basename = Path(relative_path).name
        normalized_basename = normalize_release_note_basename(basename)
        relative_dir = str(Path(relative_path).parent)
        normalized_relative_path = (
            f"{relative_dir}/{normalized_basename}"
            if relative_dir != "."
            else normalized_basename
        )
        files_to_move.append(FileMove(
            relative_path=relative_path,
            normalized_relative_path=normalized_relative_path,
            source_path=source_path,
            target_path=release_notes_dir / normalized_relative_path,
        ))

    # Move files
    if not dry_run:
        release_notes_dir.mkdir(exist_ok=True)
    else:
        print(f"  [dry-run] Would create directory: {release_notes_dir}")

    for f in files_to_move:
        if not dry_run:
            f.target_path.parent.mkdir(parents=True, exist_ok=True)
            f.source_path.rename(f.target_path)
            file_stem = Path(f.normalized_relative_path).stem
            frontmatter_id = f"{metadata['productNameSlug']}-{release_value}-{file_stem}"
            update_frontmatter_slug(f.target_path, file_stem, frontmatter_id)
        else:
            print(f"  [dry-run] Would move: {f.source_path} -> {f.target_path}")

    # Build release-notes-metadata.json
    release_notes_metadata = {
        "productName":         metadata["productName"],
        "productNameSlug":     metadata["productNameSlug"],
        "release":             metadata["release"],
        "publicationType":     "Release Notes",
        "publicationTypeSlug": "release-notes",
        "deliveryOption":      metadata["deliveryOption"],
        "deliveryOptionSlug":  metadata["deliveryOptionSlug"],
        "description":         metadata.get("description"),
        "displayOrder":        "1",
        "enabledEnvironments": {
            "dev": True,
            "stg": False,
            "prod": False,
        },
    }

    # Build release-notes-sidebar.json — rewrite hrefs from /user-guide/release-notes-* to /release-notes/*
    release_section_json = json.dumps(release_section["node"], ensure_ascii=False)
    release_section_json = re.sub(r"/user-guide/release-notes-", "/release-notes/", release_section_json)
    release_section_node = json.loads(release_section_json)
    release_notes_sidebar = {
        "title": f"{metadata['productName']} release notes",
        "children": [release_section_node],
    }

    # Remove release-notes section from user-guide sidebar
    sidebar["children"] = [
        child for i, child in enumerate(sidebar.get("children") or [])
        if i != release_section["index"]
    ]

    if not dry_run:
        write_json(release_notes_metadata_path, release_notes_metadata)
        write_json(release_notes_sidebar_path, release_notes_sidebar)
        write_json(user_guide_sidebar_path, sidebar)
    else:
        print(f"  [dry-run] Would write: {release_notes_metadata_path}")
        print(f"  [dry-run] Would write: {release_notes_sidebar_path}")
        print(f"  [dry-run] Would update: {user_guide_sidebar_path}")

    # Increment displayOrder in all sibling *-metadata.json files
    sibling_metadata_files = [
        p for p in root.glob("*-metadata.json")
        if p.name != "release-notes-metadata.json"
    ]
    for sibling_path in sibling_metadata_files:
        sibling_metadata = read_json(sibling_path)
        sibling_metadata["displayOrder"] = str(int(sibling_metadata["displayOrder"]) + 1)
        if not dry_run:
            write_json(sibling_path, sibling_metadata)
        else:
            print(f"  [dry-run] Would increment displayOrder in: {sibling_path}")

    # Build redirect CSV
    doc_root_url_path = "/" + root.relative_to(repo_root).as_posix()
    csv_rows = []
    for f in files_to_move:
        old_slug = Path(f.relative_path).stem
        new_slug = Path(f.normalized_relative_path).stem
        old_url = f"{doc_root_url_path}/user-guide/{old_slug}"
        new_url = f"{doc_root_url_path}/release-notes/{new_slug}"
        csv_rows.append(f"{old_url},307,{new_url}")
        csv_rows.append(f"/@languageCode{old_url},307,/@languageCode{new_url}")

    csv_folder = get_desktop_path() / "release notes redirects"
    doc_root_label = root.relative_to(repo_root).as_posix().replace("/", "-")
    csv_path = csv_folder / f"redirects-{doc_root_label}.csv"

    if not dry_run:
        csv_folder.mkdir(parents=True, exist_ok=True)
        csv_path.write_text("\n".join(csv_rows) + "\n", encoding="utf-8")
    else:
        print(f"  [dry-run] Would write redirect CSV: {csv_path}")
        for row in csv_rows:
            print(f"    {row}")

    return {
        "doc_root":                   str(root),
        "files_moved":                len(files_to_move),
        "release_notes_dir":          str(release_notes_dir),
        "release_notes_metadata":     str(release_notes_metadata_path),
        "release_notes_sidebar":      str(release_notes_sidebar_path),
        "updated_user_guide_sidebar": str(user_guide_sidebar_path),
        "updated_sibling_metadata":   [str(p) for p in sibling_metadata_files],
        "redirect_csv":               str(csv_path),
    }


# ---------------------------------------------------------------------------
# Entry point
# ---------------------------------------------------------------------------

def main() -> None:
    parser = argparse.ArgumentParser(
        description="Extract embedded release notes from a user-guide publication."
    )
    group = parser.add_mutually_exclusive_group(required=True)
    group.add_argument(
        "--doc-roots", nargs="+", metavar="PATH",
        help="One or more explicit doc root paths to extract.",
    )
    group.add_argument(
        "--root", metavar="PATH",
        help="Scan this directory recursively for eligible doc roots.",
    )
    parser.add_argument(
        "--dry-run", action="store_true",
        help="Print what would be done without making any changes.",
    )
    args = parser.parse_args()

    if args.root:
        scan_root = Path(args.root).resolve()
        doc_roots = find_eligible_doc_roots(scan_root)
        if not doc_roots:
            print("No eligible doc roots found.")
            return
        print(f"Found {len(doc_roots)} eligible doc root(s):")
        for p in doc_roots:
            print(f"  {p}")
        print()
    else:
        doc_roots = [Path(p) for p in args.doc_roots]

    for doc_root in doc_roots:
        print(f"Processing: {doc_root}")
        try:
            result = extract(doc_root, dry_run=args.dry_run)
            print(f"  Files moved:       {result['files_moved']}")
            print(f"  Release notes dir: {result['release_notes_dir']}")
            print(f"  Redirect CSV:      {result['redirect_csv']}")
        except Exception as e:
            print(f"  ERROR: {e}", file=sys.stderr)
        print()


if __name__ == "__main__":
    main()
