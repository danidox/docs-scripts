#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Scrape a docs page sidebar and output:
  1) <slug>-sidebar.json  (Docusaurus-friendly tree; hrefs for depth >= 2)
  2) <slug>-metadata.json (derived from URL slug)

Update (2025-09-25):
- Output filenames now use the *second to last* segment of the input URL.
  Examples:
    - https://docs.uipath.com/agents/automation-cloud/latest/release-notes/2025
        -> release-notes-sidebar.json, release-notes-metadata.json
    - https://docs.uipath.com/agents/automation-cloud/latest/user-guide/about-this-guide
        -> user-guide-sidebar.json, user-guide-metadata.json
- (Keeps behavior) For each <li>, the sidebar item's href is taken from the same <a href="..."> inside that <li>.
"""

import json
import sys
import re
import posixpath
from typing import List, Dict, Optional
from urllib.parse import urljoin, urlparse, unquote

try:
    import requests
    from bs4 import BeautifulSoup, Tag, NavigableString
except ImportError:
    print("Please install dependencies first:\n  pip install requests beautifulsoup4")
    sys.exit(1)


# SSO-aware HTTP helpers (docs-dev support)
from sso import sso_get_with_retries, safe_get_html

# ------------------------ Config ------------------------
HREF_MIN_DEPTH = 2  # add hrefs starting from this depth (relative to wrapper)

# ------------------------ URL / slug utilities ------------------------

def _segments(url: str) -> List[str]:
    parsed = urlparse(url)
    return [unquote(s) for s in (parsed.path or "").split("/") if s]

def _titleify(slug: str) -> str:
    s = re.sub(r"[-_]+", " ", slug or "").strip()
    return s.title()

def derive_guide_type_slug(url: str) -> Optional[str]:
    # Retained for compatibility; unused for filenames now.
    for seg in _segments(url):
        if "guide" in seg.lower():
            return seg
    return None


def derive_guide_name_from_slug(url: str) -> str:
    """
    Build the main sidebar title from the URL:
      Title = "<Product> <Guide Type>"
    - Product = first path segment (e.g., "agents" -> "Agents")
    - Guide Type = second-to-last segment (e.g., "release-notes" -> "Release Notes")
    """
    segs = _segments(url)
    product_slug = segs[0].lower() if len(segs) >= 1 else ""
    # Guide type anchored to the second-to-last segment
    guide_type_slug = segs[-2].lower() if len(segs) >= 2 else (segs[-1].lower() if segs else "")

    product = _titleify(product_slug) if product_slug else "Guide"
    # guide type in sentence case: fully lowercased, then only first letter kept as-is
    guide_type = re.sub(r"[-_]+", " ", guide_type_slug).strip().lower()

    title = f"{product} {guide_type}".strip()
    return title
    if not guide_kind:
        tail = segs[-1] if segs else "Guide"
        tail = re.sub(r"\.[a-z0-9]+$", "", tail, flags=re.I)
        tail = re.sub(r"[-_]+", " ", tail).strip()
        return f"{_titleify(product)} {(tail or 'guide').lower()}"
    return f"{_titleify(product)} {_titleify(guide_kind).lower()}"


def derive_metadata_from_url(url: str) -> Dict[str, str]:
    segs = _segments(url)
    product_slug = segs[0].lower() if len(segs) >= 1 else ""
    delivery_slug = segs[1].lower() if len(segs) >= 2 else ""
    release = segs[2] if len(segs) >= 3 else ""
    # NEW: publication type is always the second-to-last segment
    pubtype_slug = segs[-2].lower() if len(segs) >= 2 else ""
    return {
        "productName": _titleify(product_slug) if product_slug else "",
        "productNameSlug": product_slug,
        "release": release,
        "publicationType": _titleify(pubtype_slug) if pubtype_slug else "",
        "publicationTypeSlug": pubtype_slug,
        "deliveryOption": _titleify(delivery_slug) if delivery_slug else "",
        "deliveryOptionSlug": delivery_slug,
    }

# New: filename stem from second-to-last URL segment
_SLUG_SAFE = re.compile(r"[^a-z0-9\-]+")

def slugify(text: str) -> str:
    s = unquote((text or "").lower().strip())
    s = s.replace("&", " and ")
    s = re.sub(r"[^\w\s\-]+", "", s)
    s = re.sub(r"\s+", "-", s)
    s = _SLUG_SAFE.sub("", s)
    s = re.sub(r"-{2,}", "-", s).strip("-")
    return s or "item"

def filename_stem_from_url(url: str) -> str:
    segs = _segments(url)
    # Use second-to-last segment when available; otherwise fallback to last; otherwise "output"
    candidate = segs[-2] if len(segs) >= 2 else (segs[-1] if segs else "output")
    return slugify(candidate)

# ------------------------ Clean-text helpers ------------------------

BANNED_TAGS = {"style", "script", "noscript", "link", "meta", "button", "svg", "path"}
ICON_CLASS_HINT = re.compile(r"(icon|chevron|toggle|caret|expand)", re.I)

CSS_CLASS_BLOCK = re.compile(r"\.[A-Za-z0-9_-]+\s*\{[^}]*\}")
CSS_ID_BLOCK   = re.compile(r"#[A-Za-z0-9_-]+\s*\{[^}]*\}")
CSS_DECLARATION = re.compile(r"[A-Za-z_-]+\s*:\s*[^;{}]+\s*;")
CURLY_BLOCK = re.compile(r"\{[^{}]*\}")

def looks_like_css(s: str) -> bool:
    s = (s or "").strip()
    if ("{" in s and "}" in s) or CSS_DECLARATION.search(s or ""):
        if len(s) > 30 or ("{" in s and "}" in s):
            return True
    if (s.startswith(".") or s.startswith("#")) and "{" in s:
        return True
    return False

def clean_text_value(s: str) -> str:
    s = CSS_CLASS_BLOCK.sub(" ", s or "")
    s = CSS_ID_BLOCK.sub(" ", s)
    s = CSS_DECLARATION.sub(" ", s)
    s = CURLY_BLOCK.sub(" ", s)
    s = re.sub(r"\s+", " ", s).strip()
    return s

def is_visible_element(tag: Tag) -> bool:
    if tag.name in BANNED_TAGS:
        return False
    if tag.has_attr("aria-hidden") and str(tag["aria-hidden"]).lower() == "true":
        return False
    classes = " ".join(tag.get("class") or [])
    if ICON_CLASS_HINT.search(classes or ""):
        return False
    return True

def first_meaningful_text(node: Tag) -> str:
    a = node.find("a", recursive=False)
    if a:
        txt = a.get_text(" ", strip=True)
        if txt and not looks_like_css(txt):
            return clean_text_value(txt)
    for child in node.children:
        if isinstance(child, NavigableString):
            txt = str(child).strip()
            if txt and not looks_like_css(txt):
                return clean_text_value(txt)
        elif isinstance(child, Tag):
            if child.name == "ul" or not is_visible_element(child):
                continue
            txt = child.get_text(" ", strip=True)
            if txt and not looks_like_css(txt):
                return clean_text_value(txt)
    pieces = []
    for child in node.children:
        if isinstance(child, Tag):
            if child.name == "ul" or not is_visible_element(child):
                continue
            pieces.append(child.get_text(" ", strip=True))
        elif isinstance(child, NavigableString):
            pieces.append(str(child))
    return clean_text_value(" ".join(pieces))

# ------------------------ URL/path helpers for .mdx ------------------------

def path_dirname(path: str) -> str:
    if not path.startswith("/"):
        path = "/" + path
    d = posixpath.dirname(path)
    return d if d else "/"

def strip_ext(path: str) -> str:
    base, _ = posixpath.splitext(path)
    return base

def ensure_mdx_path_from_href(href: str, base_url: str) -> Optional[str]:
    """Resolve <a href> to absolute URL, then return site-absolute path with .mdx."""
    if not href:
        return None
    abs_url = urljoin(base_url, href)
    parsed = urlparse(abs_url)
    path = parsed.path or "/"
    if path.endswith("/"):
        path = posixpath.join(path, "index.mdx")
    else:
        path = strip_ext(path) + ".mdx"
    path = re.sub(r"//+", "/", path)
    if not path.startswith("/"):
        path = "/" + path
    return path

def derive_child_path_from_parent_dir(title: str, parent_dir: str) -> str:
    slug = slugify(title)
    return posixpath.join(parent_dir if parent_dir else "/", slug + ".mdx")

# ------------------------ Sidebar parsing ------------------------

def pick_sidebar_root(soup: BeautifulSoup) -> Optional[Tag]:
    preferred_keys = ("sidebar", "sidebarmenu")
    candidates = []
    for ul in soup.find_all("ul"):
        if not isinstance(ul, Tag):
            continue
        id_ = (ul.get("id") or "").lower()
        classes = " ".join(ul.get("class") or []).lower()
        if any(k in id_ for k in preferred_keys) or any(k in classes for k in preferred_keys):
            candidates.append(ul)
    if candidates:
        return max(candidates, key=lambda el: len(el.find_all("li")))
    uls = soup.find_all("ul")
    if not uls:
        return None
    return max(uls, key=lambda el: len(el.find_all("li")))

def href_from_li(li: Tag, base_url: str) -> Optional[str]:
    """
    Look inside the same <li> and take the first <a href="..."> value,
    normalized to a site-absolute .mdx path.
    """
    a = li.find("a", href=True)
    if a:
        return ensure_mdx_path_from_href(a["href"], base_url)
    return None

def li_to_item(li: Tag, base_url: str, depth: int, parent_dir: str, page_dir: str) -> Optional[Dict]:
    header_like = None
    for child in li.children:
        if isinstance(child, Tag) and child.name in ("div", "span", "a"):
            header_like = child
            break

    title_container = header_like if header_like else li
    title = first_meaningful_text(title_container)
    if not title:
        a = li.find("a")
        if a and a.get_text(strip=True):
            title = clean_text_value(a.get_text(" ", strip=True))
    if not title:
        return None

    item: Dict = {"title": title}

    mdx_path = href_from_li(li, base_url)

    # Add href only for depth >= HREF_MIN_DEPTH
    if depth >= HREF_MIN_DEPTH:
        if mdx_path:
            item["href"] = mdx_path
        else:
            base_dir = parent_dir or page_dir or "/"
            item["href"] = derive_child_path_from_parent_dir(title, base_dir)

    # Directory to pass to children
    this_dir = parent_dir
    if mdx_path:
        this_dir = path_dirname(mdx_path)

    child_ul = li.find("ul", recursive=False)
    if child_ul:
        children: List[Dict] = []
        for child_li in child_ul.find_all("li", recursive=False):
            child_item = li_to_item(child_li, base_url, depth + 1, this_dir, page_dir)
            if child_item:
                children.append(child_item)
        if children:
            item["children"] = children

    return item

def ul_to_items(ul: Tag, base_url: str, depth: int, parent_dir: str, page_dir: str) -> List[Dict]:
    items: List[Dict] = []
    for li in ul.find_all("li", recursive=False):
        item = li_to_item(li, base_url, depth, parent_dir, page_dir)
        if item:
            items.append(item)
    return items

# ------------------------ Build & CLI ------------------------

def build_sidebar_from_url(url: str) -> Dict:
    headers = {"User-Agent": "SidebarScraper/1.5 (+https://example.local)"}
    import requests
    session = requests.Session()
    resp = safe_get_html(url, session=session, timeout=30)
    resp.raise_for_status()

    soup = BeautifulSoup(resp.text, "html.parser")

    for tname in list(BANNED_TAGS):
        for t in soup.find_all(tname):
            t.decompose()

    root = pick_sidebar_root(soup)
    if not root:
        raise RuntimeError("Could not locate a sidebar <ul> in this page.")

    guide_title = derive_guide_name_from_slug(url)
    page_dir = path_dirname(urlparse(url).path or "/")

    children = ul_to_items(root, base_url=url, depth=1, parent_dir=page_dir, page_dir=page_dir)
    return {"title": guide_title, "children": children}

def main():
    try:
        url = input("Enter the URL that contains the sidebar: ").strip()
        if not url:
            print("No URL provided. Exiting.")
            return

        sidebar_rooted = build_sidebar_from_url(url)

        stem = filename_stem_from_url(url)  # second-to-last URL segment
        sidebar_filename = f"{stem}-sidebar.json"
        metadata_filename = f"{stem}-metadata.json"

        metadata = derive_metadata_from_url(url)

        with open(sidebar_filename, "w", encoding="utf-8") as f:
            json.dump(sidebar_rooted, f, ensure_ascii=False, indent=2)

        with open(metadata_filename, "w", encoding="utf-8") as f:
            json.dump(metadata, f, ensure_ascii=False, indent=2)

        print(f"✅ Wrote {sidebar_filename} and {metadata_filename}")
        print(f"ℹ️ Filenames are based on the second-to-last URL segment: '{stem}'")
        print(f"ℹ️ Hrefs are taken from the <li>'s own <a href> and included for items at depth ≥ {HREF_MIN_DEPTH}.")
    except Exception as e:
        print("❌ Error:", e)
        sys.exit(1)

if __name__ == "__main__":
    main()
