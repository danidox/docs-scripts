#!/usr/bin/env python3
"""
img.py

Enhancements (this version):
- ✅ NEW: Rewrites <img src="..."> found **inside HTML <table>...</table> blocks** in .mdx files.
  * Downloads the image and replaces the src with the same /images/<subfolder>/<filename> path used for markdown images.
- Prompts (or --product-name) for images subfolder (e.g., 'ui-automations') and saves to ./images/<subfolder>/...
- Handles 503/408 (and other retryables) with Retry-After + capped exponential backoff.
- Supports blob/filename-style URLs (e.g., Azure Blob).
- Enforces naming: <product>-<alt>-<id>.<ext>, where:
    * product = root folder name where it runs (cwd name, slugified)
    * alt = alt attribute (slug)
    * id = last part of src (filename stem or numeric id for /api/binary)
- Rewrites markdown image links to /images/<subfolder>/<filename>
- Dedupes by (subfolder, id) and by content hash to avoid overwrites.
- Sanitizes MDX-escaped URLs (fixes cases like .../2020.4\_StudioX/plus\_menu.png).
- Writes failed download attempts to failed_downloads.log (tab-separated).

Usage:
    python img.py
    # prompts: "Images subfolder name (e.g., ui-automations): "

    python img.py --product-name ui-automations
"""

import os
import re
import pathlib
import urllib.parse
from urllib.parse import urlparse, urlunparse, quote, unquote
import time
import hashlib
import argparse
import requests
from requests.adapters import HTTPAdapter
from urllib3.util.retry import Retry
from typing import Tuple, Optional

# ------------- Patterns & constants -------------

IMG_MD_PATTERN = re.compile(
    r"!\[(?P<alt>[^\]]*)\]\(\s*(?P<url><[^>]*>|[^)\s]+)(?:\s+\"[^\"]*\")?\s*\)",
    flags=re.IGNORECASE,
)

# New: detect <table> blocks and <img ... src="..."> inside them
TABLE_BLOCK_PATTERN = re.compile(r"<table\b[^>]*>.*?</table>", re.IGNORECASE | re.DOTALL)
IMG_TAG_PATTERN = re.compile(r"<img\b[^>]*src=(?P<q>\"|\')(?P<src>.*?)(?P=q)[^>]*>", re.IGNORECASE | re.DOTALL)
SRC_ATTR_PATTERN = re.compile(r"(\bsrc\s*=\s*)([\"\'])(.*?)(\2)", re.IGNORECASE | re.DOTALL)
ALT_ATTR_PATTERN = re.compile(r"\balt\s*=\s*([\"\'])(.*?)\1", re.IGNORECASE | re.DOTALL)

_MIN_INTERVAL = 0.6  # throttle between requests (seconds)

CONTENT_TYPE_TO_EXT = {
    "image/png": ".webp",
    "image/jpeg": ".webp",
    "image/jpg": ".webp",
    "image/webp": ".webp",
    "image/gif": ".gif",
    "image/svg+xml": ".svg",
    "image/bmp": ".bmp",
    "image/tiff": ".tif",
}

RETRYABLE_STATUS = {408, 429, 500, 502, 503, 504}


# ------------- Helpers -------------

def normalize_slug(text: str) -> str:
    text = (text or "").strip().lower()
    text = re.sub(r"[^a-z0-9]+", "-", text)
    text = re.sub(r"-{2,}", "-", text)
    return text.strip("-") or "untitled"


def make_session() -> requests.Session:
    s = requests.Session()
    s.headers.update({"User-Agent": "md-img-downloader/1.8 (html-table-imgs)"})
    # We implement our own retry loop to precisely honor Retry-After; disable built-in total retries.
    retry = Retry(
        total=0,
        backoff_factor=0,
        status_forcelist=list(RETRYABLE_STATUS),
        allowed_methods=["GET"],
        raise_on_status=False,
        respect_retry_after_header=True,
    )
    adapter = HTTPAdapter(max_retries=retry)
    s.mount("https://", adapter)
    s.mount("http://", adapter)
    return s


SESSION = make_session()
_LAST_REQUEST_TS = 0.0


def throttled_get(url: str, timeout: int = 20) -> requests.Response:
    global _LAST_REQUEST_TS
    now = time.time()
    wait = _MIN_INTERVAL - (now - _LAST_REQUEST_TS)
    if wait > 0:
        time.sleep(wait)
    resp = SESSION.get(url, timeout=timeout)
    _LAST_REQUEST_TS = time.time()
    return resp


def _parse_retry_after(headers) -> Optional[float]:
    ra = headers.get("Retry-After")
    if not ra:
        return None
    ra = ra.strip()
    return float(ra) if ra.isdigit() else None


def _exp_backoff(attempt: int, base: float = 1.5, cap: float = 20.0) -> float:
    return min(cap, base ** attempt)


def download_with_backoff(url: str, timeout: int = 20, max_attempts: int = 6) -> Tuple[bytes, Optional[str]]:
    attempt = 0
    while True:
        resp = throttled_get(url, timeout=timeout)

        if resp.status_code in RETRYABLE_STATUS:
            attempt += 1
            if attempt >= max_attempts:
                resp.raise_for_status()

            retry_after = _parse_retry_after(resp.headers)
            if retry_after is None:
                retry_after = _exp_backoff(attempt)

            print(f"⏳ {resp.status_code} for {url}. Sleeping {retry_after:.1f}s (attempt {attempt}/{max_attempts-1})...")
            time.sleep(retry_after)
            continue

        resp.raise_for_status()
        return resp.content, (resp.headers.get("Content-Type"))


def ext_from_url_or_ct(url: str, content_type: Optional[str]) -> str:
    path = pathlib.Path(urllib.parse.urlparse(url).path)
    ext = path.suffix.lower()
    if ext in {".png", ".jpg", ".jpeg", ".gif", ".webp", ".svg", ".bmp", ".tif", ".tiff"}:
        return ".jpg" if ext == ".jpeg" else (".tif" if ext == ".tiff" else ext)
    if content_type:
        ct = content_type.split(";", 1)[0].strip().lower()
        if ct in CONTENT_TYPE_TO_EXT:
            return CONTENT_TYPE_TO_EXT[ct]
    return ".png"


def unique_path(base_dir: pathlib.Path, filename: str) -> pathlib.Path:
    target = base_dir / filename
    if not target.exists():
        return target
    stem, suf = target.stem, target.suffix
    i = 2
    while True:
        cand = base_dir / f"{stem}-{i}{suf}"
        if not cand.exists():
            return cand
        i += 1


def is_site_image(url: str) -> bool:
    return url.startswith("/images/")


def is_data_or_anchor(url: str) -> bool:
    return url.startswith("data:") or url.startswith("#")


# --------- URL Sanitization (fix MDX escapes like "\_") ----------

_MD_ESCAPE_PATTERN = re.compile(r"\\([_()\[\]!\*\.\-\s])")


def _unescape_markdown_escapes(text: str) -> str:
    # Replace backslash-escaped markdown punctuation with the literal char
    return _MD_ESCAPE_PATTERN.sub(lambda m: m.group(1), text)


def sanitize_mdx_url(url: str) -> str:
    """
    Clean up a URL that may include markdown backslash escapes or stray backslashes.
    Steps:
      1) Parse and percent-decode path/query/fragment.
      2) Remove markdown escapes like '\\_' -> '_'.
      3) Replace any remaining backslashes in path with '/' if they look like separators,
         otherwise drop them when they act as escapes.
      4) Re-encode the cleaned path/query/fragment and rebuild the URL.
    """
    parsed = urlparse(url)

    raw_path = unquote(parsed.path)
    raw_query = unquote(parsed.query)
    raw_fragment = unquote(parsed.fragment)

    cleaned_path = _unescape_markdown_escapes(raw_path)
    cleaned_query = _unescape_markdown_escapes(raw_query)
    cleaned_fragment = _unescape_markdown_escapes(raw_fragment)

    segments = cleaned_path.split('/')
    fixed_segments = []
    for seg in segments:
        if "\\" in seg:
            seg = seg.replace("\\\\", "/")
            seg = re.sub(r"(?<!^)[\\]+(?=[A-Za-z0-9])", "", seg)  # drop escapes before alnum
            seg = seg.replace("\\", "/")
            inner_parts = [p for p in seg.split("/") if p != ""]
            if inner_parts:
                fixed_segments.extend(inner_parts)
            else:
                fixed_segments.append(seg)
        else:
            fixed_segments.append(seg)

    fixed_path = "/".join(fixed_segments)

    safe_path = quote(fixed_path, safe="/-._~")
    safe_query = quote(cleaned_query, safe="=&-._~")
    safe_fragment = quote(cleaned_fragment, safe="-._~")

    sanitized = urlunparse((
        parsed.scheme,
        parsed.netloc,
        safe_path,
        parsed.params,
        safe_query,
        safe_fragment
    ))
    return sanitized


# --------- ID extraction helpers ----------

def extract_binary_image_id(url: str) -> Optional[str]:
    try:
        path = urlparse(url).path
    except Exception:
        return None
    parts = [p for p in path.split("/") if p]
    if len(parts) >= 5 and parts[0].lower() == "api" and parts[1].lower() == "binary":
        candidate = parts[-1]
        if candidate.isdigit():
            return candidate
    return None


def extract_filename_id_and_ext(url: str) -> Tuple[Optional[str], Optional[str]]:
    try:
        path = urlparse(url).path
    except Exception:
        return None, None
    last = pathlib.Path(path).name  # e.g., "WebNav-5.gif"
    if not last:
        return None, None
    stem = pathlib.Path(last).stem      # "WebNav-5"
    ext = pathlib.Path(last).suffix.lower()  # ".gif"
    if not stem:
        return None, None
    fixed_ext = ".jpg" if ext == ".jpeg" else (".tif" if ext == ".tiff" else ext) if ext else None
    return stem, fixed_ext


# ------------- Core primitives -------------

def ensure_download_and_site_path(
    raw_url: str,
    alt_text: str,
    url_bytes_cache: dict,
    id_to_site_path: dict,
    subfolder_name: str,
    product_root_name: str,
    failure_log_path: pathlib.Path,
    md_path: pathlib.Path,
) -> Optional[str]:
    """Download URL if needed and return the /images/... site path. Returns None on failure.
    Dedupes within the same run by (subfolder, id) and by content hash on disk.
    """
    url = sanitize_mdx_url(raw_url)

    # Skip transforming already-site images or data/anchors
    if is_site_image(url) or is_data_or_anchor(url):
        return None

    alt_slug = normalize_slug(alt_text or "image")

    # Prefer numeric binary ID when present; otherwise use filename-based id.
    bin_id = extract_binary_image_id(url)
    file_id, file_ext_hint = (None, None)
    if not bin_id:
        file_id, file_ext_hint = extract_filename_id_and_ext(url)

    dedupe_id = bin_id or file_id
    dedupe_key = (subfolder_name, dedupe_id) if dedupe_id else None

    # Save under ./images/<subfolder_name>/
    images_root = pathlib.Path.cwd() / "images" / subfolder_name
    images_root.mkdir(parents=True, exist_ok=True)

    try:
        # If we already saw this ID in the same run, reuse the existing site path
        if dedupe_key and dedupe_key in id_to_site_path:
            return id_to_site_path[dedupe_key]

        # Download (with backoff) or reuse in-memory cache by sanitized URL
        if url in url_bytes_cache:
            data, ct = url_bytes_cache[url]
        else:
            data, ct = download_with_backoff(url)
            url_bytes_cache[url] = (data, ct)

        # Extension resolution (URL hint wins; else content-type; else .png)
        ext = file_ext_hint or ext_from_url_or_ct(url, ct)

        # Decide <id> component (numeric, filename stem, or fallback)
        img_id = bin_id or (file_id if file_id else "img")

        # Filename: <product>-<alt>-<id>.<ext>
        base_filename = f"{product_root_name}-{alt_slug}-{img_id}{ext}"
        target_path = images_root / base_filename

        # If file exists, compare content. If different, uniquify.
        if target_path.exists():
            existing = target_path.read_bytes()
            if hashlib.sha256(existing).digest() != hashlib.sha256(data).digest():
                target_path = unique_path(images_root, base_filename)

        # Write file
        target_path.write_bytes(data)

        site_path = f"/images/{subfolder_name}/{target_path.name}"

        # Record dedupe mapping
        if dedupe_key:
            id_to_site_path[dedupe_key] = site_path

        if raw_url != url:
            print(f"[SANITIZED] {md_path}: {raw_url} -> {url}")
        print(f"✅ {md_path}: {url} -> {target_path} (link -> {site_path})")
        return site_path

    except Exception as e:
        print(f"⚠️ {md_path}: failed to process {raw_url}: {e}")
        try:
            with failure_log_path.open("a", encoding="utf-8") as logf:
                logf.write(f"{md_path}\t{raw_url}\t{e}\n")
        except Exception as log_err:
            print(f"⚠️ Could not write to log {failure_log_path}: {log_err}")
        return None


def process_markdown_images(
    content: str,
    md_path: pathlib.Path,
    url_bytes_cache: dict,
    id_to_site_path: dict,
    subfolder_name: str,
    product_root_name: str,
    failure_log_path: pathlib.Path,
) -> str:
    new_parts = []
    last_idx = 0
    for match in IMG_MD_PATTERN.finditer(content):
        start, end = match.span()
        new_parts.append(content[last_idx:start])

        alt = (match.group("alt") or "").strip()
        raw_url = (match.group("url") or "").strip()
        if raw_url.startswith("<") and raw_url.endswith(">"):
            raw_url = raw_url[1:-1].strip()

        site_path = ensure_download_and_site_path(
            raw_url, alt, url_bytes_cache, id_to_site_path,
            subfolder_name, product_root_name, failure_log_path, md_path,
        )

        if site_path:
            new_parts.append(f"![{alt}]({site_path})")
        else:
            # unchanged
            new_parts.append(match.group(0))

        last_idx = end

    new_parts.append(content[last_idx:])
    return "".join(new_parts)


def process_html_table_images(
    content: str,
    md_path: pathlib.Path,
    url_bytes_cache: dict,
    id_to_site_path: dict,
    subfolder_name: str,
    product_root_name: str,
    failure_log_path: pathlib.Path,
) -> str:
    """Find <table>...</table> blocks and rewrite <img src="..."> inside them."""

    def replace_img_tag(tag_html: str) -> str:
        # Extract alt (if any) to help with filename convention
        alt_match = ALT_ATTR_PATTERN.search(tag_html)
        alt_text = alt_match.group(2) if alt_match else ""

        # Extract src and compute new path
        m = IMG_TAG_PATTERN.search(tag_html)
        if not m:
            return tag_html
        raw_src = (m.group("src") or "").strip()

        site_path = ensure_download_and_site_path(
            raw_src, alt_text, url_bytes_cache, id_to_site_path,
            subfolder_name, product_root_name, failure_log_path, md_path,
        )
        if not site_path:
            return tag_html

        # Replace only the src attribute value, preserve original quoting & other attributes
        new_tag = SRC_ATTR_PATTERN.sub(lambda s: f"{s.group(1)}{s.group(2)}{site_path}{s.group(2)}", tag_html, count=1)
        return new_tag

    changed = False
    out_parts = []
    last = 0

    for tbl in TABLE_BLOCK_PATTERN.finditer(content):
        out_parts.append(content[last:tbl.start()])
        table_html = tbl.group(0)

        # Rewrite all <img ...> tags inside this table
        def _img_sub(m: re.Match) -> str:
            nonlocal changed
            new_tag = replace_img_tag(m.group(0))
            if new_tag != m.group(0):
                changed = True
            return new_tag

        new_table = IMG_TAG_PATTERN.sub(_img_sub, table_html)
        out_parts.append(new_table)
        last = tbl.end()

    out_parts.append(content[last:])
    return "".join(out_parts)


# ------------- CLI, prompt, and entry point -------------

def prompt_product_name() -> str:
    """
    Ask the user for the images subfolder name (e.g., 'ui-automations'),
    slugify it, and require a non-empty answer.
    """
    while True:
        raw = input("Images subfolder name (e.g., ui-automations): ").strip()
        product_name = normalize_slug(raw)
        if product_name:
            return product_name
        print("Please enter a non-empty name (letters and numbers).")


def process_mdx_file(
    md_path: pathlib.Path,
    url_bytes_cache: dict,
    id_to_site_path: dict,
    subfolder_name: str,
    product_root_name: str,
    failure_log_path: pathlib.Path,
):
    original = md_path.read_text(encoding="utf-8", errors="ignore")

    # 1) Rewrite markdown image syntax
    updated = process_markdown_images(
        original, md_path, url_bytes_cache, id_to_site_path,
        subfolder_name, product_root_name, failure_log_path,
    )

    # 2) Rewrite <img src> inside HTML tables
    updated2 = process_html_table_images(
        updated, md_path, url_bytes_cache, id_to_site_path,
        subfolder_name, product_root_name, failure_log_path,
    )

    if updated2 != original:
        md_path.write_text(updated2, encoding="utf-8")


def main():
    parser = argparse.ArgumentParser(description="Download & rewrite images in MDX (markdown + HTML tables).")
    parser.add_argument(
        "--product-name",
        help="Subfolder under images/ (e.g., 'ui-automations'). If omitted, you will be prompted.",
    )
    args = parser.parse_args()

    # Decide subfolder name: prefer CLI flag, else prompt interactively.
    subfolder_name = normalize_slug(args.product_name) if args.product_name else prompt_product_name()

    # product_root_name is the CWD folder, used in filename prefix per naming convention
    product_root_name = normalize_slug(pathlib.Path.cwd().name)

    # Open/create failure log in CWD
    failure_log_path = pathlib.Path("failed_downloads.log")
    if not failure_log_path.exists():
        try:
            failure_log_path.write_text("mdx_path\timage_url\terror\n", encoding="utf-8")
        except Exception as log_err:
            print(f"⚠️ Could not initialize log {failure_log_path}: {log_err}")

    url_bytes_cache: dict[str, tuple[bytes, Optional[str]]] = {}
    id_to_site_path: dict[tuple[str, str], str] = {}

    for md_path in pathlib.Path(".").rglob("*.md"):
        # avoid processing our own script or images folders named 'img'
        if any(p.name == "img" for p in md_path.parents):
            continue
        process_mdx_file(
            md_path,
            url_bytes_cache,
            id_to_site_path,
            subfolder_name=subfolder_name,
            product_root_name=product_root_name,
            failure_log_path=failure_log_path,
        )

    print("[DONE] Completed processing.")


if __name__ == "__main__":
    main()
