#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Combined MDX converter + Sidebar/Metadata generator.

For every URL you input:
  - Converts the docs content to .mdx (crawling same-site pages).
  - Builds a Docusaurus-friendly sidebar JSON and a metadata JSON whose filenames
    are based on the second-to-last URL segment:
      <stem>-sidebar.json
      <stem>-metadata.json

Sidebar & metadata are saved under the <product>/<delivery>/<version> folder of the URL.
Examples:
  https://docs.uipath.com/automation-ops/automation-suite/2024.10/user-guide/release-notes-2024-10-0
      -> automation-ops/automation-suite/2024.10/<stem>-sidebar.json
         automation-ops/automation-suite/2024.10/<stem>-metadata.json
"""

import os
import re
import time
import random
import json
import posixpath
import urllib.parse
import email.utils
from datetime import datetime, timezone
from typing import List, Dict, Optional

import requests
from bs4 import BeautifulSoup, NavigableString, Tag
import markdownify as md

# =========================
# === MDX MAKER HELPERS ===
# =========================

# Map id-fragment in span id to literal replacements to insert into Markdown.
# PH_PLACEHOLDER_MAP = {"PH_AFJ_TFR_W2C": "{{Product_solutions}}",
    # Add more mappings as needed:
    # "PH_SOME_OTHER": "{{Product_other}}",}

# HTTP fetch with retries/backoff
DEFAULT_USER_AGENT = "UiPathDocScraper/1.0 (+https://uipath.com)"
GLOBAL_THROTTLE_SECONDS = 0.4  # polite delay between successful requests

def _parse_retry_after(value: str) -> float:
    r"""Parse Retry-After header which may be seconds or HTTP-date; return seconds to wait."""
    if not value:
        return 0.0
    v = value.strip()
    if v.isdigit():
        return float(v)
    try:
        dt = email.utils.parsedate_to_datetime(v)
        if dt.tzinfo is None:
            dt = dt.replace(tzinfo=timezone.utc)
        now = datetime.now(timezone.utc)
        return max(0.0, (dt - now).total_seconds())
    except Exception:
        return 0.0

def get_with_retries(url, session=None, max_tries=5, base_sleep=1.0, timeout=20):
    """GET with retries for 429 and 5xx, honoring Retry-After and using exponential backoff + jitter."""
    s = session or requests.Session()
    headers = {"User-Agent": DEFAULT_USER_AGENT}
    tries = 0
    while True:
        tries += 1
        try:
            resp = s.get(url, headers=headers, timeout=timeout)
            if resp.status_code == 429:
                wait = _parse_retry_after(resp.headers.get("Retry-After"))
                if wait <= 0:
                    wait = base_sleep * (2 ** (tries - 1))
                wait *= (1 + random.random() * 0.25)
                if tries >= max_tries:
                    resp.raise_for_status()
                time.sleep(wait)
                continue
            if 500 <= resp.status_code < 600:
                if tries >= max_tries:
                    resp.raise_for_status()
                wait = base_sleep * (2 ** (tries - 1))
                wait *= (1 + random.random() * 0.25)
                time.sleep(wait)
                continue
            resp.raise_for_status()
            time.sleep(GLOBAL_THROTTLE_SECONDS)
            return resp
        except requests.exceptions.HTTPError as e:
            status = getattr(e.response, "status_code", None)
            if status and 500 <= status < 600 and tries < max_tries:
                wait = base_sleep * (2 ** (tries - 1))
                wait *= (1 + random.random() * 0.25)
                time.sleep(wait)
                continue
            raise
        except requests.exceptions.RequestException:
            if tries < max_tries:
                wait = base_sleep * (2 ** (tries - 1))
                wait *= (1 + random.random() * 0.25)
                time.sleep(wait)
                continue
            raise

_PLACEHOLDER_RE = re.compile(r"{{[^}]*}}")

def replace_ph_spans_with_placeholders(container: BeautifulSoup, id_map: dict) -> None:
    r"""Replace <span class="ph" id="...{key}...">...</span> with the mapped literal text.
    This removes the span wrapper entirely and inserts a raw text node so Markdown
    contains the literal placeholder (no escaping like \_).
    """
    if not container:
        return
    for sp in list(container.find_all("span", class_="ph")):
        sid = sp.get("id") or ""
        if not sid:
            continue
        for id_fragment, replacement_text in id_map.items():
            if id_fragment in sid:
                sp.replace_with(NavigableString(replacement_text))
                break

def unescape_md_in_placeholders(md_text: str) -> str:
    r"""Undo escapes like \_ \{ \} inside {{...}} only."""
    def _fix(m):
        inner = m.group(0)[2:-2]
        inner = inner.replace(r"\_", "_").replace(r"\{", "{").replace(r"\}", "}")
        return "{{" + inner + "}}"
    return _PLACEHOLDER_RE.sub(_fix, md_text)

def transform_availability_images(container: BeautifulSoup) -> None:
    """Replace inline <img> with alt 'available'/'not available'/'yes'/'no' to emojis."""
    for img in list(container.find_all("img")):
        alt = (img.get("alt") or "").strip().lower()
        if alt in ("available", "yes"):
            img.replace_with(NavigableString("✅"))
        elif alt in ("not available", "no"):
            img.replace_with(NavigableString("❌"))


def extract_complex_tables(container: BeautifulSoup):
    """Replace complex tables with placeholders and return {placeholder: sanitized_table_html}."""
    table_html_map = {}
    counter = 1
    for table in list(container.find_all("table")):
        has_list = table.find(["ul", "ol", "li"]) is not None
        has_note = table.find("div", class_=lambda c: c and "note" in c.split()) is not None
        has_rowspan = any(cell.has_attr("rowspan") for cell in table.find_all(["td", "th"]))
        has_colspan = any(cell.has_attr("colspan") for cell in table.find_all(["td", "th"]))
        if has_list or has_note or has_rowspan or has_colspan:
            placeholder = f"HTMLTABLEPLACEHOLDER{counter}"
            counter += 1
            raw_html = str(table)
            clean_html = sanitize_table_html(raw_html)
            table_html_map[placeholder] = clean_html
            table.replace_with(NavigableString(placeholder))
    return table_html_map

def pretty_table_html(table_html: str) -> str:
    soup = BeautifulSoup(table_html, "html.parser")
    table = soup.find("table")
    if not table:
        return table_html.strip()
    pretty = table.prettify(formatter="html")
    pretty = re.sub(r"\n{3,}", "\n\n", pretty)
    return pretty.strip()

def sanitize_table_html(table_html: str) -> str:
    soup = BeautifulSoup(table_html, "html.parser")
    table = soup.find("table")
    if not table:
        return table_html
    whitelist = {
        "table": set(), "thead": set(), "tbody": set(), "tfoot": set(),
        "tr": set(), "th": {"colspan", "rowspan", "scope", "headers", "abbr"},
        "td": {"colspan", "rowspan", "headers", "abbr"},
        "colgroup": {"span"}, "col": {"span"},
        "a": {"href", "title"}, "img": {"src", "alt", "width", "height", "loading"},
        "ul": set(), "ol": set(), "li": set(), "p": set(), "div": set(), "span": set(),
        "strong": set(), "em": set(), "code": set(), "pre": set(),"sup": set(), "sub": set(),
    }
    for tag in table.descendants:
        if not getattr(tag, "attrs", None):
            continue
        name = getattr(tag, "name", "").lower()
        if not name:
            continue
        keep = whitelist.get(name, set())
        new_attrs = {}
        for k, v in list(tag.attrs.items()):
            if k.lower() in keep:
                new_attrs[k.lower()] = v.strip() if isinstance(v, str) else v
        tag.attrs = new_attrs
    for sp in list(table.find_all("span")):
        if not sp.attrs:
            sp.unwrap()
    for dv in list(table.find_all("div")):
        if not dv.attrs:
            dv.unwrap()
    return pretty_table_html(str(table))
    
_SUP_PLACEHOLDER_RE = re.compile(r"(SUPTAGPLACEHOLDER\d+)")
def protect_sup_tags(container: BeautifulSoup, prefix: str = "SUPTAGPLACEHOLDER") -> Dict[str, str]:
    """
    Replace <sup>...</sup> with unique text placeholders so markdownify won't strip them.
    Returns {placeholder: '<sup>...</sup>'}.
    """
    mapping = {}
    counter = 1
    for sup in list(container.find_all("sup")):
        placeholder = f"{prefix}{counter}"
        counter += 1
        mapping[placeholder] = str(sup)  # keep full HTML (may include nested tags)
        sup.replace_with(NavigableString(placeholder))
    return mapping

def restore_sup_placeholders(md_text: str, mapping: Dict[str, str]) -> str:
    if not mapping:
        return md_text
    # Replace placeholders with raw <sup> HTML (do not escape)
    for ph, html in mapping.items():
        md_text = md_text.replace(ph, html)
    return md_text
    
def protect_sup_tags(container: BeautifulSoup, prefix: str = "SUPTAGPLACEHOLDER") -> Dict[str, str]:
    """
    Replace <sup>...</sup> with placeholders. Normalize them so restored
    HTML is always <sup>...</sup> (no attributes).
    """
    mapping = {}
    counter = 1
    for sup in list(container.find_all("sup")):
        placeholder = f"{prefix}{counter}"
        counter += 1
        # Create a new <sup> without attributes
        clean_sup = BeautifulSoup("<sup></sup>", "html.parser").sup
        clean_sup.string = sup.get_text()  # preserve only the text
        mapping[placeholder] = str(clean_sup)
        sup.replace_with(NavigableString(placeholder))
    return mapping

def remove_leading_h2(md_text: str) -> str:
    """
    Remove the very first '## ...' heading at the start of the Markdown content,
    leaving all other headings untouched.
    """
    lines = md_text.splitlines()
    new_lines = []
    removed = False
    for line in lines:
        if not removed and line.strip().startswith("## "):
            removed = True
            continue
        new_lines.append(line)
    return "\n".join(new_lines).lstrip("\n")


def remove_empty_tags(container: BeautifulSoup):
    """Remove tags that are effectively empty (no text and no non-empty children)."""
    VOID = {"img", "br", "hr", "col", "colgroup", "source"}
    PROTECTED = {"table", "thead", "tbody", "tfoot", "tr", "th", "td"}
    changed = True
    while changed:
        changed = False
        for tag in list(container.find_all(True)):
            if tag.name in VOID or tag.name in PROTECTED:
                continue
            has_images = tag.find("img") is not None
            text = tag.get_text(strip=True)
            has_non_void_child = any(
                (child.name not in VOID) for child in tag.find_all(True, recursive=False)
            )
            if not text and not has_non_void_child and not has_images:
                tag.decompose()
                changed = True

def cleanup_markdown(md_text: str) -> str:
    md_text = md_text.replace(r"\*\*", "**")
    md_text = md_text.replace(r"\*", "*")
    return md_text

def prefix_relative_markdown_links(md_text: str, domain: str = "https://docs.uipath.com") -> str:
    """Convert relative Markdown and HTML links to absolute docs.uipath.com URLs."""
    md_pattern = re.compile(
        r'(?<!\!)\['
        r'(?P<text>[^\]]+)\]'
        r'\('
        r'(?P<url>[^)\s]+)'
        r'(?P<title>\s+"[^"]*")?'
        r'\)'
    )
    def md_repl(m):
        text, url, title = m.group('text'), m.group('url'), m.group('title') or ''
        if url.startswith(('http://', 'https://', 'mailto:', '#', '//')):
            return m.group(0)
        base = domain.rstrip('/')
        fixed = base + url if url.startswith('/') else f"{base}/{url}"
        return f'[{text}]({fixed}{title})'
    md_text = md_pattern.sub(md_repl, md_text)

    html_pattern = re.compile(
        r'<a\s+([^>]*?)href="(?P<url>[^"]+)"([^>]*)>(?P<text>.*?)</a>',
        flags=re.IGNORECASE | re.DOTALL
    )
    def html_repl(m):
        url, text = m.group('url'), m.group('text')
        before, after = m.group(1), m.group(3)
        if url.startswith(('http://', 'https://', 'mailto:', '#', '//')):
            return m.group(0)
        base = domain.rstrip('/')
        fixed = base + url if url.startswith('/') else f"{base}/{url}"
        return f'<a {before}href="{fixed}"{after}>{text}</a>'
    return html_pattern.sub(html_repl, md_text)

def _remove_notetitle_nodes(inner_soup: BeautifulSoup) -> None:
    class_like = re.compile(r"(^|\b)(note[-_ ]?title|notetitle)(\b|$)", re.I)
    for el in list(inner_soup.find_all(True)):
        classes = " ".join(el.get("class", []))
        el_id = el.get("id", "")
        if class_like.search(classes) or class_like.search(el_id or ""):
            el.decompose()
            continue
        for attr in list(el.attrs.keys()):
            if re.search(r"(^|:)notetitle$", attr, re.I):
                del el.attrs[attr]

def _strip_leading_note_title(inner_soup: BeautifulSoup) -> None:
    def try_strip_textnode(node: NavigableString) -> bool:
        if not isinstance(node, NavigableString):
            return False
        txt = str(node)
        pattern = re.compile(
            r'^\s*(?:\*\*|\*)?\s*(?P<label>note|attention|important|information|tip|warning)\s*(?::|[-–—])?\s*(?:\*\*|\*)?\s+',
            re.I,
        )
        m = pattern.match(txt)
        if m:
            new_txt = txt[m.end():]
            node.replace_with(NavigableString(new_txt))
            return True
        return False

    for child in list(inner_soup.contents):
        if isinstance(child, NavigableString):
            if try_strip_textnode(child):
                break
            if child.strip():
                break
        else:
            if child.name in {"span", "strong", "b", "em"}:
                text_node = NavigableString(child.get_text())
                if try_strip_textnode(text_node):
                    child.replace_with(text_node)
                    break
                else:
                    break
            elif child.name in {"br"}:
                child.decompose()
                continue
            else:
                break

def _strip_leading_note_title_from_md(md_text: str) -> str:
    patterns = [
        r'^\s*(?:\*\*|\*)\s*(?:Note|Attention|Important|Information|Tip|Warning)\s*(?::|[-–—])\s*(?:\*\*|\*)\s+',
        r'^\s*(?:\*\*|\*)\s*(?:Note|Attention|Important|Information|Tip|Warning)\s*(?:\*\*|\*)\s*(?::|[-–—])\s+',
        r'^\s*(?:Note|Attention|Important|Information|Tip|Warning)\s*(?::|[-–—])\s+',
    ]
    for pat in patterns:
        md_text, n = re.subn(pat, '', md_text, flags=re.I)
        if n:
            break
    return md_text

def transform_admonitions(container: BeautifulSoup) -> None:
    """Turn <div class="note ..."> blocks into Docusaurus ::: fences."""
    CLASS_TO_ADMONITION = {
        "important": "warning",
        "danger": "danger",
        "tip": "tip",
        "information": "info",
    }
    for div in container.find_all("div", class_=True):
        classes = set(div.get("class", []))
        if "note" not in classes:
            continue
        admonition = "note"
        for key, value in CLASS_TO_ADMONITION.items():
            if key in classes:
                admonition = value
                break
        inner_html = "".join(str(child) for child in div.contents)
        inner_soup = BeautifulSoup(inner_html, "html.parser")
        _remove_notetitle_nodes(inner_soup)
        _strip_leading_note_title(inner_soup)

        # NEW: protect <sup> before markdownify, then restore
        sup_map = protect_sup_tags(inner_soup, prefix="ADMSUPPLACEHOLDER")

        inner_md = md.markdownify(str(inner_soup), heading_style="ATX").strip()
        inner_md = _strip_leading_note_title_from_md(inner_md)
        inner_md = unescape_md_in_placeholders(inner_md)
        inner_md = restore_sup_placeholders(inner_md, sup_map)  # NEW

        admonition_block = f"\n:::{admonition}\n{inner_md}\n:::\n"
        div.replace_with(NavigableString(admonition_block))

        
def ignore_material_icons(container: BeautifulSoup) -> None:
    """
    Remove <span class="material-icons ...">...</span> entirely,
    so words like 'assignment' never leak into the Markdown.
    """
    for sp in list(container.find_all("span", class_=True)):
        classes = " ".join(sp.get("class", []))
        if "material-icons" in classes:
            sp.decompose()

def flatten_note_spans(container: BeautifulSoup):
    for sp in list(container.find_all("span")):
        if not sp.attrs:
            sp.unwrap()
            
def strip_paragraphs_in_lists(container: BeautifulSoup) -> None:
    """
    Normalize list markup:
    - For <p class="p"> inside an <li>, UNWRAP the <p> (keep its children like <strong>, <em>, <a>, etc.).
    - For other <p> inside <li> or directly under <ul>/<ol>, unwrap or remove if empty.
    - Also unwrap trivial <div>/<span> wrappers inside <li> that only hold text and no meaningful attributes.
    """
    if not container:
        return

    # Handle all lists
    for lst in list(container.find_all(["ul", "ol"])):
        # 1) Clean stray <p> directly under the list (between <li> siblings)
        for pnode in list(lst.find_all("p", recursive=False)):
            if not pnode.get_text(strip=True):
                pnode.decompose()
            else:
                pnode.unwrap()

        # 2) Clean <p> inside each <li>
        for li in list(lst.find_all("li")):
            for pnode in list(li.find_all("p")):
                if not pnode.get_text(strip=True):
                    pnode.decompose()
                else:
                    if "p" in (pnode.get("class") or []):
                        # Special case: <p class="p"> → unwrap (preserve children like <strong>)
                        pnode.unwrap()
                    else:
                        # Default: unwrap the <p> as well
                        pnode.unwrap()

            # 3) After <p> cleanup, unwrap trivial <div>/<span> wrappers
            for wrapper_name in ("div", "span"):
                for w in list(li.find_all(wrapper_name)):
                    # Leave wrappers that contain nested structures
                    if w.find(["ul", "ol", "table", "pre", "code", "img"]):
                        continue
                    # Unwrap if no meaningful attrs, otherwise leave
                    if not w.attrs or set(w.attrs.keys()).issubset({"class", "id"}):
                        if not w.get_text(strip=True):
                            w.decompose()
                        else:
                            w.unwrap()
 
_PLACEHOLDER_INLINE_RE = re.compile(r"{{[^}]*}}")

def backslash_escape_mdx_specials(container) -> None:
    """
    Escape MDX/Markdown specials in TEXT nodes with backslashes.
    - Skips <code>, <pre> content
    - Keeps '*' intact (bold/lists)
    - Does NOT escape '_' inside links (<a>…)
    - Leaves {{…}} placeholder chunks untouched
    """
    if not container:
        return

    skip_tags = {"code", "pre"}

    def in_tags(node, names):
        p = node.parent
        while p is not None:
            if getattr(p, "name", None) in names:
                return True
            p = getattr(p, "parent", None)
        return False

    def in_anchor(node):
        p = node.parent
        while p is not None:
            if getattr(p, "name", None) == "a":
                return True
            p = getattr(p, "parent", None)
        return False

    for tn in list(container.find_all(string=True)):
        # Touch only real text nodes
        if not isinstance(tn, NavigableString):
            continue
        s = str(tn)
        if not s:
            continue
        # Skip code/pre
        if in_tags(tn, skip_tags):
            continue
        # If this text contains a {{…}} placeholder, leave it as-is
        if _PLACEHOLDER_INLINE_RE.search(s):
            continue

        # Start with backslash itself (so we can detect already-escaped chars)
        s = s.replace("\\", "\\\\")  # \  -> \\

        # Escape angle/curly brackets only when not already escaped
        for ch in ("<", ">", "{", "}"):
            s = re.sub(r"(?<!\\)" + re.escape(ch), "\\" + ch, s)

        # Escape underscore unless we're inside a link (<a>…)
        if not in_anchor(tn):
            s = re.sub(r"(?<!\\)_", r"\_", s)

        # Note: '*' deliberately left alone

        if s != str(tn):
            tn.replace_with(NavigableString(s)) 

def last_path_segment_no_ext(url: str) -> str:
    path = urllib.parse.urlparse(url).path
    segment = path.rstrip('/').split('/')[-1]
    return re.sub(r'\.html?$', '', segment, flags=re.IGNORECASE)

def clean_title(raw_title: str) -> str:
    if not raw_title:
        return raw_title
    if " - " in raw_title:
        return raw_title.split(" - ", 1)[1].strip()
    if ":" in raw_title:
        return raw_title.split(":", 1)[1].strip()
    return raw_title.strip()

def create_folder_structure_from_url(url: str) -> str:
    parsed_url = urllib.parse.urlparse(url)
    path_segments = [segment for segment in parsed_url.path.split('/') if segment]
    if len(path_segments) > 1:
        folder_path = os.path.join(*path_segments[:-1])
    else:
        folder_path = ""
    return folder_path
    
def promote_headings(md_text: str) -> str:
    """
    Promote all ATX headings by one level:
    ### -> ##, #### -> ###, etc.
    Leaves top-level '#' unchanged.
    """
    lines = md_text.splitlines()
    new_lines = []
    for line in lines:
        if line.lstrip().startswith("#"):
            hashes, rest = line.split(" ", 1) if " " in line else (line, "")
            if len(hashes) > 1:  # only promote if it's not '#'
                hashes = hashes[:-1]  # remove one '#' to promote level
            new_lines.append(hashes + (" " + rest if rest else ""))
        else:
            new_lines.append(line)
    return "\n".join(new_lines)


def html_to_markdown_github(url, position_counter=None, crawl=True):
    """Convert page(s) to Markdown with frontmatter and write .mdx files."""
    try:
        parsed_url = urllib.parse.urlparse(url)
        base_url = (
            parsed_url.scheme
            + "://"
            + parsed_url.netloc
            + parsed_url.path.rsplit("/", 1)[0]
            + "/"
        )

        folder_structure = create_folder_structure_from_url(url)
        output_folder = os.path.join(os.getcwd(), folder_structure)
        os.makedirs(output_folder, exist_ok=True)

        visited_urls = set()
        queue = [url]
        session = requests.Session()
        skipped_urls = []
        while queue:
            current_url = queue.pop(0)
            if current_url in visited_urls:
                continue
            visited_urls.add(current_url)

            try:
                response = get_with_retries(current_url, session=session)
                soup = BeautifulSoup(response.content, "html.parser")

                doc_container = soup.find("div", id="DocContainer")
                if doc_container:
                    for anchor in doc_container.find_all("a", href=re.compile("^#")):
                        anchor.decompose()
                    remove_empty_tags(doc_container)
                    flatten_note_spans(doc_container)
                    # replace_ph_spans_with_placeholders(doc_container, PH_PLACEHOLDER_MAP)
                    backslash_escape_mdx_specials(doc_container)
                    
                    transform_availability_images(doc_container)
                    
                    table_html_map = extract_complex_tables(doc_container)
                    strip_paragraphs_in_lists(doc_container)
                    
                    sup_map_global = protect_sup_tags(doc_container)
                    
                    transform_admonitions(doc_container)
                    ignore_material_icons(doc_container)

                    markdown_content = md.markdownify(str(doc_container), heading_style="ATX")
                    markdown_content = cleanup_markdown(markdown_content)
                    markdown_content = unescape_md_in_placeholders(markdown_content)
                    # 🚨 Remove the first h2 heading
                    markdown_content = remove_leading_h2(markdown_content)
                    
                    # 🚨 Promote all headings (h3 -> h2, etc.)
                    markdown_content = promote_headings(markdown_content)

                    for placeholder, table_html in table_html_map.items():
                        markdown_content = markdown_content.replace(placeholder, table_html)
                    
                    markdown_content = restore_sup_placeholders(markdown_content, sup_map_global)


                    slug = last_path_segment_no_ext(current_url)
                    page_folder_structure = create_folder_structure_from_url(current_url)
                    page_output_folder = os.path.join(os.getcwd(), page_folder_structure)
                    os.makedirs(page_output_folder, exist_ok=True)

                    file_name = f"{slug}.mdx"
                    output_path = os.path.join(page_output_folder, file_name)

                    title_tag = soup.find("title")
                    if title_tag and title_tag.string and title_tag.string.strip():
                        title = clean_title(title_tag.string.strip())
                    else:
                        title = slug.replace("-", " ").strip().title()

                    frontmatter = (
                        f"---\n"
                        f"title: {title}\n"
                        f"visible: true\n"
                        f"slug: {slug}\n"
                        f"---\n\n"
                    )
                    full_markdown_content = frontmatter + markdown_content
                    full_markdown_content = prefix_relative_markdown_links(
                        full_markdown_content, domain="https://docs.uipath.com"
                    )

                    with open(output_path, "w", encoding="utf-8") as f:
                        f.write(full_markdown_content)
                    print(f"📝 Saved MDX: {output_path}")

                    if crawl:
                        for link in soup.find_all("a", href=True):
                            href = link["href"]
                            if href.startswith(base_url) and href not in visited_urls and not href.startswith("#"):
                                queue.append(href)
                            elif (
                                not urllib.parse.urlparse(href).netloc
                                and href.startswith("/")
                                and base_url.startswith(parsed_url.scheme + "://" + parsed_url.netloc)
                                and not href.startswith("#")
                            ):
                                absolute_url = urllib.parse.urljoin(
                                    parsed_url.scheme + "://" + parsed_url.netloc, href
                                )
                                if absolute_url.startswith(base_url) and absolute_url not in visited_urls:
                                    queue.append(absolute_url)
                            elif (
                                not urllib.parse.urlparse(href).netloc
                                and not href.startswith("#")
                                and not href.startswith("mailto:")
                                and base_url in current_url
                                and href.endswith(".html")
                            ):
                                absolute_url = urllib.parse.urljoin(current_url, href)
                                if absolute_url.startswith(base_url) and absolute_url not in visited_urls:
                                    queue.append(absolute_url)
                else:
                    print(f"⚠️  DocContainer not found: {current_url}")

            except requests.exceptions.RequestException as e:
                print(f"Error fetching URL '{current_url}': {e}")
                skipped_urls.append((current_url, str(e)))
            except Exception as e:
                print(f"An error occurred while processing '{current_url}': {e}")

        # After crawling, write skipped URLs (if any) to a timestamped log
        if skipped_urls:
            ts = datetime.now().strftime("%Y%m%d-%H%M%S")
            log_path = os.path.join(os.getcwd(), f"skipped_urls_{ts}.log")
            with open(log_path, "w", encoding="utf-8") as lf:
                lf.write("# Skipped URLs (fetch errors)\n")
                for u, err in skipped_urls:
                    lf.write(f"{u}\t{err}\n")
            print(f"🗒️  Skipped URLs logged to: {log_path}")

    except Exception as e:
        print(f"An error occurred: {e}")

# ===============================
# === SIDEBAR/metadata HELPERS ===
# ===============================

HREF_MIN_DEPTH = 2  # add hrefs starting from this depth (relative to wrapper)
_SLUG_SAFE = re.compile(r"[^a-z0-9\-]+")
ICON_CLASS_HINT = re.compile(r"(icon|chevron|toggle|caret|expand)", re.I)

BANNED_TAGS = {"style", "script", "noscript", "link", "meta", "button", "svg", "path"}

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

def _segments(url: str) -> List[str]:
    parsed = urllib.parse.urlparse(url)
    return [urllib.parse.unquote(s) for s in (parsed.path or "").split("/") if s]

def _titleify(slug: str) -> str:
    s = re.sub(r"[-_]+", " ", slug or "").strip()
    return s.title()

def derive_guide_name_from_slug(url: str) -> str:
    segs = _segments(url)
    product_slug = segs[0].lower() if len(segs) >= 1 else ""
    guide_type_slug = segs[-2].lower() if len(segs) >= 2 else (segs[-1].lower() if segs else "")
    product = _titleify(product_slug) if product_slug else "Guide"
    guide_type = re.sub(r"[-_]+", " ", guide_type_slug).strip().lower()
    title = f"{product} {guide_type}".strip()
    return title

def derive_metadata_from_url(url: str) -> Dict[str, str]:
    segs = _segments(url)
    product_slug = segs[0].lower() if len(segs) >= 1 else ""
    delivery_slug = segs[1].lower() if len(segs) >= 2 else ""
    release = segs[2] if len(segs) >= 3 else ""
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

def slugify(text: str) -> str:
    s = urllib.parse.unquote((text or "").lower().strip())
    s = s.replace("&", " and ")
    s = re.sub(r"[^\w\s\-]+", "", s)
    s = re.sub(r"\s+", "-", s)
    s = _SLUG_SAFE.sub("", s)
    s = re.sub(r"-{2,}", "-", s).strip("-")
    return s or "item"

def filename_stem_from_url(url: str) -> str:
    segs = _segments(url)
    candidate = segs[-2] if len(segs) >= 2 else (segs[-1] if segs else "output")
    return slugify(candidate)

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
    abs_url = urllib.parse.urljoin(base_url, href)
    parsed = urllib.parse.urlparse(abs_url)
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
    s = slugify(title)
    return posixpath.join(parent_dir if parent_dir else "/", s + ".mdx")

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

def href_from_li(li: Tag, base_url: str) -> Optional[str]:
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
    if depth >= HREF_MIN_DEPTH:
        if mdx_path:
            item["href"] = mdx_path
        else:
            base_dir = parent_dir or page_dir or "/"
            item["href"] = derive_child_path_from_parent_dir(title, base_dir)
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

def build_sidebar_from_url(url: str) -> Dict:
    headers = {"User-Agent": "SidebarScraper/1.5 (+https://example.local)"}
    resp = requests.get(url, headers=headers, timeout=30)
    resp.raise_for_status()
    soup = BeautifulSoup(resp.text, "html.parser")
    for tname in list(BANNED_TAGS):
        for t in soup.find_all(tname):
            t.decompose()
    root = pick_sidebar_root(soup)
    if not root:
        raise RuntimeError("Could not locate a sidebar <ul> in this page.")
    guide_title = derive_guide_name_from_slug(url)
    page_dir = path_dirname(urllib.parse.urlparse(url).path or "/")
    children = ul_to_items(root, base_url=url, depth=1, parent_dir=page_dir, page_dir=page_dir)
    return {"title": guide_title, "children": children}

def version_folder_from_url(url: str) -> str:
    """Return local folder path '<product>/<delivery>/<version>' from a docs.uipath.com URL."""
    segs = _segments(url)
    if len(segs) >= 3:
        return os.path.join(segs[0], segs[1], segs[2])
    # fallback: just use as many as we have
    return os.path.join(*segs[:3]) if segs else "."

def write_sidebar_and_metadata(url: str) -> None:
    sidebar_rooted = build_sidebar_from_url(url)
    stem = filename_stem_from_url(url)  # second-to-last URL segment
    metadata = derive_metadata_from_url(url)

    # Ensure destination dir: <product>/<delivery>/<version>
    dest_dir = os.path.join(os.getcwd(), version_folder_from_url(url))
    os.makedirs(dest_dir, exist_ok=True)

    sidebar_path = os.path.join(dest_dir, f"{stem}-sidebar.json")
    metadata_path = os.path.join(dest_dir, f"{stem}-metadata.json")

    with open(sidebar_path, "w", encoding="utf-8") as f:
        json.dump(sidebar_rooted, f, ensure_ascii=False, indent=2)
    with open(metadata_path, "w", encoding="utf-8") as f:
        json.dump(metadata, f, ensure_ascii=False, indent=2)

    print(f"📚 Wrote {sidebar_path}")
    print(f"📄 Wrote {metadata_path}")
    print(f"ℹ️ Filenames are based on the second-to-last URL segment: '{stem}'")
    print(f"ℹ️ Hrefs are included for items at depth ≥ {HREF_MIN_DEPTH}.")

# ============
# === CLI  ===
# ============

if __name__ == "__main__":
    position_tracking = {}
    while True:
        target_url = input("Enter the URL of the starting HTML page (or press Enter to quit): ").strip()
        if not target_url:
            print("No URL entered. Exiting.")
            break

        # ===========================
        # TOGGLE ONE OF THESE CALLS:
        # ===========================

        # Single-page mode (no crawling):
        html_to_markdown_github(target_url, position_tracking, crawl=False)

        # Crawl mode (follow in-site links):
        # html_to_markdown_github(target_url, position_tracking, crawl=True)

        print(f"✅ Conversion completed for: {target_url}")

        # 2) Build sidebar + metadata JSON files for the same URL, saved under <product>/<delivery>/<version>
        try:
            write_sidebar_and_metadata(target_url)
        except Exception as e:
            print(f"❌ Sidebar/metadata generation failed: {e}")

        print("-" * 72)
        
        
