#!/usr/bin/env python3
"""
image_pipeline_plus_spacing.py

One-stop script that:
1) Scans Markdown/MDX files in the current repo, downloads linked images
   (markdown syntax and <img> tags in <table> blocks) into ./images/<subfolder>/...,
   and rewrites the links to site-local paths.
2) Finds any .svg files in that images folder (or a chosen folder) and converts them
   to .webp using Inkscape or ImageMagick for rasterization, then Pillow for WebP
   encoding. Optional in-place link rewrite from .svg to .webp in Markdown/MDX.
3) Ensures there is a blank line before each Markdown image line of the form:
   `![alt](url)`.

Default behavior:
- SVG→WebP conversion and link rewriting are ENABLED.
- Image-spacing normalization (blank line before image lines) is ENABLED.
"""

import re
import os
import sys
import time
import shutil
import argparse
import pathlib
import hashlib
import tempfile
import subprocess
import urllib.parse
from typing import Tuple, Optional
from urllib.parse import urlparse, urlunparse, quote, unquote

import requests
from PIL import Image
from requests.adapters import HTTPAdapter
from urllib3.util.retry import Retry

# ---------------- Patterns & constants ----------------

IMG_MD_PATTERN = re.compile(
    r'!\[(?P<alt>[^\]]*)\]\(\s*(?P<url><[^>]*>|[^)\s]+)(?:\s+"[^"]*")?\s*\)',
    flags=re.IGNORECASE,
)

TABLE_BLOCK_PATTERN = re.compile(r"<table\b[^>]*>.*?</table>", re.IGNORECASE | re.DOTALL)
IMG_TAG_PATTERN = re.compile(r'<img\b[^>]*src=(?P<q>"|\')(?P<src>.*?)(?P=q)[^>]*>', re.IGNORECASE | re.DOTALL)
SRC_ATTR_PATTERN = re.compile(r'(\bsrc\s*=\s*)(["\'])(.*?)(\2)', re.IGNORECASE | re.DOTALL)
ALT_ATTR_PATTERN = re.compile(r'\balt\s*=\s*(["\'])(.*?)\1', re.IGNORECASE | re.DOTALL)

# From the spacing script: a markdown image line we want to normalize
IMAGE_LINE_RE = re.compile(r'^\s*!\[[^\]]*\]\([^)]+\)')

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
_MD_ESCAPE_PATTERN = re.compile(r'\\([_()\[\]!\*\.\-\s])')

# ---------------- HTTP session & utilities ----------------

def normalize_slug(text: str) -> str:
    text = (text or "").strip().lower()
    text = re.sub(r"[^a-z0-9]+", "-", text)
    text = re.sub(r"-{2,}", "-", text)
    return text.strip("-") or "untitled"

def make_session() -> requests.Session:
    s = requests.Session()
    s.headers.update({"User-Agent": "md-img-downloader/2.0 (unified-pipeline)"})
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

def _unescape_markdown_escapes(text: str) -> str:
    return _MD_ESCAPE_PATTERN.sub(lambda m: m.group(1), text)

def sanitize_mdx_url(url: str) -> str:
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
            seg = re.sub(r"(?<!^)[\\]+(?=[A-Za-z0-9])", "", seg)
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
    last = pathlib.Path(path).name
    if not last:
        return None, None
    stem = pathlib.Path(last).stem
    ext = pathlib.Path(last).suffix.lower()
    if not stem:
        return None, None
    fixed_ext = ".jpg" if ext == ".jpeg" else (".tif" if ext == ".tiff" else ext) if ext else None
    return stem, fixed_ext

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

# ---------------- Image download & rewrite core ----------------

def ensure_download_and_site_path(
    raw_url: str,
    alt_text: str,
    url_bytes_cache: dict,
    id_to_site_path: dict,
    hash_to_site_path: dict,        # content-hash dedupe map
    subfolder_name: str,
    product_root_name: str,
    failure_log_path: pathlib.Path,
    md_path: pathlib.Path,
    stats: dict
) -> Optional[str]:
    url = sanitize_mdx_url(raw_url)

    if is_site_image(url) or is_data_or_anchor(url):
        return None

    # Count each actionable image reference we try to handle.
    stats["image_refs_processed"] += 1

    alt_slug = normalize_slug(alt_text or "image")

    bin_id = extract_binary_image_id(url)
    file_id, file_ext_hint = (None, None)
    if not bin_id:
        file_id, file_ext_hint = extract_filename_id_and_ext(url)

    dedupe_id = bin_id or file_id
    dedupe_key = (subfolder_name, dedupe_id) if dedupe_id else None

    images_root = pathlib.Path.cwd() / "images" / subfolder_name
    images_root.mkdir(parents=True, exist_ok=True)

    try:
        # 1) Fast path: if we’ve already mapped this logical id this run, reuse.
        if dedupe_key and dedupe_key in id_to_site_path:
            site_path = id_to_site_path[dedupe_key]
            stats["duplicates_skipped"] += 1
            if raw_url != url:
                print(f"[SANITIZED] {md_path}: {raw_url} -> {url}")
            print(f"🔁  {md_path}: {url} → duplicate (reuse {pathlib.Path(site_path).name})")
            return site_path

        # 2) Download (or reuse URL cache)
        if url in url_bytes_cache:
            data, ct = url_bytes_cache[url]
        else:
            data, ct = download_with_backoff(url)
            url_bytes_cache[url] = (data, ct)

        # 3) Content-hash based dedupe (handles different URLs with same bytes)
        digest = hashlib.sha256(data).hexdigest()
        if digest in hash_to_site_path:
            site_path = hash_to_site_path[digest]
            if dedupe_key:
                id_to_site_path[dedupe_key] = site_path
            stats["duplicates_skipped"] += 1
            if raw_url != url:
                print(f"[SANITIZED] {md_path}: {raw_url} -> {url}")
            print(f"🔁  {md_path}: {url} → duplicate (reuse {pathlib.Path(site_path).name})")
            return site_path

        # 4) Determine extension and filename
        ext = file_ext_hint or ext_from_url_or_ct(url, ct)
        img_id = bin_id or (file_id if file_id else "img")
        raw_stem = f"{product_root_name}-{alt_slug}-{img_id}"
        # compute max filename length dynamically based on full path
        probe_path = images_root / ("X" * 255 + ext)
        max_filename_len = 255 - (len(str(probe_path)) - 255)
        
        if max_filename_len <= len(ext) + 10:
            max_filename_len = len(ext) + 10  # absolute safety floor

        # shorten stem and add hash for uniqueness
        digest8 = hashlib.sha1(raw_stem.encode("utf-8")).hexdigest()[:8]
        trimmed_stem = raw_stem[: max_filename_len - len(ext) - 9]

        base_filename = f"{trimmed_stem}-{digest8}{ext}"
        target_path = images_root / base_filename
        

        # 5) If a file with same name exists but different bytes, uniquify; if same bytes, dedupe.
        if target_path.exists():
            existing = target_path.read_bytes()
            if hashlib.sha256(existing).digest() != hashlib.sha256(data).digest():
                target_path = unique_path(images_root, base_filename)
            else:
                site_path = f"/images/{subfolder_name}/{target_path.name}"
                hash_to_site_path[digest] = site_path
                if dedupe_key:
                    id_to_site_path[dedupe_key] = site_path
                stats["duplicates_skipped"] += 1
                if raw_url != url:
                    print(f"[SANITIZED] {md_path}: {raw_url} -> {url}")
                print(f"🔁  {md_path}: {url} → duplicate (reuse {pathlib.Path(site_path).name})")
                return site_path

        # 6) Write file once per unique content
        target_path.write_bytes(data)
        site_path = f"/images/{subfolder_name}/{target_path.name}"

        # Remember mappings
        hash_to_site_path[digest] = site_path
        if dedupe_key:
            id_to_site_path[dedupe_key] = site_path

        stats["new_images_saved"] += 1

        if raw_url != url:
            print(f"[SANITIZED] {md_path}: {raw_url} -> {url}")
        print(f"✅  {md_path}: {url} → {site_path}")
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
    hash_to_site_path: dict,
    subfolder_name: str,
    product_root_name: str,
    failure_log_path: pathlib.Path,
    stats: dict,
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
            raw_url, alt, url_bytes_cache, id_to_site_path, hash_to_site_path,
            subfolder_name, product_root_name, failure_log_path, md_path, stats
        )

        if site_path:
            new_parts.append(f"![{alt}]({site_path})")
        else:
            new_parts.append(match.group(0))

        last_idx = end

    new_parts.append(content[last_idx:])
    return "".join(new_parts)

def process_html_table_images(
    content: str,
    md_path: pathlib.Path,
    url_bytes_cache: dict,
    id_to_site_path: dict,
    hash_to_site_path: dict,
    subfolder_name: str,
    product_root_name: str,
    failure_log_path: pathlib.Path,
    stats: dict,
) -> str:
    def replace_img_tag(tag_html: str) -> str:
        alt_match = ALT_ATTR_PATTERN.search(tag_html)
        alt_text = alt_match.group(2) if alt_match else ""
        m = IMG_TAG_PATTERN.search(tag_html)
        if not m:
            return tag_html
        raw_src = (m.group("src") or "").strip()

        site_path = ensure_download_and_site_path(
            raw_src, alt_text, url_bytes_cache, id_to_site_path, hash_to_site_path,
            subfolder_name, product_root_name, failure_log_path, md_path, stats
        )
        if not site_path:
            return tag_html

        new_tag = SRC_ATTR_PATTERN.sub(lambda s: f"{s.group(1)}{s.group(2)}{site_path}{s.group(2)}", tag_html, count=1)
        return new_tag

    out_parts = []
    last = 0
    for tbl in TABLE_BLOCK_PATTERN.finditer(content):
        out_parts.append(content[last:tbl.start()])
        table_html = tbl.group(0)

        def _img_sub(m: re.Match) -> str:
            new_tag = replace_img_tag(m.group(0))
            return new_tag

        new_table = IMG_TAG_PATTERN.sub(_img_sub, table_html)
        out_parts.append(new_table)
        last = tbl.end()

    out_parts.append(content[last:])
    return "".join(out_parts)

# ---------------- Image spacing helpers (from second script) ----------------

def insert_blank_lines_before_markdown_images(text: str) -> str:
    """
    Ensures there is a blank line before each Markdown image line:
    lines that start with `![alt](url)` (possibly with leading whitespace).
    """
    lines = text.splitlines(keepends=True)
    output: list[str] = []

    for line in lines:
        if IMAGE_LINE_RE.match(line):
            if output and output[-1].strip() != "":
                output.append("\n")
            output.append(line)
        else:
            output.append(line)

    return "".join(output)

# ---------------- SVG -> WebP helpers ----------------

def have(cmd: str) -> bool:
    return shutil.which(cmd) is not None

def run_cmd(cmd, **kwargs):
    try:
        subprocess.run(cmd, check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, **kwargs)
        return True, ""
    except subprocess.CalledProcessError as e:
        return False, e.stderr.decode(errors="ignore")

def convert_with_inkscape(svg_path: pathlib.Path, tmp_png: pathlib.Path, width: Optional[int], height: Optional[int], scale: Optional[float]):
    cmd = ["inkscape", str(svg_path), "--export-type=png", f"--export-filename={tmp_png}"]
    if width:
        cmd.append(f"--export-width={width}")
    if height:
        cmd.append(f"--export-height={height}")
    if scale:
        cmd.append(f"--export-dpi={96*scale}")
    return run_cmd(cmd)

def convert_with_imagemagick(svg_path: pathlib.Path, tmp_png: pathlib.Path, width: Optional[int], height: Optional[int], scale: Optional[float]):
    resize = None
    if width and height:
        resize = f"{width}x{height}!"
    elif width:
        resize = f"{width}x"
    elif height:
        resize = f"x{height}"
    cmd = ["magick", str(svg_path), "-background", "none"]
    if resize:
        cmd += ["-resize", resize]
    elif scale:
        cmd += ["-resize", f"{int(scale*100)}%"]
    cmd += [str(tmp_png)]
    return run_cmd(cmd)

def save_webp_from_png(png_path: pathlib.Path, webp_path: pathlib.Path, quality: int, lossless: bool, method: int):
    webp_path.parent.mkdir(parents=True, exist_ok=True)
    with Image.open(png_path) as im:
        im = im.convert("RGBA")
        params = {"lossless": lossless, "method": method}
        if not lossless:
            params["quality"] = quality
        im.save(webp_path, format="WEBP", **params)

def find_svgs(folder: pathlib.Path):
    return sorted(p for p in folder.rglob("*.svg"))

def convert_svgs_to_webp(input_dir: pathlib.Path, output_dir: pathlib.Path,
                         width: Optional[int], height: Optional[int], scale: Optional[float],
                         quality: int, lossless: bool, method: int) -> Tuple[int, int]:
    """
    Returns: (converted_count, failures)
    """
    svgs = find_svgs(input_dir)
    if not svgs:
        print(f"No .svg files found in {input_dir}")
        return (0, 0)

    use_inkscape = have("inkscape")
    use_magick = have("magick")
    if not (use_inkscape or use_magick):
        print("Neither Inkscape nor ImageMagick ('magick') is available in PATH.", file=sys.stderr)
        print("Install one of these, then re-run:")
        print("  - Inkscape: winget install Inkscape.Inkscape")
        print("  - ImageMagick: winget install ImageMagick.ImageMagick")
        return (0, -1)

    failures = 0
    converted = 0
    for svg in svgs:
        rel = svg.relative_to(input_dir)
        webp_path = output_dir / rel.with_suffix(".webp")
        webp_path.parent.mkdir(parents=True, exist_ok=True)

        with tempfile.TemporaryDirectory() as td:
            tmp_png = pathlib.Path(td) / (svg.stem + ".png")

            if use_inkscape:
                ok, err = convert_with_inkscape(svg, tmp_png, width, height, scale)
                if not ok and use_magick:
                    ok, err = convert_with_imagemagick(svg, tmp_png, width, height, scale)
            else:
                ok, err = convert_with_imagemagick(svg, tmp_png, width, height, scale)

            if not ok:
                print(f"✗ Failed to rasterize {svg}: {err}", file=sys.stderr)
                failures += 1
                continue

            try:
                save_webp_from_png(tmp_png, webp_path, quality, lossless, method)
                print(f"🖼️  {svg} → {webp_path}")
                converted += 1
            except Exception as e:
                print(f"✗ Failed to write {webp_path}: {e}", file=sys.stderr)
                failures += 1

    return (converted, failures)

# ---------------- .svg -> .webp link rewriting ----------------

def rewrite_svg_links_to_webp_in_text(text: str) -> str:
    text = re.sub(r"(\(/images/[^\)\s]+?)\.svg(\))", r"\1.webp\2", text)
    text = re.sub(r'(src\s*=\s*["\'])(/images/[^"\']+?)\.svg(["\'])', r'\1\2.webp\3', text, flags=re.IGNORECASE)
    return text

def apply_link_rewrites(root: pathlib.Path):
    for md_path in root.rglob("*.md*"):
        original = md_path.read_text(encoding="utf-8", errors="ignore")
        updated = rewrite_svg_links_to_webp_in_text(original)
        if updated != original:
            md_path.write_text(updated, encoding="utf-8")
            print(f"🔗 Rewrote .svg -> .webp links in {md_path}")

# ---------------- CLI, prompt, and entry point ----------------

def prompt_product_name() -> str:
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
    hash_to_site_path: dict,
    subfolder_name: str,
    product_root_name: str,
    failure_log_path: pathlib.Path,
    stats: dict,
    enable_image_spacing: bool,
):
    original = md_path.read_text(encoding="utf-8", errors="ignore")

    # Phase 1: download & rewrite markdown image links
    updated = process_markdown_images(
        original, md_path, url_bytes_cache, id_to_site_path, hash_to_site_path,
        subfolder_name, product_root_name, failure_log_path, stats
    )

    # Phase 2: handle <img> tags inside HTML <table>s
    updated2 = process_html_table_images(
        updated, md_path, url_bytes_cache, id_to_site_path, hash_to_site_path,
        subfolder_name, product_root_name, failure_log_path, stats
    )

    # Phase 3: normalize spacing before markdown image lines
    if enable_image_spacing:
        updated3 = insert_blank_lines_before_markdown_images(updated2)
    else:
        updated3 = updated2

    if updated3 != original:
        md_path.write_text(updated3, encoding="utf-8")

def main():
    parser = argparse.ArgumentParser(
        description="Download & rewrite images in MDX, convert SVGs to WebP, and normalize image spacing."
    )
    parser.add_argument(
        "--product-name",
        help="Subfolder under images/ (e.g., 'ui-automations'). If omitted, you will be prompted.",
    )
    # Defaults: enabled; provide negative flags to opt out
    parser.add_argument(
        "--no-svg-to-webp",
        action="store_true",
        help="Disable automatic SVG to WebP conversion (enabled by default)",
    )
    parser.add_argument(
        "--svg-root",
        type=pathlib.Path,
        default=None,
        help="Root folder to search for SVGs (default: ./images/<subfolder>)",
    )
    parser.add_argument(
        "--svg-output",
        type=pathlib.Path,
        default=None,
        help="Output folder for .webp (default: same as svg-root)",
    )
    parser.add_argument(
        "--no-replace-svg-links",
        action="store_true",
        help="Disable automatic .svg -> .webp link rewrite (enabled by default)",
    )

    parser.add_argument(
        "--width",
        type=int,
        default=None,
        help="Output width in px (SVG rasterization)",
    )
    parser.add_argument(
        "--height",
        type=int,
        default=None,
        help="Output height in px (SVG rasterization)",
    )
    parser.add_argument(
        "--scale",
        type=float,
        default=None,
        help="Scale factor (e.g. 2 for 2x)",
    )
    parser.add_argument(
        "--quality",
        type=int,
        default=90,
        help="WebP quality 0-100 (ignored if --lossless)",
    )
    parser.add_argument(
        "--lossless",
        action="store_true",
        help="Use lossless WebP",
    )
    parser.add_argument(
        "--method",
        type=int,
        default=4,
        choices=range(0, 7),
        help="WebP effort (0=fast, 6=best)",
    )

    parser.add_argument(
        "--no-image-spacing",
        action="store_true",
        help="Disable inserting blank lines before markdown image lines.",
    )

    args = parser.parse_args()

    subfolder_name = normalize_slug(args.product_name) if args.product_name else prompt_product_name()
    product_root_name = normalize_slug(pathlib.Path.cwd().name)

    enable_image_spacing = not args.no_image_spacing

    # Stats for summary
    stats = {
        "image_refs_processed": 0,
        "new_images_saved": 0,
        "duplicates_skipped": 0,
        "svg_converted": 0,
        "svg_failed": 0,
    }

    failure_log_path = pathlib.Path("failed_downloads.log")
    if not failure_log_path.exists():
        try:
            failure_log_path.write_text("mdx_path\timage_url\terror\n", encoding="utf-8")
        except Exception as log_err:
            print(f"⚠️ Could not initialize log {failure_log_path}: {log_err}")

    url_bytes_cache: dict[str, tuple[bytes, Optional[str]]] = {}
    id_to_site_path: dict[tuple[str, str], str] = {}
    hash_to_site_path: dict[str, str] = {}   # content-hash -> /images/... path

    # Phase 1: download & rewrite MD/MDX across repo + spacing normalization
    for md_path in pathlib.Path(".").rglob("*.md*"):
        if any(p.name == "img" for p in md_path.parents):
            continue
        process_mdx_file(
            md_path,
            url_bytes_cache,
            id_to_site_path,
            hash_to_site_path,
            subfolder_name=subfolder_name,
            product_root_name=product_root_name,
            failure_log_path=failure_log_path,
            stats=stats,
            enable_image_spacing=enable_image_spacing,
        )

    print("[DOWNLOAD & SPACING DONE] Images processed, links rewritten, and image spacing normalized.")

    # Phase 2: default = convert SVG->WebP and rewrite links
    if not args.no_svg_to_webp:
        default_svg_root = pathlib.Path("images") / subfolder_name
        svg_root = (args.svg_root or default_svg_root).resolve()
        webp_out = (args.svg_output or svg_root).resolve()
        webp_out.mkdir(parents=True, exist_ok=True)

        converted, failures = convert_svgs_to_webp(
            input_dir=svg_root,
            output_dir=webp_out,
            width=args.width,
            height=args.height,
            scale=args.scale,
            quality=args.quality,
            lossless=args.lossless,
            method=args.method,
        )
        if failures < 0:
            sys.exit(1)

        stats["svg_converted"] = converted
        stats["svg_failed"] = failures

        print("[SVG CONVERSION DONE]" + (f" with {failures} failures." if failures else ""))

        if not args.no_replace_svg_links:
            apply_link_rewrites(pathlib.Path("."))
            print("[LINK REWRITE DONE] .svg references updated to .webp for /images/... paths.")

    # Terminal + file summary
    summary = (
        f"images: processed={stats['image_refs_processed']}, "
        f"new_saved={stats['new_images_saved']}, duplicates={stats['duplicates_skipped']}; "
        f"svg: converted={stats['svg_converted']}, failures={stats['svg_failed']}"
    )
    print("\n=== SUMMARY ===")
    print(f"Image refs processed : {stats['image_refs_processed']}")
    print(f"New images saved     : {stats['new_images_saved']}  ✅")
    print(f"Duplicates skipped   : {stats['duplicates_skipped']}  🔁")
    print(f"SVGs converted       : {stats['svg_converted']}  🖼️")
    print(f"SVG conversion fails : {stats['svg_failed']}")
    print("[SUMMARY] " + summary)

    try:
        pathlib.Path("image_pipeline_summary.log").write_text(summary + "\n", encoding="utf-8")
    except Exception as e:
        print(f"⚠️ Could not write summary log: {e}")

    print("[ALL DONE] Completed processing.")

if __name__ == "__main__":
    main()
