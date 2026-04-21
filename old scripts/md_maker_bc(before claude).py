#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
UiPath Docs MDX exporter + Sidebar/Metadata generator.

For every URL you input (docs.uipath.com OR docs-dev/docs-staging/preview-docs):
  - Converts the docs content to .md (Docusaurus-friendly MDX-compatible).
    Optionally crawls same-site pages.
  - Builds a Docusaurus-friendly sidebar JSON and a metadata JSON whose filenames
    are based on the second-to-last URL segment:
      <stem>-sidebar.json
      <stem>-metadata.json

Sidebar & metadata are saved under the <product>/<delivery>/<version> folder of the URL.
Examples:
  https://docs-dev.uipath.com/automation-ops/automation-suite/2024.10/user-guide/release-notes-2024-10-0
      -> automation-ops/automation-suite/2024.10/<stem>-sidebar.json
         automation-ops/automation-suite/2024.10/<stem>-metadata.json

Notes:
- Only docs-dev/docs-staging/preview-docs require Cloudflare Access/SSO.
- docs.uipath.com does NOT require Cloudflare and will never prompt for it.
- Playwright render fallback can be used for BOTH public and protected docs if SSR content is empty.
"""

import os
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
from bs4 import BeautifulSoup, NavigableString, Tag
import markdownify as md
import webbrowser

# =========================
# === GLOBAL SETTINGS   ===
# =========================

DEFAULT_USER_AGENT = "UiPathDocsScraper/1.1 (+https://uipath.com)"
GLOBAL_THROTTLE_SECONDS = 0.4  # polite delay between successful requests

# Track whether we've already prompted for protected-host login in this run
_DOCS_DEV_PROMPTED = False
GLOBAL_SESSION: requests.Session | None = None

# Hosts this script can scrape
DOCS_PROTECTED_HOSTS = {"docs-dev.uipath.com", "docs-staging.uipath.com", "preview-docs.uipath.com"}  # Cloudflare Access / SSO
DOCS_PUBLIC_HOSTS = {"docs.uipath.com"}  # no Cloudflare needed
DOCS_ALL_HOSTS = DOCS_PROTECTED_HOSTS | DOCS_PUBLIC_HOSTS

CLOUDFLARE_LOGIN_BASE = "https://uipath.cloudflareaccess.com/cdn-cgi/access/login"

# Global Playwright driver cache: (playwright, browser, context, page)
PLAYWRIGHT_DRIVER = None

# =========================
# === UTILS / HELPERS   ===
# =========================

def _match_docs_host(url: str) -> str | None:
    """Return the matching UiPath docs host for a URL, or None."""
    try:
        netloc = urllib.parse.urlparse(url).netloc.lower()
    except Exception:
        return None
    for h in DOCS_ALL_HOSTS:
        if netloc.endswith(h):
            return h
    return None


def _match_protected_docs_host(url: str) -> str | None:
    """Return matching protected host (docs-dev/docs-staging/preview-docs) or None."""
    try:
        netloc = urllib.parse.urlparse(url).netloc.lower()
    except Exception:
        return None
    for h in DOCS_PROTECTED_HOSTS:
        if netloc.endswith(h):
            return h
    return None


def _needs_cloudflare_access(url: str) -> bool:
    """True only for protected docs environments."""
    return _match_protected_docs_host(url) is not None


def _parse_cookie_string(cookie_string: str) -> Dict[str, str]:
    """Parse a simple 'k1=v1; k2=v2' cookie string into a dict."""
    jar: Dict[str, str] = {}
    if not cookie_string:
        return jar
    parts = [p.strip() for p in cookie_string.split(";") if p.strip()]
    for part in parts:
        if "=" in part:
            k, v = part.split("=", 1)
            jar[k.strip()] = v.strip()
    return jar


def _parse_retry_after(value: str) -> float:
    """Parse Retry-After header which may be seconds or HTTP-date; return seconds to wait."""
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


def looks_like_login_wall(html: str) -> bool:
    """
    Lightweight detection for an SSO/login page. This is a heuristic.
    """
    if not html:
        return False
    text = html.lower()
    cues = [
        "sign in", "log in", "login", "single sign-on", "sso",
        "continue with", "enter your email", "verify your identity"
    ]
    if 'id="DocContainer"' in text or "id='DocContainer'" in text:
        return False
    return any(cue in text for cue in cues)


def get_with_retries(
    url: str,
    session: Optional[requests.Session] = None,
    max_tries: int = 5,
    base_sleep: float = 1.0,
    timeout: int = 20,
    **request_kwargs,
) -> requests.Response:
    """
    GET with retries for 429 and 5xx, honoring Retry-After and using exponential backoff + jitter.
    Extra keyword args (like headers, params, etc.) are passed through to requests.Session.get.
    """
    s = session or requests.Session()
    headers = request_kwargs.pop("headers", None)
    if headers is None:
        headers = {"User-Agent": DEFAULT_USER_AGENT}

    tries = 0
    while True:
        tries += 1
        try:
            resp = s.get(url, headers=headers, timeout=timeout, **request_kwargs)
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


def sso_get_with_retries(
    url: str,
    session: Optional[requests.Session] = None,
    max_tries: int = 5,
    base_sleep: float = 1.0,
    timeout: int = 20,
    **request_kwargs,
) -> requests.Response:
    """Thin wrapper used by SSO-aware helpers. Just forwards to get_with_retries."""
    return get_with_retries(
        url,
        session=session,
        max_tries=max_tries,
        base_sleep=base_sleep,
        timeout=timeout,
        **request_kwargs,
    )


def configure_docs_dev_auth(session: requests.Session, host: Optional[str] = None) -> None:
    """
    Best-effort auth bootstrap for SSO-protected docs-dev/docs-staging pages.
    Looks for env vars:
      - DOCS_DEV_BEARER: a JWT or opaque token -> Authorization: Bearer <token>
      - DOCS_DEV_COOKIES: raw cookie string "k1=v1; k2=v2"
      - CLOUDFRONT_COOKIES: signed cookies string (Key-Pair-Id, Policy, Signature)

    No-op for docs.uipath.com.
    """
    host = host or "docs-dev.uipath.com"
    if host not in DOCS_PROTECTED_HOSTS:
        return  # public docs don't need auth bootstrap

    token = os.getenv("DOCS_DEV_BEARER")
    if token and "authorization" not in {k.lower() for k in session.headers}:
        session.headers["Authorization"] = f"Bearer {token}"

    raw = os.getenv("DOCS_DEV_COOKIES") or ""
    cf = os.getenv("CLOUDFRONT_COOKIES") or ""
    cookies = {}
    cookies.update(_parse_cookie_string(raw))
    cookies.update(_parse_cookie_string(cf))

    for k, v in cookies.items():
        session.cookies.set(k, v, domain=host)

    if "User-Agent" not in session.headers:
        session.headers["User-Agent"] = DEFAULT_USER_AGENT
    session.headers.setdefault(
        "Accept",
        "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
    )
    session.headers.setdefault("Accept-Language", "en-US,en;q=0.9")


def _detect_kid_from_cloudflare(target_url: str, session: requests.Session) -> Optional[str]:
    """
    Try to discover the Cloudflare Access KID automatically for PROTECTED hosts only.
    """
    host = _match_protected_docs_host(target_url)
    if not host:
        return None  # public docs do not use Cloudflare Access

    try:
        app_login = f"https://{host}/cdn-cgi/access/login?" + urllib.parse.urlencode(
            {"redirect_url": target_url}
        )
        r = session.get(app_login, allow_redirects=False, timeout=10)

        loc = r.headers.get("Location", "") or r.headers.get("location", "")
        if loc:
            try:
                parsed = urllib.parse.urlparse(loc)
                qs = urllib.parse.parse_qs(parsed.query)
                kid_vals = qs.get("kid") or []
                if kid_vals:
                    return kid_vals[0]
            except Exception:
                pass

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

    try:
        team_login_no_kid = CLOUDFLARE_LOGIN_BASE + "?" + urllib.parse.urlencode(
            {"redirect_url": target_url}
        )
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
######
def _install_fast_routes_sidebar(page) -> None:
    """
    Speed up sidebar rendering by aborting heavy resources.
    Keeps scripts/xhr so the sidebar React app can still render.
    """
    try:
        page.route(
            "**/*",
            lambda route: (
                route.abort()
                if route.request.resource_type in {"image", "media", "font"}
                else route.continue_()
            ),
        )
    except Exception:
        pass
######

def _get_sidebar_html_with_playwright(url: str, session: requests.Session | None = None) -> str | None:
    """
    Use the shared Playwright browser to get HTML with the *full* sidebar expanded:
      - navigate to the URL
      - expand all 'Expand ...' buttons
      - scroll the sidebar container to load any virtualized items
      - return page.content()
    """
    global PLAYWRIGHT_DRIVER

    try:
        from playwright.sync_api import sync_playwright
    except Exception as e:
        print(f"[Playwright][sidebar] Not available: {e}")
        return None

    try:
        # Start browser once, reuse
        if PLAYWRIGHT_DRIVER is None:
            pw = sync_playwright().start()
            browser = pw.chromium.launch(headless=True)
            context = browser.new_context()

            # Pull cookies from the requests session so we stay authenticated (protected hosts)
            if session is not None:
                cookies_to_add = []
                for c in session.cookies:
                    domain = c.domain or ""
                    if any(domain.endswith(h) for h in DOCS_PROTECTED_HOSTS) or domain.endswith(".uipath.com"):
                        cookies_to_add.append({
                            "name": c.name,
                            "value": c.value,
                            "domain": domain,
                            "path": c.path or "/",
                            "httpOnly": False,
                            "secure": False,
                            "sameSite": "Lax",
                        })
                if cookies_to_add:
                    context.add_cookies(cookies_to_add)

            page = context.new_page()
            
            # Speed knobs (only set once for the reused page)
            _install_fast_routes_sidebar(page)
            page.set_default_timeout(7000)
            page.set_default_navigation_timeout(15000)
            
            PLAYWRIGHT_DRIVER = (pw, browser, context, page)
        else:
            pw, browser, context, page = PLAYWRIGHT_DRIVER

        #print(f"[Playwright][sidebar] Rendering {url} ...")
        # Much faster than networkidle on modern docs sites
        page.goto(url, wait_until="domcontentloaded")
        

        # Wait until the sidebar root exists
        try:
            page.wait_for_selector("#SideBarMenu_Root", timeout=5000)
        except Exception:
            print("[Playwright][sidebar] No #SideBarMenu_Root found.")
            return page.content()

        # 1) Click all collapsed 'expand' buttons until no more
        for _ in range(10):  # safety cap
            buttons = page.query_selector_all("#SideBarMenu_Root button[aria-expanded='false']")
            if not buttons:
                break
            for b in buttons:
                try:
                    b.click()
                except Exception:
                    pass
            page.wait_for_timeout(75)

        # 2) Scroll sidebar container to force any virtualized items to render
        sidebar_selector_candidates = [
            "div.css-117a3kr >> #SideBarMenu_Root",
            "#SideBarMenu_Root",
        ]
        sidebar_handle = None
        for sel in sidebar_selector_candidates:
            try:
                sidebar_handle = page.query_selector(sel)
                if sidebar_handle:
                    break
            except Exception:
                continue

        if sidebar_handle:
            last_height = -1
            for _ in range(12):  # safety cap ###
                try:
                    page.evaluate("(el) => { el.scrollTop = el.scrollHeight; }", sidebar_handle)
                    page.wait_for_timeout(75)
                    height = page.evaluate("(el) => el.scrollHeight", sidebar_handle)
                    if height == last_height:
                        break
                    last_height = height
                except Exception:
                    break

        html = page.content()
        print("[Playwright][sidebar] Collected HTML with expanded sidebar.")
        return html

    except Exception as e:
        print(f"[Playwright][sidebar] Failed: {e}")
        return None


def _try_playwright_login(target_url: str, session: requests.Session) -> bool:
    """
    Attempt to complete SSO using a real browser via Playwright and import cookies
    into the provided requests session. Returns True if cookies were captured and set.
    Only relevant for protected hosts.
    """
    if not _needs_cloudflare_access(target_url):
        return False

    try:
        from playwright.sync_api import sync_playwright  # type: ignore
    except Exception as e:
        print("Playwright not available:", e)
        return False

    try:
        with sync_playwright() as p:
            browser = p.chromium.launch(headless=False)
            context = browser.new_context()
            page = context.new_page()

            page.goto(target_url)

            print("\nA browser window has opened to complete SSO.")
            print("1) Use the email login and enter your UiPath email, then click 'Send code'.")
            print("2) Wait to receive the login code from [EXTERNAL] Cloudflare Access login code.")
            print("3) Paste the code in the login window.")
            print("4) Make sure you land on the docs content.")
            input("Press ENTER here after you finish SSO in the browser... ")

            cookies = context.cookies()
            got_any = False
            for c in cookies:
                domain = c.get("domain") or ""
                for h in DOCS_PROTECTED_HOSTS:
                    if h in domain:
                        session.cookies.set(c["name"], c["value"], domain=h)
                        got_any = True
                        break

            try:
                browser.close()
            except Exception:
                pass

            if got_any:
                print("Imported authenticated cookies from Playwright into this session.")
            else:
                print("Didn't detect protected docs cookies from Playwright session.")
            return got_any
    except Exception as e:
        print("Playwright flow failed:", e)
        return False


def render_html_with_playwright(url: str, session: requests.Session | None = None) -> str | None:
    """
    Use Playwright to get the fully rendered HTML (including React content).
    Reuses a single browser/context/page across all calls in this process.

    Returns HTML string or None on failure.
    """
    global PLAYWRIGHT_DRIVER

    try:
        from playwright.sync_api import sync_playwright
    except Exception as e:
        print(f"[Playwright] Not available for rendering: {e}")
        return None

    try:
        # Lazily start Playwright & a browser only once
        if PLAYWRIGHT_DRIVER is None:
            pw = sync_playwright().start()
            browser = pw.chromium.launch(headless=True)
            context = browser.new_context()

            # Reuse cookies from requests session (Cloudflare / protected SSO), if present.
            if session is not None:
                cookies_to_add = []
                for c in session.cookies:
                    domain = c.domain or ""
                    if any(domain.endswith(h) for h in DOCS_PROTECTED_HOSTS) or domain.endswith(".uipath.com"):
                        cookies_to_add.append({
                            "name": c.name,
                            "value": c.value,
                            "domain": domain,
                            "path": c.path or "/",
                            "httpOnly": False,
                            "secure": False,
                            "sameSite": "Lax",
                        })
                if cookies_to_add:
                    context.add_cookies(cookies_to_add)

            page = context.new_page()
            # Speed optimizations
            _install_fast_routes(page)
            page.set_default_timeout(7000)
            page.set_default_navigation_timeout(15000)
            PLAYWRIGHT_DRIVER = (pw, browser, context, page)
        else:
            pw, browser, context, page = PLAYWRIGHT_DRIVER

        #print(f"[Playwright] Rendering {url} ...")
        # Faster than networkidle (network may never truly go idle on docs sites)
        page.goto(url, wait_until="domcontentloaded")
        # Wait for the content container we actually need
        # (DocContainer is what your parser uses when present)
        try:
            page.wait_for_selector("#DocContainer", timeout=5000)
        except Exception:
            # Fallback: still return the DOM we have
            pass
        return page.content()
###
    except Exception as e:
        print(f"[Playwright] Render failed: {e}")
        return None


import atexit

def _shutdown_playwright():
    global PLAYWRIGHT_DRIVER
    if PLAYWRIGHT_DRIVER is not None:
        pw, browser, context, page = PLAYWRIGHT_DRIVER
        try:
            browser.close()
        except Exception:
            pass
        try:
            pw.stop()
        except Exception:
            pass
        PLAYWRIGHT_DRIVER = None

atexit.register(_shutdown_playwright)


def prompt_for_docs_dev_login(target_url: str, session: requests.Session) -> None:
    """
    Interactive SSO bootstrap for PROTECTED hosts only:
      - tries Playwright-based browser login
      - then opens Cloudflare login URLs in your browser
      - waits for you to finish
    """
    global _DOCS_DEV_PROMPTED
    _DOCS_DEV_PROMPTED = True

    host = _match_protected_docs_host(target_url)
    if not host:
        return  # do not prompt for public docs

    parsed = urllib.parse.urlparse(target_url)
    if not parsed.netloc:
        return

    full_url = urllib.parse.urlunparse(parsed._replace())

    print("\nOpening Cloudflare Access login in your browser...")
    print("1) Use the email login and enter your UiPath email, then click 'Send code'.")
    print(f"2) Wait to receive the login code from [EXTERNAL] Cloudflare Access login code for {host}.")
    print("3) Paste the code in the login window.")
    print("4) Make sure you land on the docs content.")

    detected_kid = None
    try:
        detected_kid = _detect_kid_from_cloudflare(full_url, session=session)
        if detected_kid:
            print(f"[info] Detected Cloudflare Access KID: {detected_kid[:8]}…")
    except Exception:
        pass

    params = {"redirect_url": full_url}
    if detected_kid:
        params["kid"] = detected_kid
    team_login = CLOUDFLARE_LOGIN_BASE + "?" + urllib.parse.urlencode(params)
    app_login = f"https://{host}/cdn-cgi/access/login?" + urllib.parse.urlencode({"redirect_url": full_url})

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


def safe_get_html(url: str, session: requests.Session, **kw) -> requests.Response:
    """
    GET wrapper:
      - For protected hosts (docs-dev/docs-staging/preview): does SSO-aware retry + interactive fallback.
      - For public host (docs.uipath.com): normal retry, NO Cloudflare prompt.
    """
    resp = sso_get_with_retries(url, session=session, **kw)

    ct = resp.headers.get("Content-Type", "")
    looks_html = ("html" in ct) or (ct == "")

    if looks_html and _needs_cloudflare_access(url) and looks_like_login_wall(resp.text):
        host = _match_protected_docs_host(url)
        configure_docs_dev_auth(session, host=host)
        resp = sso_get_with_retries(url, session=session, **kw)

        ct2 = resp.headers.get("Content-Type", "")
        if ("html" in ct2 or ct2 == "") and looks_like_login_wall(resp.text):
            try:
                global _DOCS_DEV_PROMPTED
                if not _DOCS_DEV_PROMPTED:
                    prompt_for_docs_dev_login(url, session=session)
                    resp = sso_get_with_retries(url, session=session, **kw)
            except Exception:
                pass

    return resp


# =========================
# === CONTENT DETECTION ===
# =========================

def get_content_container(soup: BeautifulSoup) -> Optional[Tag]:
    """
    Try multiple fallbacks to find the main doc content.
    1) div#DocContainer (old layout)
    2) <main> tag
    3) common doc-ish IDs/classes
    4) <body> as last resort
    """
    doc = soup.find("div", id="DocContainer")
    if doc:
        return doc

    main = soup.find("main")
    if main:
        return main

    candidates = [
        soup.find("div", id="docs-container"),
        soup.find("div", id="content"),
        soup.find("div", class_="DocContainer"),
        soup.find("div", class_="doc-container"),
        soup.find("div", class_="doc-content"),
    ]
    for c in candidates:
        if c:
            return c

    if soup.body:
        return soup.body

    return None


# =========================
# === HTML -> MDX CORE  ===
# =========================

_PLACEHOLDER_RE = re.compile(r"{{[^}]*}}")
BARE_AUTOLINK_RE = re.compile(r"<(https?://[^>\s]+)>")

def unescape_md_in_placeholders(md_text: str) -> str:
    """Undo escapes like \\_ \\{ \\} inside {{...}} only."""
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
    """
    for table in list(container.find_all("table")):
        if _is_complex_table(table):
            continue
        for img in list(table.find_all("img")):
            alt = (img.get("alt") or "").strip()
            src = (img.get("src") or "").strip()
            if not src:
                replacement = NavigableString(f"[image]{f'({alt})' if alt else ''}")
            else:
                safe_alt = alt.replace("|", r"\|")
                replacement = NavigableString(f"![{safe_alt}]({src})")
            img.replace_with(replacement)


def convert_html_imgs_in_md_tables(markdown_text: str) -> str:
    """
    If any <img ...> leaked into Markdown tables, convert them to ![alt](src).
    Only touches lines that look like Markdown table rows (start with '|').
    """
    def _img_to_md(html_img: str) -> str:
        alt = ""
        src = ""
        m = re.search(r'alt="([^"]*)"', html_img, flags=re.IGNORECASE)
        if m:
            alt = m.group(1)
        m = re.search(r'src="([^"]+)"', html_img, flags=re.IGNORECASE)
        if m:
            src = m.group(1)
        if src:
            return f"![{alt.replace('|', r'\\|')}]({src})"
        return f"[image]{f'({alt})' if alt else ''}"

    def _convert_line(line: str) -> str:
        if not line.strip().startswith("|"):
            return line
        return re.sub(r"<img\b[^>]*>", lambda m: _img_to_md(m.group(0)), line, flags=re.IGNORECASE)

    return "\n".join(_convert_line(ln) for ln in markdown_text.splitlines())


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
        "strong": set(), "em": set(), "code": set(), "pre": set(), "sup": set(), "sub": set(),
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


def extract_complex_tables(container: BeautifulSoup) -> Dict[str, str]:
    """Replace complex tables with placeholders and return {placeholder: sanitized_table_html}."""
    table_html_map: Dict[str, str] = {}
    counter = 1
    for table in list(container.find_all("table")):
        if not _is_complex_table(table):
            continue
        placeholder = f"HTMLTABLEPLACEHOLDER{counter}"
        counter += 1
        raw_html = str(table)
        clean_html = sanitize_table_html(raw_html)
        table_html_map[placeholder] = clean_html
        table.replace_with(NavigableString(placeholder))
    return table_html_map


def normalize_paragraphs(container: BeautifulSoup) -> None:
    """
    Clean <p> blocks that are not complex containers.
    """
    for br in list(container.find_all("br")):
        br.decompose()

    for p in list(container.find_all("p")):
        if _in_itemgroup_info(p):
            continue
        if p.find(["pre", "code", "table", "ul", "ol"]) is not None:
            continue

        for node in list(p.descendants):
            if isinstance(node, NavigableString):
                s = str(node).replace("\xa0", " ")
                s = re.sub(r"\s+", " ", s)
                node.replace_with(s)

        html = str(p)
        html = re.sub(r"\s+([,.;:!?])", r"\1", html)
        html = re.sub(r"\s+(\))", r"\1", html)
        html = re.sub(r"(\()\s+", r"\1", html)
        html = re.sub(r">\s+<", "> <", html)
        html = re.sub(r"\s{2,}", " ", html).strip()
        p.replace_with(BeautifulSoup(html, "html.parser"))


def protect_sup_tags(container: BeautifulSoup, prefix: str = "SUPTAGPLACEHOLDER") -> Dict[str, str]:
    """
    Replace <sup>...</sup> with placeholders. Normalize them so restored
    HTML is always <sup>...</sup> (no attributes).
    """
    mapping: Dict[str, str] = {}
    counter = 1
    for sup in list(container.find_all("sup")):
        placeholder = f"{prefix}{counter}"
        counter += 1
        clean_sup = BeautifulSoup("<sup></sup>", "html.parser").sup
        clean_sup.string = sup.get_text()
        mapping[placeholder] = str(clean_sup)
        sup.replace_with(NavigableString(placeholder))
    return mapping


def restore_sup_placeholders(md_text: str, mapping: Dict[str, str]) -> str:
    if not mapping:
        return md_text
    for ph, html in mapping.items():
        md_text = md_text.replace(ph, html)
    return md_text


def remove_leading_h2(md_text: str) -> str:
    """
    Remove the very first '## ...' heading at the start of the Markdown content.
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


def remove_empty_tags(container: BeautifulSoup) -> None:
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


def unwrap_bare_autolinks(md_text: str) -> str:
    """Turn <https://example.com> into https://example.com."""
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
        if isinstance(sib, Tag) and sib.name == "div" and "note" in (sib.get("class") or []):
            break
        if isinstance(sib, Tag) and sib.name in {"ul", "ol", "table", "pre", "blockquote", "hr"}:
            break

        if isinstance(sib, NavigableString):
            if str(sib).strip():
                p = div.new_tag("p")
                p.string = str(sib)
                div.append(p)
            sib.extract()
            continue

        if isinstance(sib, Tag) and (is_inlineish(sib) or sib.name in {"p"}):
            div.append(sib.extract())
            continue

        break


def _dedent_admonition_content(s: str) -> str:
    lines = s.splitlines()
    while lines and not lines[0].strip():
        lines.pop(0)
    while lines and not lines[-1].strip():
        lines.pop()
    if not lines:
        return ""
    indents = []
    for ln in lines:
        if ln.strip():
            m = re.match(r'^[ \t]*', ln)
            indents.append(len(m.group(0)) if m else 0)
    common = min(indents) if indents else 0
    if common:
        pad = " " * common
        lines = [ln[common:] if ln.startswith(pad) else ln for ln in lines]
    return "\n".join(lines)


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

        _absorb_following_into_note_if_empty(div)

        inner_html = "".join(str(child) for child in div.contents)
        inner_soup = BeautifulSoup(inner_html, "html.parser")

        _remove_notetitle_nodes(inner_soup)
        _strip_leading_note_title(inner_soup)

        sup_map = protect_sup_tags(inner_soup, prefix="ADMSUPPLACEHOLDER")
        inner_md = md.markdownify(str(inner_soup), heading_style="ATX").strip()
        inner_md = _strip_leading_note_title_from_md(inner_md)
        inner_md = unescape_md_in_placeholders(inner_md)
        inner_md = restore_sup_placeholders(inner_md, sup_map)

        inner_md = _dedent_admonition_content(inner_md)
        block = f":::{admonition}\n{inner_md}\n:::"

        if div.find_parent("li") is not None:
            admonition_block = block
        else:
            admonition_block = f"\n{block}"

        div.replace_with(NavigableString(admonition_block))


def escape_angle_brackets_plain_text(container: BeautifulSoup) -> None:
    """
    HTML stage: escape '<' and '>' in *text nodes only*.
    Skips text inside <code>, <pre>, <script>, <style>.
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


def ignore_material_icons(container: BeautifulSoup) -> None:
    """
    Remove <span class="material-icons ...">...</span> entirely.
    """
    for sp in list(container.find_all("span", class_=True)):
        classes = " ".join(sp.get("class") or [])
        if "material-icons" in classes:
            sp.decompose()


def flatten_note_spans(container: BeautifulSoup) -> None:
    for sp in list(container.find_all("span")):
        if not sp.attrs:
            sp.unwrap()


# ===== LIST / ADMONITION / IMAGE POST-PROCESSORS (unchanged) =====

def unwrap_markdown_paragraphs_and_lists(md_text: str) -> str:
    lines = md_text.splitlines()
    new_lines: List[str] = []
    buffer: List[str] = []
    inside_codeblock = False
    inside_table = False
    inside_admonition = False

    list_prefix = re.compile(r'^(\s*)([-*+]|\d+\.)\s+')
    table_line = re.compile(r'^\s*\|')
    table_divider = re.compile(r'^\s*[:\-| ]+$')

    code_fence_re = re.compile(r'^\s*(```|~~~)')
    fence_open_re = re.compile(r'^\s*:::\w+\s*$')
    fence_close_re = re.compile(r'^\s*:::\s*$')

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
        merged = " ".join(line.rstrip() for line in buffer).strip()
        merged = re.sub(r"\s{2,}", " ", merged)
        new_lines.append(indent + merged)
        buffer.clear()

    for line in lines:
        stripped = line.strip()

        if code_fence_re.match(line):
            flush_buffer()
            new_lines.append(line)
            inside_codeblock = not inside_codeblock
            continue

        if inside_codeblock:
            new_lines.append(line)
            continue

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

        if not stripped:
            flush_buffer()
            inside_table = False
            new_lines.append("")
            continue

        if stripped.startswith("#"):
            flush_buffer()
            inside_table = False
            new_lines.append(stripped)
            continue

        if stripped.startswith(":::"):
            flush_buffer()
            inside_table = False
            new_lines.append(line)
            continue

        if table_line.match(line) or (inside_table and (table_line.match(line) or table_divider.match(stripped))):
            flush_buffer()
            inside_table = True
            new_lines.append(line)
            continue

        if list_prefix.match(line):
            flush_buffer()
            inside_table = False
            buffer.append(line)
            continue

        if html_block_re.match(line) or html_close_re.match(line):
            flush_buffer()
            inside_table = False
            new_lines.append(line)
            continue

        buffer.append(line)

    flush_buffer()
    return "\n".join(new_lines)


def collapse_soft_wraps_inside_admonitions(md_text: str) -> str:
    lines = md_text.splitlines()
    out: List[str] = []

    fence_open_re = re.compile(r'^\s*:::\w+\s*$')
    fence_close_re = re.compile(r'^\s*:::\s*$')
    code_fence_re = re.compile(r'^\s*(```|~~~)')
    list_head_re = re.compile(r'^\s*([-*+]|[0-9]+\.)\s+')
    table_line_re = re.compile(r'^\s*\|')
    table_div_re = re.compile(r'^\s*[:\-| ]+$')

    inside_admon = False
    inside_code = False
    para_buf: List[str] = []

    def flush_paragraph():
        nonlocal para_buf
        if para_buf:
            first = para_buf[0]
            leading_ws = re.match(r'^[ \t]*', first).group(0)
            joined = " ".join([first.strip(), *[ln.strip() for ln in para_buf[1:]]]).strip()
            out.append(leading_ws + joined)
            para_buf = []

    i = 0
    n = len(lines)
    while i < n:
        line = lines[i]

        if not inside_admon:
            out.append(line)
            if fence_open_re.match(line):
                inside_admon = True
            i += 1
            continue

        if fence_close_re.match(line) and not inside_code:
            flush_paragraph()
            out.append(line)
            inside_admon = False
            i += 1
            continue

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

        if not line.strip():
            flush_paragraph()
            out.append(line)
            i += 1
            continue

        if list_head_re.match(line) or table_line_re.match(line) or table_div_re.match(line):
            flush_paragraph()
            out.append(line)
            i += 1
            continue

        para_buf.append(line)
        i += 1

    flush_paragraph()
    return "\n".join(out)


def clean_admonition_lists(md_text: str) -> str:
    lines = md_text.splitlines()
    out: List[str] = []
    inside_admon = False
    inside_code = False

    fence_open_re = re.compile(r'^\s*:::\w+\s*$')
    fence_close_re = re.compile(r'^\s*:::\s*$')
    code_fence_re = re.compile(r'^\s*(```|~~~)')
    assignment_line_re = re.compile(r'^\s*[+*-]\s*assignment\s*$', re.I)

    for line in lines:
        if fence_open_re.match(line):
            inside_admon = True
            out.append(line)
            continue
        if fence_close_re.match(line):
            inside_admon = False
            out.append(line)
            continue

        if code_fence_re.match(line):
            out.append(line)
            inside_code = not inside_code
            continue

        if inside_code:
            out.append(line)
            continue

        if inside_admon and assignment_line_re.match(line):
            continue

        out.append(line)

    return "\n".join(out)


def collapse_leading_newlines_before_images_in_lists(md_text: str) -> str:
    pattern1 = re.compile(r'(?m)^(?P<head>(?P<indent>\s*)(?:[-*+]|\d+\.)[^\n]*?)\n\n(?=(?P=indent)!\[)')
    md_text = pattern1.sub(r'\g<head>\n', md_text)
    pattern2 = re.compile(r'(?m)^(?P<head>(?P<indent>\s{2,})(?!#|```|~~~).+?)\n\n(?=(?P=indent)!\[)')
    md_text = pattern2.sub(r'\g<head>\n', md_text)
    return md_text


def collapse_blank_lines_before_codeblocks_in_lists(md_text: str) -> str:
    pat_head = re.compile(
        r'(?m)'
        r'^(?P<head>(?P<indent>\s*)(?:[-*+]|\d+\.)[^\n]*?)'
        r'\n{2,}'
        r'(?=(?P=indent)[ \t]*(?:```|~~~))'
    )

    pat_cont = re.compile(
        r'(?m)'
        r'^(?P<head>(?P<indent>\s{2,})(?!#|```|~~~).+?)'
        r'\n{2,}'
        r'(?=(?P=indent)[ \t]*(?:```|~~~))'
    )

    prev = None
    out = md_text
    while out != prev:
        prev = out
        out = pat_head.sub(r'\g<head>\n', out)
        out = pat_cont.sub(r'\g<head>\n', out)

    return out


def collapse_blank_lines_before_notes_in_lists(md_text: str) -> str:
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
    lines = md_text.splitlines()
    out: List[str] = []
    i, n = 0, len(lines)

    list_head_re = re.compile(r'^(\s*)([-*+]|\d+\.)\s+(.*\S.*)$')
    code_fence_re = re.compile(r'^\s*(```|~~~)')

    inside_code = False

    while i < n:
        line = lines[i]

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

        base_indent, marker, _ = m.groups()
        cont_indent = base_indent + (" " * (len(marker) + 1))

        out.append(line)
        i += 1

        while i < n:
            nxt = lines[i]

            if code_fence_re.match(nxt):
                break

            if re.match(rf'^{re.escape(base_indent)}([-*+]|\d+\.)\s+', nxt):
                break

            if nxt.strip() and len(nxt) - len(nxt.lstrip(" ")) < len(base_indent):
                break

            if not nxt.strip():
                if (i + 1 < n) and re.match(rf'^{re.escape(base_indent)}!\[', lines[i + 1]):
                    i += 1
                    nxt = lines[i]
                else:
                    out.append(nxt)
                    i += 1
                    continue

            if re.match(rf'^{re.escape(base_indent)}!\[', nxt):
                out.append(re.sub(rf'^{re.escape(base_indent)}', cont_indent, nxt, count=1))
                i += 1
                continue

            out.append(nxt)
            i += 1

    return "\n".join(out)


def indent_notes_like_list_content(md_text: str) -> str:
    lines = md_text.splitlines()
    out: List[str] = []
    i, n = 0, len(lines)

    list_head_re = re.compile(r'^(\s*)([-*+]|\d+\.)\s+(.*\S.*)$')
    fence_open_re = re.compile(r'^\s*:::\w+\s*$')
    fence_close_re = re.compile(r'^\s*:::\s*$')
    code_fence_re = re.compile(r'^\s*(```|~~~)')

    inside_code = False

    while i < n:
        line = lines[i]

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

        base_indent, marker, _ = m.groups()
        cont_indent = base_indent + (" " * (len(marker) + 1))

        out.append(line)
        i += 1

        if i < n and not lines[i].strip():
            if i + 1 < n and fence_open_re.match(lines[i + 1]) and lines[i + 1].startswith(base_indent):
                i += 1

        if i < n and fence_open_re.match(lines[i]) and lines[i].startswith(base_indent):
            block: List[str] = []
            while i < n:
                cur = lines[i]
                block.append(cur)
                i += 1
                if fence_close_re.match(cur):
                    break

            stripped = [re.sub(rf'^{re.escape(base_indent)}', '', b, count=1) for b in block]
            reindented = [cont_indent + b for b in stripped]
            out.extend(reindented)
            continue

        while i < n:
            nxt = lines[i]
            if re.match(rf'^{re.escape(base_indent)}([-*+]|\d+\.)\s+', nxt):
                break
            if code_fence_re.match(nxt):
                break
            out.append(nxt)
            i += 1

    return "\n".join(out)


def move_inline_admonitions_to_own_line(md_text: str) -> str:
    ADMO = r'(?:note|tip|warning|info|important|caution|danger)'

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
        result.append(f"{base}{fence}")
        if after:
            result.append(f"{base}{after}")
        return "\n".join(result)

    return pattern_inline_list.sub(_split_list_inline, md_text)


def hoist_trailing_admonition_after_sublist(md_text: str) -> str:
    md_text = md_text.replace('\t', '    ')

    fence_open_re = re.compile(r'^(\s*):::(note|tip|warning|danger|info|important|caution)\s*$', re.M)
    fence_close_re = re.compile(r'^(\s*):::\s*$', re.M)
    list_head_re = re.compile(r'^(\s*)([-*+]|\d+\.)\s', re.M)

    lines = md_text.splitlines()
    out: List[str] = []
    i, n = 0, len(lines)

    def leading_spaces(s: str) -> int:
        return len(s) - len(s.lstrip(' '))

    while i < n:
        m_open = fence_open_re.match(lines[i])
        if not m_open:
            out.append(lines[i])
            i += 1
            continue

        fence_indent = m_open.group(1)
        j = i + 1
        while j < n and not fence_close_re.match(lines[j]):
            j += 1
        if j < n:
            j += 1

        block = lines[i:j]

        k = len(out) - 1
        while k >= 0 and not out[k].strip():
            k -= 1

        parent_cont_indent = None
        if k >= 0:
            m_parent = list_head_re.match(out[k])
            if m_parent:
                base_indent, marker = m_parent.group(1), m_parent.group(2)
                parent_cont_indent = base_indent + (" " * (len(marker) + 1))

        t = j
        while t < n and not lines[t].strip():
            t += 1
        end_of_sublist = (t >= n) or (leading_spaces(lines[t]) < len(fence_indent))

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
    pat_after_head = re.compile(
        r'(?m)'
        r'^(?P<head>(?P<base>\s*)(?:[-*+]|\d+\.)[^\n]*?)'
        r'\n{2,}'
        r'(?=(?P=base)[ \t]{2,}(?:[-*+]|\d+\.)\s+)'
    )
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
    pat_head_to_head = re.compile(
        r'(?m)'
        r'^(?P<first>(?P<base>\s*)(?:[-*+]|\d+\.)[^\n]*?)'
        r'\n{2,}'
        r'(?=(?P=base)(?:[-*+]|\d+\.)\s+)'
    )
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


def strip_paragraphs_in_lists(container: BeautifulSoup) -> None:
    """
    Normalize list markup inside list items.
    """
    if not container:
        return

    for lst in list(container.find_all(["ul", "ol"])):
        for pnode in list(lst.find_all("p", recursive=False)):
            if _in_itemgroup_info(pnode):
                continue
            if not pnode.get_text(strip=True):
                pnode.decompose()
            else:
                pnode.unwrap()

        for li in list(lst.find_all("li")):
            for wrapper_name in ("div", "span"):
                for w in list(li.find_all(wrapper_name, recursive=False)):
                    if _in_itemgroup_info(w):
                        continue
                    if w.attrs and not set(w.attrs.keys()).issubset({"class", "id"}):
                        continue
                    tag_children = [c for c in w.contents if isinstance(c, Tag)]
                    text_has_non_ws = any(isinstance(c, NavigableString) and c.strip() for c in w.contents)
                    if len(tag_children) == 1 and tag_children[0].name == "p" and not text_has_non_ws:
                        if _in_itemgroup_info(tag_children[0]):
                            continue
                        w.unwrap()

            for pnode in list(li.find_all("p")):
                if _in_itemgroup_info(pnode):
                    continue
                if not pnode.get_text(strip=True):
                    pnode.decompose()
                else:
                    pnode.unwrap()

            for d in list(li.find_all("div", recursive=False)):
                if _in_itemgroup_info(d):
                    continue
                classes = set(d.get("class") or [])
                if {"note", "warning", "important", "information", "tip", "danger"} & classes:
                    continue
                if (d.get("id") or "").lower().startswith("admonition"):
                    continue

                if d.find(["ul", "ol"], recursive=False):
                    d.unwrap()
                    continue

                nxt = d.find_next_sibling()
                is_list_sibling = (
                    nxt is not None and (
                        nxt.name in {"ul", "ol"} or
                        (nxt.name == "div" and nxt.find(["ul", "ol"], recursive=False))
                    )
                )
                if is_list_sibling:
                    if d.get_text(strip=True):
                        d.unwrap()
                    else:
                        d.decompose()
                    continue

            for wrapper_name in ("div", "span"):
                for w in list(li.find_all(wrapper_name)):
                    if _in_itemgroup_info(w):
                        continue
                    if w.find(["ul", "ol", "table", "pre", "code", "img"]):
                        continue
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
    Promote all ATX headings by one level: ### -> ##, #### -> ###, etc.
    Leaves top-level '#' unchanged.
    """
    lines = md_text.splitlines()
    new_lines = []
    for line in lines:
        if line.lstrip().startswith("#"):
            parts = line.split(" ", 1)
            hashes = parts[0]
            rest = parts[1] if len(parts) > 1 else ""
            if len(hashes) > 1:
                hashes = hashes[:-1]
            new_lines.append(hashes + (" " + rest if rest else ""))
        else:
            new_lines.append(line)
    return "\n".join(new_lines)


def get_doc_container_with_fallback(url: str, session: requests.Session) -> tuple[Optional[Tag], BeautifulSoup]:
    """
    1) Fetch via requests + safe_get_html.
    2) Try get_content_container; if it's empty, fall back to Playwright rendering (public or protected).
    Returns (doc_container, soup).
    """
    resp = safe_get_html(url, session=session)
    soup = BeautifulSoup(resp.content, "html.parser")
    doc_container = get_content_container(soup)

    if doc_container and doc_container.get_text(strip=True):
        return doc_container, soup

    # If this is any UiPath docs host and content is empty, try JS rendering
    if _match_docs_host(url):
        rendered_html = render_html_with_playwright(url, session=session)
        if rendered_html:
            soup_pw = BeautifulSoup(rendered_html, "html.parser")
            doc_container_pw = get_content_container(soup_pw)
            if doc_container_pw and doc_container_pw.get_text(strip=True):
                #print("[info] Using Playwright-rendered HTML for content.")
                return doc_container_pw, soup_pw

    return doc_container, soup
######
def canonicalize_url(u: str) -> str:
    """
    Normalize URL for crawling:
    - drop #fragment so anchored URLs don't get crawled as separate pages
    """
    if not u:
        return u
    u = u.strip()
    u, _frag = urllib.parse.urldefrag(u)  # <-- removes anything after '#'
    return u
    
def _install_fast_routes(page) -> None:
    """
    Abort resources we don't need for HTML extraction.
    This is the biggest speed win on docs sites.
    """
    try:
        page.route(
            "**/*",
            lambda route: (
                route.abort()
                if route.request.resource_type in {"image", "media", "font"}
                else route.continue_()
            ),
        )
        # CSS can be optional; keep it if you see layout-dependent selectors failing.
        page.route(
            "**/*",
            lambda route: (
                route.abort()
                if route.request.resource_type in {"stylesheet"}
                else route.continue_()
            ),
        )
    except Exception:
        # Routing can fail in some edge cases; don't crash the run.
        pass

######

def html_to_markdown_github(url, position_counter=None, crawl=True):
    """Convert page(s) to Markdown with frontmatter and write .md files."""
    try:
        global GLOBAL_SESSION
        if GLOBAL_SESSION is None:
            GLOBAL_SESSION = requests.Session()

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
        session = GLOBAL_SESSION
        skipped_urls = []

        while queue:
            current_url = canonicalize_url(queue.pop(0))
            if current_url in visited_urls:
                continue
            visited_urls.add(current_url)

            try:
                doc_container, soup = get_doc_container_with_fallback(current_url, session)

                if not doc_container or not doc_container.get_text(strip=True):
                    print(f"⚠️  No usable content found in DocContainer/main/body for: {current_url}")
                    markdown_content = ""
                else:
                    for anchor in doc_container.find_all("a", href=re.compile("^#")):
                        anchor.decompose()
                    remove_empty_tags(doc_container)
                    flatten_note_spans(doc_container)

                    # Prevent duplicate code blocks
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

                if not markdown_content.strip():
                    print(f"⚠️  Generated empty Markdown body (frontmatter only) for: {current_url}")

                with open(output_path, "w", encoding="utf-8") as f:
                    f.write(full_markdown_content)
                print(f"📝 Saved MD: {output_path}")

                if crawl:
                    for link in soup.find_all("a", href=True):
                        href = link["href"]
                        
                        # Skip pure in-page anchors and mailto early
                        if href.startswith("#") or href.startswith("mailto:"):
                            continue
                        
                        # Make absolute, then drop any #fragment
                        absolute_url = urllib.parse.urljoin(current_url, href)
                        absolute_url = canonicalize_url(absolute_url)
                        
                        # Only crawl within this guide's base_url scope
                        if absolute_url.startswith(base_url) and absolute_url not in visited_urls:
                            queue.append(absolute_url)
                            
###

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
# === SIDEBAR / METADATA      ===
# ===============================

HREF_MIN_DEPTH = 2
_SLUG_SAFE = re.compile(r"[^a-z0-9\-]+")
ICON_CLASS_HINT = re.compile(r"(icon|chevron|toggle|caret|expand)", re.I)

BANNED_TAGS = {"style", "script", "noscript", "link", "meta", "button", "svg", "path"}

CSS_CLASS_BLOCK = re.compile(r"\.[A-Za-z0-9_-]+\s*\{[^}]*\}")
CSS_ID_BLOCK = re.compile(r"#[A-Za-z0-9_-]+\s*\{[^}]*\}")
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
    """Resolve <a href> to absolute URL, then return site-absolute path with .md."""
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
    """
    Build the sidebar JSON from the docs page.

    For protected hosts we may need JS to render the real sidebar,
    so we:
      1) try safe_get_html (handles SSO if needed)
      2) if no sidebar <ul> found, fall back to Playwright-rendered HTML
         with all sidebar sections expanded and scrolled.
    """
    global GLOBAL_SESSION
    if GLOBAL_SESSION is None:
        GLOBAL_SESSION = requests.Session()

    headers = {"User-Agent": "SidebarScraper/1.6 (+https://example.local)"}
    resp = safe_get_html(url, session=GLOBAL_SESSION, headers=headers, timeout=30)
    resp.raise_for_status()
    soup = BeautifulSoup(resp.text, "html.parser")

    for tname in list(BANNED_TAGS):
        for t in soup.find_all(tname):
            t.decompose()

    root = pick_sidebar_root(soup)

    if root is None:
        print("[sidebar] No sidebar <ul> found in raw HTML; trying Playwright…")
        html_pw = _get_sidebar_html_with_playwright(url, session=GLOBAL_SESSION)
        if html_pw:
            soup_pw = BeautifulSoup(html_pw, "html.parser")
            for tname in list(BANNED_TAGS):
                for t in soup_pw.find_all(tname):
                    t.decompose()
            root = pick_sidebar_root(soup_pw)

    if not root:
        raise RuntimeError("Could not locate a sidebar <ul> in this page.")

    guide_title = derive_guide_name_from_slug(url)
    page_dir = path_dirname(urllib.parse.urlparse(url).path or "/")
    children = ul_to_items(root, base_url=url, depth=1, parent_dir=page_dir, page_dir=page_dir)

    return {"title": guide_title, "children": children}


def version_folder_from_url(url: str) -> str:
    """Return local folder path '<product>/<delivery>/<version>' from a docs URL."""
    segs = _segments(url)
    if len(segs) >= 3:
        return os.path.join(segs[0], segs[1], segs[2])
    return os.path.join(*segs[:3]) if segs else "."


def write_sidebar_and_metadata(url: str) -> None:
    sidebar_rooted = build_sidebar_from_url(url)
    stem = filename_stem_from_url(url)
    metadata = derive_metadata_from_url(url)

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

def main() -> None:
    parser = argparse.ArgumentParser(
        description="UiPath Docs HTML -> MD converter + sidebar/metadata generator (public + protected hosts)."
    )
    parser.add_argument(
        "--op",
        action="store_true",
        help="One-page mode: convert only the provided URL without crawling in-site links.",
    )
    args = parser.parse_args()

    position_tracking: Dict[str, int] = {}
    mode_label = "ONE-PAGE" if args.op else "CRAWL"
    print(f"▶ Running in {mode_label} mode (docs.uipath.com + docs-dev/docs-staging/preview-docs).")

    while True:
        target_url = input("Enter the URL of the starting HTML page (or press Enter to quit): ").strip()
        if not target_url:
            print("No URL entered. Exiting.")
            break
        
        start_time = time.perf_counter()

        html_to_markdown_github(target_url, position_tracking, crawl=(not args.op))

        print(f"✅ Conversion completed for: {target_url}")

        try:
            write_sidebar_and_metadata(target_url)
        except Exception as e:
            print(f"❌ Sidebar/metadata generation failed: {e}")
        
        end_time = time.perf_counter()
        elapsed = end_time - start_time
        print(f"⏱️ Total processing time: {elapsed:.2f} seconds")


        print("-" * 72)


if __name__ == "__main__":
    main()
