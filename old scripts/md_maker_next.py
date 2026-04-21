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
import html
import re
import time
import random
import json
import posixpath
import urllib.parse
import email.utils
import argparse
from datetime import datetime, timezone
from typing import List, Dict, Optional


import requests

# Track whether we've already prompted for docs-dev login in this run
_DOCS_DEV_PROMPTED = False
GLOBAL_SESSION: requests.Session | None = None

from bs4 import BeautifulSoup, NavigableString, Tag
import markdownify as md

# ==============================
# === docs-dev SSO helpers  ====

DOCS_DEV_HOSTS = {"docs-dev.uipath.com", "preview-docs.uipath.com"}


def _detect_kid_from_cloudflare(target_url: str, session: requests.Session) -> str | None:
    """
    Try to discover the Cloudflare Access KID automatically.
    Strategy:
      1) Hit the app-host login endpoint (docs-dev) with a redirect to the target URL,
         but DO NOT follow redirects. Cloudflare typically bounces to the team login
         and includes `kid=...` in the Location query.
      2) If not found, try the team endpoint without kid and inspect Location/HTML.
    Returns the detected KID (str) or None.
    """
    try:
        # Build app-host login first
        app_login = "https://docs-dev.uipath.com/cdn-cgi/access/login?" + urllib.parse.urlencode({"redirect_url": target_url})
        r = session.get(app_login, allow_redirects=False, timeout=10)
        # Check immediate redirect
        loc = r.headers.get("Location", "") or r.headers.get("location", "")
        if loc:
            # Parse kid from query if present
            try:
                parsed = urllib.parse.urlparse(loc)
                qs = urllib.parse.parse_qs(parsed.query)
                kid_vals = qs.get("kid") or []
                if kid_vals:
                    return kid_vals[0]
            except Exception:
                pass
        # If not, try following one hop
        if r.is_redirect or r.status_code in (301, 302, 303, 307, 308):
            try:
                r2 = session.get(urllib.parse.urljoin(app_login, loc), allow_redirects=False, timeout=10)
                loc2 = r2.headers.get("Location", "") or r2.headers.get("location", "")
                if loc2:
                    parsed2 = urllib.parse.urlparse(loc2)
                    qs2 = urllib.parse.parse_qs(parsed2.query)
                    kid_vals2 = qs2.get("kid") or []
                    if kid_vals2:
                        return kid_vals2[0]
            except Exception:
                pass
    except Exception:
        pass

    # Try team endpoint without kid
    try:
        team_login_no_kid = CLOUDFLARE_LOGIN_BASE + "?" + urllib.parse.urlencode({"redirect_url": target_url})
        r3 = session.get(team_login_no_kid, allow_redirects=False, timeout=10)
        loc3 = r3.headers.get("Location", "") or r3.headers.get("location", "")
        if loc3:
            parsed3 = urllib.parse.urlparse(loc3)
            qs3 = urllib.parse.parse_qs(parsed3.query)
            kv = qs3.get("kid") or []
            if kv:
                return kv[0]
    except Exception:
        pass

    return None

import webbrowser
import urllib.parse
import time
import getpass

CLOUDFLARE_LOGIN_BASE = "https://uipath.cloudflareaccess.com/cdn-cgi/access/login"


def _build_cf_login_url(redirect_path: str) -> str:
    """
    Build Cloudflare Access login URL(s) for docs-dev with optional KID.
    Returns the team login endpoint by default; prompt_for_docs_dev_login will
    also try the app-host login and the direct target URL.
    """
    kid = os.getenv("CLOUDFLARE_KID")
    # redirect_path may actually be a full URL; if it's just a path, prefix docs-dev host
    if redirect_path.startswith("http"):
        target = redirect_path
    else:
        target = "https://docs-dev.uipath.com" + (redirect_path if redirect_path.startswith("/") else ("/" + redirect_path))
    params = {"redirect_url": target}
    if kid:
        params["kid"] = kid
    team_login = CLOUDFLARE_LOGIN_BASE + "?" + urllib.parse.urlencode(params)
    return team_login




def _try_playwright_login(target_url: str, session: requests.Session) -> bool:
    """
    Attempt to complete SSO using a real browser via Playwright and import cookies
    into the provided requests session. Returns True if cookies for docs-dev were
    captured and set; False otherwise. Requires `pip install playwright` and
    `playwright install chromium` on first use.
    """
    try:
        # Lazy import so users without Playwright can still run the script.
        from playwright.sync_api import sync_playwright
    except Exception as e:
        # Playwright not installed or import failed
        print("Playwright not available:", e)
        return False

    try:
        with sync_playwright() as p:
            # Use a visible browser so the user can complete SSO comfortably.
            browser = p.chromium.launch(headless=False)
            context = browser.new_context()
            page = context.new_page()

            # Start at the target URL (or Cloudflare login will redirect there)
            page.goto(target_url)

            print("\nA browser window has opened to complete SSO.")
            print("1) Use the email login and write your uipath email, then click Send code.")
            print("2) Wait to receive the login code from [EXTERNAL] Cloudflare Access login code for docs-dev.uipath.com.")
            print("3) Paste the code in the login window.")
            print("4) Make sure you land on the docs-dev content.")
            input("Press ENTER here after you finish SSO in the browser... ")

            # Collect cookies and filter to docs-dev.uipath.com
            cookies = context.cookies()
            got_any = False
            for c in cookies:
                domain = c.get("domain") or ""
                if "docs-dev.uipath.com" in domain:
                    session.cookies.set(c["name"], c["value"], domain="docs-dev.uipath.com")
                    got_any = True

            try:
                browser.close()
            except Exception:
                pass

            if got_any:
                print("Imported authenticated cookies from Playwright into this session.")
            else:
                print("Didn't detect docs-dev cookies from Playwright session.")
            return got_any
    except Exception as e:
        print("Playwright flow failed:", e)
        return False

def prompt_for_docs_dev_login(target_url: str, session: requests.Session):
    global _DOCS_DEV_PROMPTED
    _DOCS_DEV_PROMPTED = True
    """
    Send the user to Cloudflare Access login for docs-dev, ask them to choose Azure AD,
    and wait until they finish SSO in the browser. Then we try the target URL again.
    If access still fails, we ask the user to paste cookies from the browser.
    """
    parsed = urllib.parse.urlparse(target_url)
    if not parsed.netloc:
        return
    full_url = urllib.parse.urlunparse(parsed._replace())
    print("\nOpening Cloudflare Access login in your browser...")
    print("1) Use the email login and write your uipath email, then click Send code.")
    print("2) Wait to receive the login code from [EXTERNAL] Cloudflare Access login code for docs-dev.uipath.com.")
    print("3) Paste the code in the login window.")
    print("4) Make sure you land on the docs-dev content.")
    print("Press ENTER here after you finish SSO in the browser... ")

    # Auto-detect KID
    detected_kid = None
    try:
        detected_kid = _detect_kid_from_cloudflare(full_url, session=session)
        if detected_kid:
            print(f"[info] Detected Cloudflare Access KID: {detected_kid[:8]}…")
    except Exception:
        pass

    # Build candidates
    params = {"redirect_url": full_url}
    if detected_kid:
        params["kid"] = detected_kid
    team_login = CLOUDFLARE_LOGIN_BASE + "?" + urllib.parse.urlencode(params)
    app_login = "https://docs-dev.uipath.com/cdn-cgi/access/login?" + urllib.parse.urlencode({"redirect_url": full_url})

    # First, try Playwright to harvest authenticated cookies without env vars
    if _try_playwright_login(full_url, session):
        return
    opened_any = False
    for candidate in (team_login, app_login, full_url):
        try:
            webbrowser.open(candidate, new=2, autoraise=True)
            opened_any = True
        except Exception:
            pass
    if not opened_any:
        print("If the browser didn't open, try any of these manually:")
        print(f"- Team login: {team_login}")
        print(f"- App login:  {app_login}")
        print(f"- Direct:     {full_url}")
    input("Press ENTER after you finish signing in... ")
    time.sleep(1.2)

    # Try to fetch again using our session
    try:
        resp = sso_get_with_retries(target_url, session=session, max_tries=2, base_sleep=0.4)
        if resp.status_code == 200 and not looks_like_login_wall(resp.text):
            return
    except Exception:
        pass

    # If we're still blocked, ask the user to paste cookies from the logged-in browser.
    print("\nIt looks like we still can't access the page programmatically.")
    print("Please copy cookies from your browser's DevTools (Application → Cookies → docs-dev.uipath.com).")
    print("You can paste the full 'Cookie' header value (e.g., 'CloudFront-Key-Pair-Id=...; CloudFront-Policy=...; CloudFront-Signature=...')")
    try:
        import getpass
        cookie_str = getpass.getpass("Paste cookies here (input hidden): ")
    except Exception:
        cookie_str = input("Paste cookies here: ")
    if cookie_str.strip():
        cookies = _parse_cookie_string(cookie_str)
        for k, v in cookies.items():
            session.cookies.set(k, v, domain="docs-dev.uipath.com")

        return

    else:
        print("No cookies pasted; continuing without additional cookies.")
        # Use FULL target URL for redirects
        full_url = urllib.parse.urlunparse(parsed._replace())
        print("\nOpening Cloudflare Access login in your browser...")
        print("1) In the browser, choose 'Azure AD' and complete SSO.")
        print("2) You'll be redirected back to the docs-dev page.")
        print("3) Return here and press ENTER to continue.\n")
        # Build candidates: team login (with optional kid), app-host login, and direct
        team_login = _build_cf_login_url(full_url)
        app_login = "https://docs-dev.uipath.com/cdn-cgi/access/login?" + urllib.parse.urlencode({"redirect_url": full_url})
        opened_any = False
    for candidate in (team_login, app_login, full_url):
        try:
            webbrowser.open(candidate, new=2, autoraise=True)
            opened_any = True
        except Exception:
            pass
    if not opened_any:
        print("If the browser didn't open, try any of these manually:")
        print(f"- Team login: {team_login}")
        print(f"- App login:  {app_login}")
        print(f"- Direct:     {full_url}")
    input("Press ENTER after you finish signing in... ")
    time.sleep(1.2)

def _parse_cookie_string(cookie_string: str):
    """Parse a simple "k1=v1; k2=v2" cookie string into a dict."""
    jar = {}
    if not cookie_string:
        return jar
    # Split on semicolons not inside quotes
    parts = [p.strip() for p in cookie_string.split(";") if p.strip()]
    for part in parts:
        if "=" in part:
            k, v = part.split("=", 1)
            jar[k.strip()] = v.strip()
    return jar

def _is_docs_dev_url(url: str) -> bool:
    try:
        netloc = urllib.parse.urlparse(url).netloc.lower()
    except Exception:
        return False
    return any(netloc.endswith(h) for h in DOCS_DEV_HOSTS)

def configure_docs_dev_auth(session: requests.Session):
    """
    Best-effort auth bootstrap for SSO-protected docs-dev pages.
    Looks for env vars:
      - DOCS_DEV_BEARER: a JWT or opaque token -> Authorization: Bearer <token>
      - DOCS_DEV_COOKIES: raw cookie string "k1=v1; k2=v2" (e.g., .ASPXAUTH, session)
      - CLOUDFRONT_COOKIES: signed cookies string (Key-Pair-Id, Policy, Signature)
    You can provide any or all; they will be merged into the session.
    """
    token = os.getenv("DOCS_DEV_BEARER")
    if token and "authorization" not in {k.lower() for k in session.headers}:
        session.headers["Authorization"] = f"Bearer {token}"
    raw = os.getenv("DOCS_DEV_COOKIES") or ""
    cf  = os.getenv("CLOUDFRONT_COOKIES") or ""
    cookies = {}
    cookies.update(_parse_cookie_string(raw))
    cookies.update(_parse_cookie_string(cf))
    for k, v in cookies.items():
        session.cookies.set(k, v, domain="docs-dev.uipath.com")
    # Be explicit about a UA; some edges block generic ones
    if "User-Agent" not in session.headers:
        session.headers["User-Agent"] = DEFAULT_USER_AGENT
    # Helpful for some proxies
    session.headers.setdefault("Accept", "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8")
    session.headers.setdefault("Accept-Language", "en-US,en;q=0.9")

def sso_get_with_retries(url, session=None, max_tries=5, base_sleep=1.0, timeout=20, **kwargs):
    """
    Wrapper around get_with_retries that detects SSO walls on docs-dev and
    attempts to (lazily) configure auth from environment variables.
    """
    s = session or requests.Session()
    # If targeting docs-dev, pre-configure once
    if _is_docs_dev_url(url):
        configure_docs_dev_auth(s)
    try:
        return get_with_retries(url, session=s, max_tries=max_tries, base_sleep=base_sleep, timeout=timeout)
    except requests.exceptions.HTTPError as e:
        status = getattr(e.response, "status_code", None)
        # If unauthorized/forbidden, try one more time after configuring auth
        if _is_docs_dev_url(url) and status in (401, 403):
            configure_docs_dev_auth(s)
            return get_with_retries(url, session=s, max_tries=max_tries, base_sleep=base_sleep, timeout=timeout)
        raise

def looks_like_login_wall(html: str) -> bool:
    """
    Lightweight detection for an SSO/login page. This is a heuristic.
    """
    if not html:
        return False
    text = html.lower()
    # Common cues without binding to a specific IdP
    cues = [
        "sign in", "log in", "login", "single sign-on", "sso",
        "continue with", "enter your email", "verify your identity"
    ]
    # Avoid false positives on real docs by checking absence of DocContainer
    if 'id="DocContainer"' in text or "id='DocContainer'" in text:
        return False
    return any(cue in text for cue in cues)

def safe_get_html(url: str, session: requests.Session, **kw) -> requests.Response:
    """
    Fetches URL with SSO/backoff handling.
    If the HTML looks like a login wall and the host is docs-dev, we try auth once and refetch;
    if that fails, we open the Cloudflare Access login and wait for the user to finish SSO.
    """
    s = session
    resp = sso_get_with_retries(url, session=s, **kw)
    ct = resp.headers.get("Content-Type", "")
    looks_html = "html" in ct or ct == ""
    if looks_html and _is_docs_dev_url(url) and looks_like_login_wall(resp.text):
        # Attempt to upgrade auth and refetch once
        configure_docs_dev_auth(session)
        resp = sso_get_with_retries(url, session=session, **kw)
        ct2 = resp.headers.get("Content-Type", "")
        if ("html" in ct2 or ct2 == "") and looks_like_login_wall(resp.text):
            # Launch interactive login flow in the user's browser and wait
            try:
                # Only prompt once per run
                global _DOCS_DEV_PROMPTED
                if not _DOCS_DEV_PROMPTED:
                    prompt_for_docs_dev_login(url, session=session)
                    resp = sso_get_with_retries(url, session=session, **kw)
                else:
                    # Already prompted earlier; skip re-prompt to avoid nagging
                    pass
            except Exception:
                pass
    return resp


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

# --- Table helpers: detect complexity & convert images in simple tables ---

def _is_complex_table(table: Tag) -> bool:
    """Match the same rules used for 'complex' table extraction."""
    has_list = table.find(["ul", "ol", "li"]) is not None
    has_note = table.find("div", class_=lambda c: c and "note" in c.split()) is not None
    has_rowspan = any(cell.has_attr("rowspan") for cell in table.find_all(["td", "th"]))
    has_colspan = any(cell.has_attr("colspan") for cell in table.find_all(["td", "th"]))
    return has_list or has_note or has_rowspan or has_colspan


def transform_images_in_simple_tables_to_markdown(container: BeautifulSoup) -> None:
    """
    For tables that are NOT 'complex', replace <img> tags in cells with Markdown images.
    This ensures images are preserved/identified inside Markdown tables.
    """
    for table in list(container.find_all("table")):
        if _is_complex_table(table):
            continue  # complex tables handled elsewhere (HTML placeholders)
        for img in list(table.find_all("img")):
            alt = (img.get("alt") or "").strip()
            src = (img.get("src") or "").strip()
            if not src:
                # keep a minimal marker if src missing
                replacement = NavigableString(f"[image]{f'({alt})' if alt else ''}")
            else:
                # escape pipe in alt to avoid breaking Markdown tables
                safe_alt = alt.replace("|", r"\|")
                replacement = NavigableString(f"![{safe_alt}]({src})")
            img.replace_with(replacement)


def convert_html_imgs_in_md_tables(markdown_text: str) -> str:
    """
    Safety net: if any <img ...> leaked into Markdown tables, convert them to ![alt](src).
    We only touch lines that look like Markdown table rows (start with '|').
    """
    def _img_to_md(html_img: str) -> str:
        # very small attribute sniffer; robust enough for our controlled output
        alt = ""
        src = ""
        # alt
        m = re.search(r'alt="([^"]*)"', html_img, flags=re.IGNORECASE)
        if m: alt = m.group(1)
        # src
        m = re.search(r'src="([^"]+)"', html_img, flags=re.IGNORECASE)
        if m: src = m.group(1)
        if src:
            return f"![{alt.replace('|', r'\\|')}]({src})"
        return f"[image]{f'({alt})' if alt else ''}"

    def _convert_line(line: str) -> str:
        # only process likely table rows to avoid messing with normal paragraphs
        if not line.strip().startswith("|"):
            return line
        return re.sub(r"<img\b[^>]*>", lambda m: _img_to_md(m.group(0)), line, flags=re.IGNORECASE)

    return "\n".join(_convert_line(ln) for ln in markdown_text.splitlines())


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
    
def normalize_paragraphs(container: BeautifulSoup) -> None:
    # Remove <br> nodes entirely
    for br in list(container.find_all("br")):
        br.decompose()

    # Normalize <p> blocks that aren't complex containers
    for p in list(container.find_all("p")):
        if _in_itemgroup_info(p):
            continue
        if p.find(["pre", "code", "table", "ul", "ol"]) is not None:
            continue

        # 1) Collapse whitespace ONLY inside text nodes (keep <a>, <sup>, etc.)
        for node in list(p.descendants):
            if isinstance(node, NavigableString):
                # Turn &nbsp; into regular spaces first
                s = str(node).replace("\xa0", " ")
                # Collapse runs of whitespace/newlines/tabs into a single space
                s = re.sub(r"\s+", " ", s)
                node.replace_with(s)

        # 2) Clean spacing around punctuation without touching tag structure
        #    Convert the <p> to HTML string, fix spacing, reparse back into the same place.
        html = str(p)

        # Remove spaces *before* common punctuation
        html = re.sub(r"\s+([,.;:!?])", r"\1", html)
        # Remove spaces just inside closing parens/brackets
        html = re.sub(r"\s+(\))", r"\1", html)
        # Remove spaces just after opening parens/brackets
        html = re.sub(r"(\()\s+", r"\1", html)

        # Ensure single spaces between words/tags (avoid leading/trailing space)
        html = re.sub(r">\s+<", "> <", html)            # normalize inter-tag spaces
        html = re.sub(r"\s{2,}", " ", html).strip()     # collapse doubles

        p.replace_with(BeautifulSoup(html, "html.parser"))

    
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
    
BARE_AUTOLINK_RE = re.compile(r"<(https?://[^>\s]+)>")

def unwrap_bare_autolinks(md_text: str) -> str:
    """
    Turn Markdown autolinks like <https://example.com> into bare links:
    https://example.com

    Only matches http/https URLs, so real HTML tags like <img ...> are untouched.
    """
    return BARE_AUTOLINK_RE.sub(r"\1", md_text)


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
    
def _absorb_following_into_note_if_empty(div: Tag) -> None:
    """
    If a <div class="note"> is empty (e.g., only a 'Note:' label wrapper remains),
    pull adjacent text/inline siblings that follow it back inside.
    """
    def is_inlineish(tag: Tag) -> bool:
        return tag.name in {"span", "a", "strong", "em", "code", "kbd", "sup", "sub", "b", "i"}

    if div.get_text(strip=True):
        return

    for sib in list(div.next_siblings):
        # Stop at clear block boundaries
        if isinstance(sib, Tag) and sib.name == "div" and "note" in (sib.get("class") or []):
            break
        if isinstance(sib, Tag) and sib.name in {"ul", "ol", "table", "pre", "blockquote", "hr"}:
            break

        if isinstance(sib, NavigableString):
            if str(sib).strip():
                p = div.new_tag("p"); p.string = str(sib); div.append(p)
            sib.extract()
            continue

        if isinstance(sib, Tag) and (is_inlineish(sib) or sib.name in {"p"}):
            div.append(sib.extract())
            continue

        break
   

def transform_admonitions(container: BeautifulSoup) -> None:
    """Turn <div class="note ..."> blocks into Docusaurus ::: fences."""
    CLASS_TO_ADMONITION = {
        "important": "important",
        "warning": "warning", 
        "danger": "warning",
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

        # NEW: if empty, pull trailing content (like 'Note: ...' text) inside first
        _absorb_following_into_note_if_empty(div)

        inner_html = "".join(str(child) for child in div.contents)
        inner_soup = BeautifulSoup(inner_html, "html.parser")

        # Your existing cleanup already removes <span class="notetitle"> and strips leading 'Note:'
        _remove_notetitle_nodes(inner_soup)                 # already in your file :contentReference[oaicite:2]{index=2}
        _strip_leading_note_title(inner_soup)               # already in your file :contentReference[oaicite:3]{index=3}

        sup_map = protect_sup_tags(inner_soup, prefix="ADMSUPPLACEHOLDER")
        inner_md = md.markdownify(str(inner_soup), heading_style="ATX").strip()
        inner_md = _strip_leading_note_title_from_md(inner_md)  # also in your file :contentReference[oaicite:4]{index=4}
        inner_md = unescape_md_in_placeholders(inner_md)
        inner_md = restore_sup_placeholders(inner_md, sup_map)

        # Build fences
        inner_md = _dedent_admonition_content(inner_md)
        block = f":::{admonition}\n{inner_md}\n:::"

        # NEW: if this note is inside a list item, indent 4 spaces so it nests under that bullet
        if div.find_parent("li") is not None:
            admonition_block = block
        else:
            admonition_block = f"\n{block}"

        div.replace_with(NavigableString(admonition_block))


_PLACEHOLDER_INLINE_RE = re.compile(r"{{[^}]*}}")


def escape_angle_brackets_plain_text(container: BeautifulSoup) -> None:
    """
    HTML stage: escape '<' and '>' in *text nodes only*.
    Skips text inside <code>, <pre>, <script>, <style>.
    Does not alter real HTML tags—only the text content.
    """
    if not container:
        return

    SKIP = {"code", "pre", "script", "style"}

    def inside_forbidden(node: NavigableString) -> bool:
        p = node.parent
        while isinstance(p, Tag):
            if p.name in SKIP:
                return True
            p = p.parent
        return False

    for tn in list(container.find_all(string=True)):
        if not isinstance(tn, NavigableString):
            continue
        if not tn.strip():
            continue
        if inside_forbidden(tn):
            continue
        s = str(tn)
        s2 = s.replace("<", "&lt;").replace(">", "&gt;")
        if s2 != s:
            tn.replace_with(NavigableString(s2))


# def backslash_escape_mdx_specials(container) -> None:
    # """
    # Escape MDX/Markdown specials in TEXT nodes with backslashes.
    # - Skips <code>, <pre> content
    # - Keeps '*' intact (bold/lists)
    # - Does NOT escape '_' inside links (<a>…)
    # - Leaves {{…}} placeholder chunks untouched
    # """
    # if not container:
        # return

    # skip_tags = {"code", "pre"}

    # def in_tags(node, names):
        # p = node.parent
        # while p is not None:
            # if getattr(p, "name", None) in names:
                # return True
            # p = getattr(p, "parent", None)
        # return False

    # def in_anchor(node):
        # p = node.parent
        # while p is not None:
            # if getattr(p, "name", None) == "a":
                # return True
            # p = getattr(p, "parent", None)
        # return False

    # for tn in list(container.find_all(string=True)):
        # # Touch only real text nodes
        # if not isinstance(tn, NavigableString):
            # continue
        # s = str(tn)
        # if not s:
            # continue
        # # Skip code/pre
        # if in_tags(tn, skip_tags):
            # continue
        # # If this text contains a {{…}} placeholder, leave it as-is
        # if _PLACEHOLDER_INLINE_RE.search(s):
            # continue

        # # Start with backslash itself (so we can detect already-escaped chars)
        # s = s.replace("\\", "\\\\")  # \  -> \\

        # # Escape angle/curly brackets only when not already escaped
        # for ch in ("<", ">", "{", "}"):
            # s = re.sub(r"(?<!\\)" + re.escape(ch), "\\" + ch, s)

        # # Escape underscore unless we're inside a link (<a>…)
        # if not in_anchor(tn):
            # s = re.sub(r"(?<!\\)_", r"\_", s)

        # # Note: '*' deliberately left alone

        # if s != str(tn):
            # tn.replace_with(NavigableString(s))           


        
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
            
def unwrap_markdown_paragraphs_and_lists(md_text: str) -> str:
    lines = md_text.splitlines()
    new_lines = []
    buffer = []
    inside_codeblock = False
    inside_table = False
    inside_admonition = False  # <<< NEW

    list_prefix = re.compile(r'^(\s*)([-*+]|\d+\.)\s+')
    table_line = re.compile(r'^\s*\|')
    table_divider = re.compile(r'^\s*[:\-| ]+$')

    code_fence_re = re.compile(r'^\s*(```|~~~)')
    fence_open_re = re.compile(r'^\s*:::\w+\s*$')   # <<< NEW
    fence_close_re = re.compile(r'^\s*:::\s*$')     # <<< NEW
    
    # <<< NEW: treat these as block HTML starters
    html_block_re = re.compile(
        r'^\s*<(?:p|div|ol|ul|table|pre|blockquote|h[1-6]|details|summary)\b', re.I
    )
    html_close_re = re.compile(r'^\s*</(?:p|div|ol|ul|table|pre|blockquote|details)\s*>', re.I)    

    def flush_buffer():
        if not buffer:
            return
        indent = ""
        m = list_prefix.match(buffer[0])
        if m:
            indent = m.group(1)
        # IMPORTANT: we used to strip() each line, which kills alignment.
        # Keep original intra-line leading spaces; only trim right and collapse internal runs.
        merged = " ".join(line.rstrip() for line in buffer).strip()
        merged = re.sub(r"\s{2,}", " ", merged)
        new_lines.append(indent + merged)
        buffer.clear()

    for line in lines:
        stripped = line.strip()

        # Code fences: pass through
        if code_fence_re.match(line):
            flush_buffer()
            new_lines.append(line)
            inside_codeblock = not inside_codeblock
            continue

        if inside_codeblock:
            new_lines.append(line)
            continue

        # Admonition fences: pass through unchanged like code blocks  <<< NEW
        if fence_open_re.match(line):
            flush_buffer()
            inside_admonition = True
            new_lines.append(line)
            continue

        if inside_admonition:
            new_lines.append(line)
            if fence_close_re.match(line):
                inside_admonition = False
            continue

        # Blank line handling
        if not stripped:
            flush_buffer()
            inside_table = False
            new_lines.append("")
            continue

        # Headings/admonition open/close lines
        if stripped.startswith("#"):
            flush_buffer()
            inside_table = False
            # ✅ Flush-left all headings (##, ###, etc.)
            new_lines.append(stripped)
            continue

        if stripped.startswith(":::"):
            flush_buffer()
            inside_table = False
            # 🔁 Keep original indent for ::: fences
            new_lines.append(line)
            continue


        # Table detection
        if table_line.match(line) or (inside_table and (table_line.match(line) or table_divider.match(stripped))):
            flush_buffer()
            inside_table = True
            new_lines.append(line)
            continue

        # List item -> start new buffer
        if list_prefix.match(line):
            flush_buffer()
            inside_table = False
            buffer.append(line)
            continue
            
        # >>> NEW: block HTML should not be merged with neighbors
        if html_block_re.match(line) or html_close_re.match(line):
            flush_buffer()
            inside_table = False
            new_lines.append(line)
            continue            

        # Continuation
        # If this line looks like block HTML, don't buffer (merging would collapse it)
        if html_block_re.match(line) or html_close_re.match(line):
            flush_buffer()
            new_lines.append(line)
            continue

        buffer.append(line)


    flush_buffer()
    return "\n".join(new_lines)
    


def collapse_soft_wraps_inside_admonitions(md_text: str) -> str:
    """
    Inside :::admonitions, collapse paragraph soft-wraps so each paragraph becomes a single line.
    Preserve:
      - blank lines (paragraph separators),
      - list items (start with -, *, +),
      - code fences (``` / ~~~) and their contents,
      - table lines starting with '|', and header dividers.

    Works only inside :::... blocks, leaves content outside untouched.
    """
    import re

    lines = md_text.splitlines()
    out = []

    fence_open_re  = re.compile(r'^\s*:::\w+\s*$')
    fence_close_re = re.compile(r'^\s*:::\s*$')
    code_fence_re  = re.compile(r'^\s*(```|~~~)')
    list_head_re   = re.compile(r'^\s*([-*+]|[0-9]+\.)\s+')
    table_line_re  = re.compile(r'^\s*\|')
    table_div_re   = re.compile(r'^\s*[:\-| ]+$')

    inside_admon = False
    inside_code  = False
    # buffer for a paragraph’s soft-wrapped lines (inside admonitions only)
    para_buf = []

    def flush_paragraph():
        nonlocal para_buf
        if para_buf:
            # join with spaces; keep the paragraph’s leading indent if any on first line
            first = para_buf[0]
            # detect leading spaces/tabs to preserve
            leading_ws = re.match(r'^[ \t]*', first).group(0)
            # strip only leading whitespace from subsequent lines, not from first
            joined = " ".join([first.strip(), *[ln.strip() for ln in para_buf[1:]]]).strip()
            out.append(leading_ws + joined)
            para_buf = []

    i = 0
    n = len(lines)
    while i < n:
        line = lines[i]

        # outside admonitions: just copy
        if not inside_admon:
            out.append(line)
            if fence_open_re.match(line):
                inside_admon = True
            i += 1
            continue

        # inside admonition:
        # handle fence close
        if fence_close_re.match(line) and not inside_code:
            flush_paragraph()
            out.append(line)
            inside_admon = False
            i += 1
            continue

        # code fence toggling inside admonition
        if code_fence_re.match(line):
            flush_paragraph()
            out.append(line)
            inside_code = not inside_code
            i += 1
            continue

        if inside_code:
            out.append(line)
            i += 1
            continue

        # blank line -> paragraph boundary
        if not line.strip():
            flush_paragraph()
            out.append(line)
            i += 1
            continue

        # list head or table-related -> paragraph boundary; emit as-is
        if list_head_re.match(line) or table_line_re.match(line) or table_div_re.match(line):
            flush_paragraph()
            out.append(line)
            i += 1
            continue

        # otherwise, this is a soft-wrapped paragraph line -> accumulate
        para_buf.append(line)
        i += 1

    # tail
    flush_paragraph()
    return "\n".join(out)
    
def clean_admonition_lists(md_text: str) -> str:
    """
    Inside :::admonitions, drop meaningless list items like '+ assignment' or '- assignment'
    while keeping nested list/code structure valid.
    """
    import re

    lines = md_text.splitlines()
    out = []
    inside_admon = False
    inside_code = False

    fence_open_re  = re.compile(r'^\s*:::\w+\s*$')
    fence_close_re = re.compile(r'^\s*:::\s*$')
    code_fence_re  = re.compile(r'^\s*(```|~~~)')
    assignment_line_re = re.compile(r'^\s*[+*-]\s*assignment\s*$', re.I)

    for line in lines:
        # Detect admonition entry/exit
        if fence_open_re.match(line):
            inside_admon = True
            out.append(line)
            continue
        if fence_close_re.match(line):
            inside_admon = False
            out.append(line)
            continue

        # Detect code fence toggles
        if code_fence_re.match(line):
            out.append(line)
            inside_code = not inside_code
            continue
            

        if inside_code:
            out.append(line)
            continue

        # When inside an admonition, skip meaningless list entries
        if inside_admon and assignment_line_re.match(line):
            continue

        out.append(line)

    return "\n".join(out)

def collapse_leading_newlines_before_images_in_lists(md_text: str) -> str:
    """
    Remove a blank line between a list item and an image with the same indent.
    Example fixed:
      - "  - item text\n\n  ![alt](...)" -> "  - item text\n  ![alt](...)"
    """
    import re
    pattern1 = re.compile(r'(?m)^(?P<head>(?P<indent>\s*)(?:[-*+]|\d+\.)[^\n]*?)\n\n(?=(?P=indent)!\[)')
    md_text = pattern1.sub(r'\g<head>\n', md_text)
    pattern2 = re.compile(r'(?m)^(?P<head>(?P<indent>\s{2,})(?!#|```|~~~).+?)\n\n(?=(?P=indent)!\[)')
    md_text = pattern2.sub(r'\g<head>\n', md_text)
    return md_text
    
def collapse_blank_lines_before_codeblocks_in_lists(md_text: str) -> str:
    """
    Remove blank lines between a list line (head or continuation) and a fenced code block.
    Works at any nesting depth and with ``` or ~~~, even if the fence is indented further.

    Examples fixed:
      - "- Item\n\n  ```py"     -> "- Item\n  ```py"
      - "  * Sub\n\n    ~~~"    -> "  * Sub\n    ~~~"
      - "    Text\n\n    ```"   -> "    Text\n    ```"
    """
    import re

    # Case 1: directly after a list *head* (base indent + marker)
    # Allow extra spaces before the fence and any language tag.
    pat_head = re.compile(
        r'(?m)'
        r'^(?P<head>(?P<indent>\s*)(?:[-*+]|\d+\.)[^\n]*?)'
        r'\n{2,}'
        r'(?=(?P=indent)[ \t]*(?:```|~~~))'
    )

    # Case 2: after any *continuation* line inside a list item
    # (at least 2 spaces of indent; avoid headings and fences themselves).
    pat_cont = re.compile(
        r'(?m)'
        r'^(?P<head>(?P<indent>\s{2,})(?!#|```|~~~).+?)'
        r'\n{2,}'
        r'(?=(?P=indent)[ \t]*(?:```|~~~))'
    )

    # Apply repeatedly until stable in case adjacent patterns cascade.
    prev = None
    out = md_text
    while out != prev:
        prev = out
        out = pat_head.sub(r'\g<head>\n', out)
        out = pat_cont.sub(r'\g<head>\n', out)

    return out

def collapse_blank_lines_before_notes_in_lists(md_text: str) -> str:
    """
    Remove blank lines between a list item (any nesting depth) and a note/admonition fence (:::note, :::tip, etc.).
    Examples fixed:
      - "- Item\n\n  :::note" -> "- Item\n  :::note"
      - "  * Nested\n\n    :::warning" -> "  * Nested\n    :::warning"
    """
    import re

    # Match a list head or continuation, followed by 1+ blank lines, then an indented ::: fence
    pattern1 = re.compile(
        r'(?m)^(?P<head>(?P<indent>\s*)(?:[-*+]|\d+\.)[^\n]*?)\n{2,}(?=(?P=indent)[ \t]*:::)'
    )
    pattern2 = re.compile(
        r'(?m)^(?P<head>(?P<indent>\s{2,})(?!#|```|~~~).+?)\n{2,}(?=(?P=indent)[ \t]*:::)'
    )

    text = md_text
    prev = None
    while text != prev:
        prev = text
        text = pattern1.sub(r'\g<head>\n', text)
        text = pattern2.sub(r'\g<head>\n', text)
    return text



def indent_images_like_list_content(md_text: str) -> str:
    """
    Make Markdown image lines inside list items align with the list content (continuation indent).
    Also collapses a single blank line between the list line and the image, if present.

    Examples:
      "- Foo\n\n![img](u)"     -> "- Foo\n  ![img](u)"
      "  * Bar\n\n  ![img](u)" -> "  * Bar\n    ![img](u)"
      "10. Baz\n\n![img](u)"   -> "10. Baz\n    ![img](u)"   (continuation indent width = len('10.') + 1)
    """
    import re

    lines = md_text.splitlines()
    out = []
    i, n = 0, len(lines)

    list_head_re = re.compile(r'^(\s*)([-*+]|\d+\.)\s+(.*\S.*)$')  # base indent, marker, text
    code_fence_re = re.compile(r'^\s*(```|~~~)')  # don’t modify inside fenced code blocks

    inside_code = False

    while i < n:
        line = lines[i]

        # Pass code fences through untouched
        if code_fence_re.match(line):
            inside_code = not inside_code
            out.append(line)
            i += 1
            continue

        if inside_code:
            out.append(line)
            i += 1
            continue

        m = list_head_re.match(line)
        if not m:
            out.append(line)
            i += 1
            continue

        # We’re at a list item head
        base_indent, marker, _ = m.groups()
        cont_indent = base_indent + (" " * (len(marker) + 1))  # align with first char after marker

        out.append(line)
        i += 1

        # Walk forward within the same list item block:
        #   - stop at a blank line followed by a dedented line,
        #   - or a new sibling/parent list item (same or less indent),
        #   - or a heading/fence.
        while i < n:
            nxt = lines[i]

            # Stop on fences
            if code_fence_re.match(nxt):
                break

            # New list item at same/less indent -> stop
            if re.match(rf'^{re.escape(base_indent)}([-*+]|\d+\.)\s+', nxt):
                break

            # Dedented non-empty line -> likely a new block
            if nxt.strip() and len(nxt) - len(nxt.lstrip(" ")) < len(base_indent):
                break

            # Collapse one blank line just before an image with base indent
            if not nxt.strip():
                if (i + 1 < n) and re.match(rf'^{re.escape(base_indent)}!\[', lines[i + 1]):
                    # skip the blank line
                    i += 1
                    nxt = lines[i]  # fall through to reindent the image below
                else:
                    out.append(nxt)
                    i += 1
                    continue

            # Reindent images that start at base indent to continuation indent
            if re.match(rf'^{re.escape(base_indent)}!\[', nxt):
                out.append(re.sub(rf'^{re.escape(base_indent)}', cont_indent, nxt, count=1))
                i += 1
                continue

            # Any other line inside this list item
            out.append(nxt)
            i += 1

        # loop ends when we hit a boundary (next list item / fence / etc.)
    return "\n".join(out)
    
# put this near your other small helpers
def _dedent_admonition_content(s: str) -> str:
    lines = s.splitlines()

    # trim leading/trailing blank lines
    while lines and not lines[0].strip():
        lines.pop(0)
    while lines and not lines[-1].strip():
        lines.pop()

    if not lines:
        return ""

    # compute common left indent across non-empty lines (spaces or tabs)
    import re
    indents = []
    for ln in lines:
        if ln.strip():
            m = re.match(r'^[ \t]*', ln)
            indents.append(len(m.group(0)) if m else 0)
    common = min(indents) if indents else 0

    if common:
        pad = r' ' * common
        lines = [ln[common:] if ln.startswith(pad) else ln for ln in lines]
    return "\n".join(lines)


def indent_notes_like_list_content(md_text: str) -> str:
    """
    Inside list items, indent Docusaurus-style note fences (:::note / :::tip / etc.)
    to the list's continuation indent (same column as list content), and collapse
    a single blank line between the list head and the fence if present.
    """
    import re

    lines = md_text.splitlines()
    out = []
    i, n = 0, len(lines)

    list_head_re = re.compile(r'^(\s*)([-*+]|\d+\.)\s+(.*\S.*)$')   # base indent, marker, text
    fence_open_re = re.compile(r'^\s*:::\w+\s*$')                   # :::note / :::tip / :::warning / etc.
    fence_close_re = re.compile(r'^\s*:::\s*$')
    code_fence_re = re.compile(r'^\s*(```|~~~)')                    # skip fenced code

    inside_code = False

    while i < n:
        line = lines[i]

        # Toggle code fence mode
        if code_fence_re.match(line):
            inside_code = not inside_code
            out.append(line)
            i += 1
            continue

        if inside_code:
            out.append(line)
            i += 1
            continue

        m = list_head_re.match(line)
        if not m:
            out.append(line)
            i += 1
            continue

        # We are at a list-item head
        base_indent, marker, _ = m.groups()
        cont_indent = base_indent + (" " * (len(marker) + 1))  # align with first char after marker

        out.append(line)
        i += 1

        # Consume optional single blank line before a fence
        if i < n and not lines[i].strip():
            if i + 1 < n and fence_open_re.match(lines[i + 1]) and lines[i + 1].startswith(base_indent):
                # drop this single blank line
                i += 1

        # If the next line is a fence open at base indent, reindent whole fence block
        if i < n and fence_open_re.match(lines[i]) and lines[i].startswith(base_indent):
            # collect fence block
            block = []
            while i < n:
                cur = lines[i]
                block.append(cur)
                i += 1
                if fence_close_re.match(cur):
                    break
                    
            stripped = [re.sub(rf'^{re.escape(base_indent)}', '', b, count=1) for b in block]

            # reindent every line in the fence from base -> continuation indent
            reindented = [cont_indent + b for b in stripped]
            out.extend(reindented)
            continue

        # Otherwise just continue copying lines until list-item boundary
        while i < n:
            nxt = lines[i]
            # stop when we reach a sibling/parent list head (same or less indent)
            if re.match(rf'^{re.escape(base_indent)}([-*+]|\d+\.)\s+', nxt):
                break
            if code_fence_re.match(nxt):
                break
            out.append(nxt)
            i += 1

    return "\n".join(out)




from bs4 import NavigableString, Tag

def strip_paragraphs_in_lists(container: BeautifulSoup) -> None:
    """
    Normalize list markup inside list items:
    1) Unwrap neutral <div>/<span> whose ONLY child is a <p> (do this first; preserves inline markup like <code>).
    2) Unwrap/remove <p> (including <p class="p">) inside <li>.
    3) Unwrap leading wrapper <div> that either (A) directly wraps a nested <ul>/<ol> or
       (B) sits immediately before a sibling list (including when the sibling is a wrapper <div> around the list).
       This applies to ANY neutral <div> (e.g., class="p", class="itemgroup info"), while skipping admonitions.
    4) Generic unwrap of trivial <div>/<span> wrappers, with protections.
    """
    if not container:
        return

    for lst in list(container.find_all(["ul", "ol"])):
        # Remove stray <p> directly under <ul>/<ol>
        for pnode in list(lst.find_all("p", recursive=False)):
            if _in_itemgroup_info(pnode):
                continue
            if not pnode.get_text(strip=True):
                pnode.decompose()
            else:
                pnode.unwrap()

        # Work within each <li>
        for li in list(lst.find_all("li")):

            # (1) Unwrap neutral wrappers whose ONLY child is a <p>
            for wrapper_name in ("div", "span"):
                for w in list(li.find_all(wrapper_name, recursive=False)):
                    if _in_itemgroup_info(w):
                        continue
                    # Skip wrappers with meaningful attributes beyond class/id
                    if w.attrs and not set(w.attrs.keys()).issubset({"class", "id"}):
                        continue
                    tag_children = [c for c in w.contents if isinstance(c, Tag)]
                    text_has_non_ws = any(isinstance(c, NavigableString) and c.strip() for c in w.contents)
                    if len(tag_children) == 1 and tag_children[0].name == "p" and not text_has_non_ws:
                        if _in_itemgroup_info(tag_children[0]):
                            continue
                        w.unwrap()

            # (2) Unwrap/remove <p> inside <li>
            for pnode in list(li.find_all("p")):
                if _in_itemgroup_info(pnode):
                    continue
                if not pnode.get_text(strip=True):
                    pnode.decompose()
                else:
                    pnode.unwrap()

            # (3) Unwrap leading wrapper <div> around or before a nested list (generalized from only div.p)
            for d in list(li.find_all("div", recursive=False)):
                if _in_itemgroup_info(d):
                    continue
                # Skip admonitions or special containers
                classes = set(d.get("class") or [])
                if {"note", "warning", "important", "information", "tip", "danger"} & classes:
                    continue
                if (d.get("id") or "").lower().startswith("admonition"):
                    continue

                # Case A: this <div> directly wraps a <ul>/<ol>
                if d.find(["ul", "ol"], recursive=False):
                    d.unwrap()
                    continue

                # Case B: this <div> is immediately followed by a sibling list
                nxt = d.find_next_sibling()
                is_list_sibling = (
                    nxt is not None and (
                        nxt.name in {"ul", "ol"} or
                        (nxt.name == "div" and nxt.find(["ul", "ol"], recursive=False))
                    )
                )
                if is_list_sibling:
                    if d.get_text(strip=True):
                        # preserve inline markup (e.g., <code>) by unwrapping
                        d.unwrap()
                    else:
                        d.decompose()
                    continue

            # (4) Generic unwrap for trivial wrappers (keep protections)
            for wrapper_name in ("div", "span"):
                for w in list(li.find_all(wrapper_name)):
                    if _in_itemgroup_info(w):
                        continue
                    # Leave wrappers that contain nested structures
                    if w.find(["ul", "ol", "table", "pre", "code", "img"]):
                        continue
                    # Do NOT unwrap admonitions
                    classes = set(w.get("class") or [])
                    if {"note", "warning", "important", "information", "tip", "danger"} & classes:
                        continue
                    if (w.get("id") or "").lower().startswith("admonition"):
                        continue

                    if not w.attrs or set(w.attrs.keys()).issubset({"class", "id"}):
                        if not w.get_text(strip=True):
                            w.decompose()
                        else:
                            w.unwrap()




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

######## below this are chatgpt interactions
def move_inline_admonitions_to_own_line(md_text: str) -> str:
    """
    Fix cases where a :::note (or similar) fence appears inline with list text.
    Does NOT add extra blank lines to properly formatted standalone notes.
    """
    import re

    ADMO = r'(?:note|tip|warning|info|important|caution|danger)'

    # Only target list items with inline admonitions (e.g., "- text :::note")
    pattern_inline_list = re.compile(
        rf'^(?P<base>\s*)(?P<mark>[-*+]|\d+\.)\s+(?P<head>.*?)(?P<fence>:::{ADMO})(?P<after>[^\n]*)$',
        re.M
    )

    def _split_list_inline(m):
        base = m.group('base')
        mark = m.group('mark')
        head = m.group('head').rstrip()
        fence = m.group('fence')
        after = m.group('after').strip()

        result = [f"{base}{mark} {head}"]
        result.append(f"{base}{fence}")  # fence starts on its own line
        if after:
            result.append(f"{base}{after}")
        return "\n".join(result)

    md_text = pattern_inline_list.sub(_split_list_inline, md_text)

    # Prevent extra blank lines for already-correct notes
    # (do not touch ::: lines that are already standalone)
    return md_text

import re

def hoist_trailing_admonition_after_sublist(md_text: str) -> str:
    """
    If a :::admonition block appears at a deeper indent immediately at the end
    of a sublist, reindent it one level up so it becomes a sibling of the parent
    list item (i.e., after the sublist), preserving the parent's continuation indent.
    """
    # Normalize tabs defensively (your pipeline is space-based)
    md_text = md_text.replace('\t', '    ')

    fence_open_re  = re.compile(r'^(\s*):::(note|tip|warning|danger|info|important|caution)\s*$', re.M)
    fence_close_re = re.compile(r'^(\s*):::\s*$', re.M)
    list_head_re   = re.compile(r'^(\s*)([-*+]|\d+\.)\s', re.M)

    lines = md_text.splitlines()
    out = []
    i, n = 0, len(lines)

    def leading_spaces(s: str) -> int:
        return len(s) - len(s.lstrip(' '))

    while i < n:
        m_open = fence_open_re.match(lines[i])
        if not m_open:
            out.append(lines[i]); i += 1
            continue

        # Capture the whole fence block starting at i
        fence_indent = m_open.group(1)
        j = i + 1
        while j < n and not fence_close_re.match(lines[j]):
            j += 1
        if j < n:  # include closing line
            j += 1

        block = lines[i:j]

        # Look backward to nearest non-blank line in 'out'
        k = len(out) - 1
        while k >= 0 and not out[k].strip():
            k -= 1

        parent_cont_indent = None
        if k >= 0:
            m_parent = list_head_re.match(out[k])
            if m_parent:
                base_indent, marker = m_parent.group(1), m_parent.group(2)
                # continuation indent = base indent + one space after marker
                parent_cont_indent = base_indent + (" " * (len(marker) + 1))

        # Look ahead to see if we’re at the end of the sublist (next non-blank is dedented)
        t = j
        while t < n and not lines[t].strip():
            t += 1
        end_of_sublist = (t >= n) or (leading_spaces(lines[t]) < len(fence_indent))

        # Hoist only if:
        #  (a) we have a parent continuation indent,
        #  (b) the fence is deeper than the parent continuation indent, and
        #  (c) we’re at the end of that sublist.
        if parent_cont_indent and end_of_sublist and len(fence_indent) > len(parent_cont_indent):
            stripped = [re.sub(rf'^{re.escape(fence_indent)}', '', ln, count=1) for ln in block]
            reindented = [(parent_cont_indent + ln) if ln.strip() else ln for ln in stripped]
            out.extend(reindented)
        else:
            out.extend(block)

        i = j

    return "\n".join(out)

def _in_itemgroup_info(node: Tag) -> bool:
    """Return True if 'node' has an ancestor <div class="itemgroup info">."""
    p = node if isinstance(node, Tag) else None
    while isinstance(p, Tag):
        if p.name == "div":
            classes = set(p.get("class") or [])
            if {"itemgroup", "info"}.issubset(classes):
                return True
        p = p.parent
    return False

def collapse_blank_lines_before_sublists(md_text: str) -> str:
    """
    Remove blank lines between a list item and an immediately following *nested* list.
    Works at any nesting depth. Preserves code fences/admonitions.
    Examples fixed:
      - "- Parent\n\n  - Child"  -> "- Parent\n  - Child"
      - "10. A\n\n    * B"       -> "10. A\n    * B"
    """
    import re
    # Case 1: blank(s) after a list HEAD, then a deeper-indented list head
    pat_after_head = re.compile(
        r'(?m)'
        r'^(?P<head>(?P<base>\s*)(?:[-*+]|\d+\.)[^\n]*?)'
        r'\n{2,}'
        r'(?=(?P=base)[ \t]{2,}(?:[-*+]|\d+\.)\s+)'  # deeper indent + new list
    )
    # Case 2: blank(s) after a continuation line within a list item, then a deeper list
    pat_after_cont = re.compile(
        r'(?m)'
        r'^(?P<head>(?P<base>\s{2,})(?!#|```|~~~|:::).+?)'
        r'\n{2,}'
        r'(?=(?P=base)[ \t]{2,}(?:[-*+]|\d+\.)\s+)'
    )
    prev, out = None, md_text
    while out != prev:
        prev = out
        out = pat_after_head.sub(r'\g<head>\n', out)
        out = pat_after_cont.sub(r'\g<head>\n', out)
    return out


def collapse_blank_lines_between_sibling_list_items(md_text: str) -> str:
    """
    Remove blank lines between consecutive list items at the same indent.
    Example fixed:
      - "- One\n\n- Two" -> "- One\n- Two"
    """
    import re
    # Between two list *heads* at the same base indent
    pat_head_to_head = re.compile(
        r'(?m)'
        r'^(?P<first>(?P<base>\s*)(?:[-*+]|\d+\.)[^\n]*?)'
        r'\n{2,}'
        r'(?=(?P=base)(?:[-*+]|\d+\.)\s+)'
    )
    # Between any indented continuation line and the next head at the same base indent
    pat_cont_to_head = re.compile(
        r'(?m)'
        r'^(?P<first>(?P<base>\s{2,})(?!#|```|~~~|:::).+?)'
        r'\n{2,}'
        r'(?=(?P=base)(?:[-*+]|\d+\.)\s+)'
    )
    prev, out = None, md_text
    while out != prev:
        prev = out
        out = pat_head_to_head.sub(r'\g<first>\n', out)
        out = pat_cont_to_head.sub(r'\g<first>\n', out)
    return out

#############################
# ---------------------------
# Helpers to extract Next.js data
# ---------------------------
import json
import re
from bs4 import BeautifulSoup

def _get_next_data_script_text(html_text: str) -> str | None:
    """Return the JSON string inside <script id="__NEXT_DATA__"> or None."""
    soup = BeautifulSoup(html_text, "html.parser")
    tag = soup.find("script", id="__NEXT_DATA__", type="application/json")
    if tag and tag.string:
        return tag.string
    tag = soup.find("script", id="__NEXT_DATA__")
    if tag and tag.string:
        return tag.string
    return None

def _find_first_html_string(obj):
    """
    Recursively look for a string value that looks like HTML (large and containing tags).
    Returns the first such string or None.
    """
    if isinstance(obj, str):
        if "<" in obj and ">" in obj and len(obj) > 200:
            return obj
        return None
    if isinstance(obj, dict):
        # Heuristic: check known path shapes first for speed
        for candidate_key in ("page", "pageProps", "rawContent", "Component", "topicBody", "Values"):
            if candidate_key in obj:
                found = _find_first_html_string(obj[candidate_key])
                if found:
                    return found
        for v in obj.values():
            found = _find_first_html_string(v)
            if found:
                return found
    if isinstance(obj, (list, tuple)):
        for v in obj:
            found = _find_first_html_string(v)
            if found:
                return found
    return None

def extract_html_fragment_from_next_data(html_text: str) -> str | None:
    """
    Parse __NEXT_DATA__ and find the first large HTML-like string.
    Heuristic: look recursively for a string that contains tags and is reasonably long.
    Returns that HTML fragment or None.
    """
    json_text = _get_next_data_script_text(html_text)
    if not json_text:
        return None
    try:
        data = json.loads(json_text)
    except Exception:
        return None

    def _find_html_like(obj):
        if isinstance(obj, str):
            if "<" in obj and ">" in obj and len(obj) > 200:
                return obj
            return None
        if isinstance(obj, dict):
            # check likely keys first
            for k in ("pageProps", "page", "props", "rawContent", "Component", "topicBody", "Values"):
                if k in obj:
                    found = _find_html_like(obj[k])
                    if found:
                        return found
            for v in obj.values():
                found = _find_html_like(v)
                if found:
                    return found
        if isinstance(obj, (list, tuple)):
            for v in obj:
                found = _find_html_like(v)
                if found:
                    return found
        return None

    return _find_html_like(data)
    
def extract_topicbody_html_from_next_data(html_text: str) -> str | None:
    """
    UiPath docs (Next.js): the article body is usually in:
      props.pageProps.page.containerItems[].rawContent.data.Component.Fields.topicBody.Values[0]
    Returns HTML string or None.
    """
    json_text = _get_next_data_script_text(html_text)
    if not json_text:
        return None

    try:
        data = json.loads(json_text)
    except Exception:
        return None

    page = (
        data.get("props", {})
            .get("pageProps", {})
            .get("page", {})
    )

    container_items = page.get("containerItems") or []
    for item in container_items:
        fields = (
            item.get("rawContent", {})
                .get("data", {})
                .get("Component", {})
                .get("Fields", {})
        )

        topic_body = (fields.get("topicBody") or {}).get("Values")
        if isinstance(topic_body, list) and topic_body:
            body_html = topic_body[0]
            if isinstance(body_html, str) and "<" in body_html:
                # json.loads already decoded \u003c etc; unescape any entities just in case
                return html.unescape(body_html)

        # (Optional) sometimes content is stored under a different key
        for alt_key in ("body", "content", "markdown", "mdx"):
            alt = (fields.get(alt_key) or {}).get("Values")
            if isinstance(alt, list) and alt and isinstance(alt[0], str) and "<" in alt[0]:
                return html.unescape(alt[0])

    return None


# ---------------------------
# Mapper for sitemapSubtree -> sidebar items
# ---------------------------
def _sitemap_node_to_sidebar_item(node: dict, parent_dir: str, page_dir: str, base_url: str) -> dict:
    """
    Convert one node from sitemapSubtree -> {title, href?, children?}
    node is expected to have 'title' and optionally 'topicSlug' and 'items' (children list).
    """
    title = node.get("title") or node.get("label") or node.get("text") or ""
    if not title:
        return None
    item = {"title": title}
    topic = node.get("topicSlug") or node.get("slug") or node.get("topic") or None
    if topic:
        # Build site path from topicSlug (match ensure_mdx_path_from_href semantics).
        # We construct a path relative to the site: page_dir + '/' + topic + '.md'
        # If page_dir is '/', join correctly.
        if not topic.startswith("/"):
            # assume topicSlug is a single slug component: create path relative to product/delivery/version
            md_path = posixpath.join(page_dir, topic + ".md")
        else:
            md_path = topic
        # Normalize leading slash and strip double slashes
        if not md_path.startswith("/"):
            md_path = "/" + md_path
        md_path = re.sub(r"//+", "/", md_path)
        item["href"] = md_path
    # children
    children_nodes = node.get("items") or node.get("children") or []
    children = []
    for child in children_nodes:
        child_item = _sitemap_node_to_sidebar_item(child, parent_dir, page_dir, base_url)
        if child_item:
            children.append(child_item)
    if children:
        item["children"] = children
    return item

def build_sidebar_from_next_data(resp_text: str, url: str) -> dict | None:
    """
    Attempt to build the sidebar structure from __NEXT_DATA__'s sitemapSubtree.
    Returns sidebar dict {title, children} or None.
    """
    json_text = _get_next_data_script_text(resp_text)
    if not json_text:
        return None
    try:
        data = json.loads(json_text)
    except Exception:
        return None
    page_props = data.get("props", {}).get("pageProps", {}) or {}
    sitemap = page_props.get("sitemapSubtree")
    if not sitemap or not isinstance(sitemap, dict):
        return None
    # page_dir = directory portion of the URL path, same as your path_dirname()
    page_dir = path_dirname(urllib.parse.urlparse(url).path or "/")
    guide_title = derive_guide_name_from_slug(url)
    children = []
    # sitemap['items'] is usually the top-level list
    for n in sitemap.get("items", []) or []:
        item = _sitemap_node_to_sidebar_item(n, parent_dir="", page_dir=page_dir, base_url=url)
        if item:
            children.append(item)
    return {"title": guide_title, "children": children}

def strip_fragment(u: str) -> str:
    return u.split("#", 1)[0].strip()

#############################
def html_to_markdown_github(url, position_counter=None, crawl=True):
    """Convert pages to Markdown and crawl ONLY within the same guide root."""
    try:
        global GLOBAL_SESSION
        if GLOBAL_SESSION is None:
            GLOBAL_SESSION = requests.Session()

        parsed_url = urllib.parse.urlparse(url)

        # ✅ Guide root = parent folder of the starting URL (what you want)
        guide_root = (
            f"{parsed_url.scheme}://{parsed_url.netloc}"
            + parsed_url.path.rsplit("/", 1)[0]
            + "/"
        )

        folder_structure = create_folder_structure_from_url(url)
        output_folder = os.path.join(os.getcwd(), folder_structure)
        os.makedirs(output_folder, exist_ok=True)

        visited_urls = set()
        queued_urls = set()
        queue = [url]
        queued_urls.add(strip_fragment(url))
        session = GLOBAL_SESSION
        skipped_urls = []

        while queue:
            current_url = strip_fragment(queue.pop(0))
            if not current_url:
                continue

            # ✅ Never leave the guide root
            if not current_url.startswith(guide_root):
                continue

            if current_url in visited_urls:
                continue
            visited_urls.add(current_url)

            try:
                response = safe_get_html(current_url, session=session)
                soup = BeautifulSoup(response.content, "html.parser")

                # 1) Try SSR
                doc_container = soup.find("div", id="DocContainer")

                # 2) Fall back to Next.js __NEXT_DATA__
                if not doc_container:
                    print(f"⚠️  DocContainer not found in server HTML: {current_url}")

                    fallback_html = extract_topicbody_html_from_next_data(response.text)
                    if not fallback_html:
                        fallback_html = extract_html_fragment_from_next_data(response.text)

                    print("DEBUG: fallback_html length =", len(fallback_html) if fallback_html else 0)

                    if fallback_html:
                        print("ℹ️  Extracted HTML from __NEXT_DATA__ (Next.js) — using it as DocContainer.")
                        frag_soup = BeautifulSoup(fallback_html, "html.parser")
                        doc_container = frag_soup.find("div", id="DocContainer") or frag_soup
                    else:
                        print(f"⚠️  No __NEXT_DATA__ HTML fragment discovered for: {current_url}")
                        continue

                if not doc_container:
                    continue

                # ✅ ALWAYS convert (SSR or Next.js)
                for anchor in doc_container.find_all("a", href=re.compile(r"^#")):
                    anchor.decompose()

                remove_empty_tags(doc_container)
                flatten_note_spans(doc_container)

                for pre in doc_container.find_all("pre"):
                    for code in pre.find_all("code", recursive=False):
                        code.unwrap()

                for clip in doc_container.select("span.clipboard-code"):
                    clip.decompose()

                transform_availability_images(doc_container)
                transform_images_in_simple_tables_to_markdown(doc_container)

                table_html_map = extract_complex_tables(doc_container)
                strip_paragraphs_in_lists(doc_container)

                sup_map_global = protect_sup_tags(doc_container)

                transform_admonitions(doc_container)
                ignore_material_icons(doc_container)
                normalize_paragraphs(doc_container)
                escape_angle_brackets_plain_text(doc_container)

                markdown_content = md.markdownify(
                    str(doc_container),
                    heading_style="ATX",
                    strip=["br"],
                )

                markdown_content = cleanup_markdown(markdown_content)
                markdown_content = unescape_md_in_placeholders(markdown_content)
                markdown_content = convert_html_imgs_in_md_tables(markdown_content)
                markdown_content = remove_leading_h2(markdown_content)
                markdown_content = promote_headings(markdown_content)
                markdown_content = unwrap_markdown_paragraphs_and_lists(markdown_content)
                markdown_content = move_inline_admonitions_to_own_line(markdown_content)
                markdown_content = collapse_soft_wraps_inside_admonitions(markdown_content)
                markdown_content = clean_admonition_lists(markdown_content)
                markdown_content = collapse_leading_newlines_before_images_in_lists(markdown_content)
                markdown_content = collapse_blank_lines_before_codeblocks_in_lists(markdown_content)
                markdown_content = collapse_blank_lines_before_notes_in_lists(markdown_content)
                markdown_content = collapse_blank_lines_before_sublists(markdown_content)
                markdown_content = collapse_blank_lines_between_sibling_list_items(markdown_content)
                markdown_content = indent_images_like_list_content(markdown_content)
                markdown_content = indent_notes_like_list_content(markdown_content)
                markdown_content = hoist_trailing_admonition_after_sublist(markdown_content)

                for placeholder, table_html in table_html_map.items():
                    markdown_content = markdown_content.replace(placeholder, table_html)

                markdown_content = restore_sup_placeholders(markdown_content, sup_map_global)

                slug = last_path_segment_no_ext(current_url)
                page_folder_structure = create_folder_structure_from_url(current_url)
                page_output_folder = os.path.join(os.getcwd(), page_folder_structure)
                os.makedirs(page_output_folder, exist_ok=True)

                file_name = f"{slug}.md"
                output_path = os.path.join(page_output_folder, file_name)

                title_tag = soup.find("title")
                if title_tag and title_tag.string and title_tag.string.strip():
                    title = clean_title(title_tag.string.strip())
                else:
                    title = slug.replace("-", " ").strip().title()

                frontmatter = (
                    f"---\n"
                    f'title: "{title}"\n'
                    f"visible: true\n"
                    f'slug: "{slug}"\n'
                    f"---\n\n"
                )

                full_markdown_content = frontmatter + markdown_content
                full_markdown_content = prefix_relative_markdown_links(
                    full_markdown_content, domain="https://docs.uipath.com"
                )
                full_markdown_content = unwrap_bare_autolinks(full_markdown_content)
                full_markdown_content = re.sub(r'\\+_', '_', full_markdown_content)

                with open(output_path, "w", encoding="utf-8") as f:
                    f.write(full_markdown_content)

                print(f"📝 Saved MD: {output_path}")

                # ✅ Crawl only within guide_root
                if crawl:
                    for link in doc_container.find_all("a", href=True):
                        href = strip_fragment(link["href"].strip())
                        if (
                            not href
                            or href.startswith("#")
                            or href.startswith("mailto:")
                            or href.startswith("javascript:")
                            or href.startswith("tel:")
                        ):
                            continue

                        # Normalize to absolute URL
                        if href.startswith("/"):
                            href = urllib.parse.urljoin(
                                f"{parsed_url.scheme}://{parsed_url.netloc}", href
                            )
                        elif not href.startswith("http://") and not href.startswith("https://"):
                            href = urllib.parse.urljoin(current_url, href)

                        href = strip_fragment(href)

                        # ✅ Only keep pages in this guide
                        if href.startswith(guide_root) and href not in visited_urls and href not in queued_urls:
                            queue.append(href)
                            queued_urls.add(href)

            except requests.exceptions.RequestException as e:
                print(f"Error fetching URL '{current_url}': {e}")
                skipped_urls.append((current_url, str(e)))
            except Exception as e:
                print(f"An error occurred while processing '{current_url}': {e}")

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
        "description": "Your product description",
        "displayOrder": "1"
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
        path = posixpath.join(path, "index.md")
    else:
        path = strip_ext(path) + ".md"
    path = re.sub(r"//+", "/", path)
    if not path.startswith("/"):
        path = "/" + path
    return path

def derive_child_path_from_parent_dir(title: str, parent_dir: str) -> str:
    s = slugify(title)
    return posixpath.join(parent_dir if parent_dir else "/", s + ".md")

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
    global GLOBAL_SESSION
    if GLOBAL_SESSION is None:
        GLOBAL_SESSION = requests.Session()
    resp = sso_get_with_retries(url, session=GLOBAL_SESSION, headers=headers, timeout=30)    
    resp.raise_for_status()
    soup = BeautifulSoup(resp.text, "html.parser")
    for tname in list(BANNED_TAGS):
        for t in soup.find_all(tname):
            t.decompose()
    root = pick_sidebar_root(soup)
    if not root:
        # try Next.js data -> sitemapSubtree
        sidebar_from_next = build_sidebar_from_next_data(resp.text, url)
        if sidebar_from_next:
            return sidebar_from_next
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
    parser = argparse.ArgumentParser(
        description="Convert HTML to Markdown. Use --op for one-page (no crawl)."
    )
    parser.add_argument(
        "--op",
        action="store_true",
        help="One-page mode: convert only the provided URL without crawling in-site links.",
    )
    args = parser.parse_args()

    position_tracking = {}
    mode_label = "ONE-PAGE" if args.op else "CRAWL"
    print(f"▶ Running in {mode_label} mode.")

    while True:
        target_url = input("Enter the URL of the starting HTML page (or press Enter to quit): ").strip()
        if not target_url:
            print("No URL entered. Exiting.")
            break

        # Single call — crawl depends on --op flag
        html_to_markdown_github(target_url, position_tracking, crawl=(not args.op))

        print(f"✅ Conversion completed for: {target_url}")

        # Build sidebar + metadata JSON for the same URL
        try:
            write_sidebar_and_metadata(target_url)
        except Exception as e:
            print(f"❌ Sidebar/metadata generation failed: {e}")

        print("-" * 72)

        
        
