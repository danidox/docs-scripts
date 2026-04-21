#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Dev entry point for protected docs environments.

md_maker.py owns shared conversion/rendering logic.
This wrapper owns Cloudflare Access and Playwright login state for docs-dev,
docs-staging, and preview-docs.
"""

from __future__ import annotations

import importlib.util
import json
import os
import shutil
import sys
import time
import urllib.parse
import webbrowser
from functools import lru_cache
from pathlib import Path
from types import ModuleType
from typing import Optional

import requests


SCRIPT_DIR = Path(__file__).resolve().parent
DELEGATE_PATH = SCRIPT_DIR / "md_maker.py"
SESSION_FILE = SCRIPT_DIR / "auth-session.json"
EXPIRED_SESSION_FILE = SCRIPT_DIR / "auth-session-expired.json"
CLOUDFLARE_LOGIN_BASE = "https://uipath.cloudflareaccess.com/cdn-cgi/access/login"
CLOUDFLARE_ACCESS_HOST = "uipath.cloudflareaccess.com"
_DOCS_DEV_PROMPTED = False


def _cookie_domain_matches(domain: str, hosts: set[str]) -> bool:
    domain = (domain or "").lstrip(".").lower()
    return any(domain == host or domain.endswith(f".{host}") for host in hosts)


def _parse_cookie_string(cookie_string: str) -> dict[str, str]:
    jar: dict[str, str] = {}
    if not cookie_string:
        return jar
    parts = [p.strip() for p in cookie_string.split(";") if p.strip()]
    for part in parts:
        if "=" in part:
            k, v = part.split("=", 1)
            jar[k.strip()] = v.strip()
    return jar


@lru_cache(maxsize=1)
def _load_delegate() -> ModuleType:
    spec = importlib.util.spec_from_file_location("md_maker_delegate", DELEGATE_PATH)
    if spec is None or spec.loader is None:
        raise RuntimeError(f"Could not load delegate script: {DELEGATE_PATH}")

    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    _install_dev_auth_hooks(module)
    return module


def _auth_hosts(module: ModuleType) -> set[str]:
    return set(module.DOCS_PROTECTED_HOSTS) | {CLOUDFLARE_ACCESS_HOST}


def _needs_cloudflare_access(module: ModuleType, url: str) -> bool:
    return module._match_protected_docs_host(url) is not None


def load_saved_session_state(module: ModuleType) -> Optional[dict]:
    if not SESSION_FILE.exists():
        return None
    try:
        data = json.loads(SESSION_FILE.read_text(encoding="utf-8"))
    except Exception:
        return None

    cookies = data.get("cookies") or []
    valid = any(
        (cookie.get("name") in {"CF_AppSession", "CF_Authorization"})
        and _cookie_domain_matches(cookie.get("domain") or "", _auth_hosts(module))
        for cookie in cookies
    )
    return data if valid else None


def save_session_state(storage_state: dict) -> None:
    try:
        SESSION_FILE.write_text(json.dumps(storage_state, indent=2), encoding="utf-8")
        print("  Saved authenticated session to auth-session.json")
    except Exception as e:
        print(f"  Could not save auth-session.json: {e}")


def invalidate_saved_session() -> None:
    if not SESSION_FILE.exists():
        return
    try:
        shutil.copyfile(SESSION_FILE, EXPIRED_SESSION_FILE)
    except Exception:
        pass
    try:
        SESSION_FILE.unlink()
    except Exception:
        pass
    print("  [warn] Session invalidated (backed up to auth-session-expired.json).")


def apply_storage_state_to_session(module: ModuleType, session: requests.Session, storage_state: Optional[dict]) -> bool:
    host_matched = False
    if not storage_state:
        return host_matched
    for cookie in storage_state.get("cookies") or []:
        domain = cookie.get("domain") or ""
        if not _cookie_domain_matches(domain, _auth_hosts(module)):
            continue
        session.cookies.set(
            cookie.get("name", ""),
            cookie.get("value", ""),
            domain=domain,
            path=cookie.get("path") or "/",
        )
        host_matched = True
    return host_matched


def configure_docs_dev_auth(module: ModuleType, session: requests.Session, url: str) -> None:
    host = module._match_protected_docs_host(url)
    if not host:
        return

    apply_storage_state_to_session(module, session, load_saved_session_state(module))

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
        session.headers["User-Agent"] = module.DEFAULT_USER_AGENT
    session.headers.setdefault(
        "Accept",
        "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
    )
    session.headers.setdefault("Accept-Language", "en-US,en;q=0.9")


def _detect_kid_from_cloudflare(module: ModuleType, target_url: str, session: requests.Session) -> Optional[str]:
    host = module._match_protected_docs_host(target_url)
    if not host:
        return None

    try:
        app_login = f"https://{host}/cdn-cgi/access/login?" + urllib.parse.urlencode(
            {"redirect_url": target_url}
        )
        r = session.get(app_login, allow_redirects=False, timeout=10)

        loc = r.headers.get("Location", "") or r.headers.get("location", "")
        if loc:
            parsed = urllib.parse.urlparse(loc)
            qs = urllib.parse.parse_qs(parsed.query)
            kid_vals = qs.get("kid") or []
            if kid_vals:
                return kid_vals[0]

        if r.is_redirect or r.status_code in (301, 302, 303, 307, 308):
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


def _try_playwright_login(module: ModuleType, target_url: str, session: requests.Session) -> bool:
    if not _needs_cloudflare_access(module, target_url):
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
                if _cookie_domain_matches(domain, _auth_hosts(module)):
                    session.cookies.set(
                        c["name"],
                        c["value"],
                        domain=domain,
                        path=c.get("path") or "/",
                    )
                    got_any = True

            save_session_state(context.storage_state())

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


def prompt_for_docs_dev_login(module: ModuleType, target_url: str, session: requests.Session) -> bool:
    global _DOCS_DEV_PROMPTED
    if _DOCS_DEV_PROMPTED:
        return False
    _DOCS_DEV_PROMPTED = True

    host = module._match_protected_docs_host(target_url)
    if not host:
        return False

    parsed = urllib.parse.urlparse(target_url)
    if not parsed.netloc:
        return False

    full_url = urllib.parse.urlunparse(parsed._replace())

    print("\nOpening Cloudflare Access login in your browser...")
    print("1) Use the email login and enter your UiPath email, then click 'Send code'.")
    print(f"2) Wait to receive the login code from [EXTERNAL] Cloudflare Access login code for {host}.")
    print("3) Paste the code in the login window.")
    print("4) Make sure you land on the docs content.")

    detected_kid = _detect_kid_from_cloudflare(module, full_url, session=session)
    if detected_kid:
        print(f"ℹ️ Detected Cloudflare Access KID: {detected_kid[:8]}...")

    params = {"redirect_url": full_url}
    if detected_kid:
        params["kid"] = detected_kid
    team_login = CLOUDFLARE_LOGIN_BASE + "?" + urllib.parse.urlencode(params)
    app_login = f"https://{host}/cdn-cgi/access/login?" + urllib.parse.urlencode({"redirect_url": full_url})

    if _try_playwright_login(module, full_url, session):
        return True

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
    return True


def handle_login_wall(module: ModuleType, url: str, session: requests.Session) -> bool:
    if not _needs_cloudflare_access(module, url):
        return False

    if load_saved_session_state(module) is not None:
        invalidate_saved_session()

    return prompt_for_docs_dev_login(module, url, session)


def _install_dev_auth_hooks(module: ModuleType) -> None:
    module.set_auth_hooks(
        storage_state_loader=lambda: load_saved_session_state(module),
        session_configurer=lambda session, url: configure_docs_dev_auth(module, session, url),
        login_handler=lambda url, session: handle_login_wall(module, url, session),
        protected_url_matcher=lambda url: _needs_cloudflare_access(module, url),
    )


def __getattr__(name: str):
    return getattr(_load_delegate(), name)


def main() -> None:
    print(
        "[deprecated] md_maker_dev.py delegates conversion to md_maker.py "
        "and keeps Cloudflare/Playwright auth locally.",
        file=sys.stderr,
    )
    _load_delegate().main()


if __name__ == "__main__":
    main()
