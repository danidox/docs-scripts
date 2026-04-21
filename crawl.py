import os
import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin, urlparse
from markdownify import markdownify as md
from playwright.sync_api import sync_playwright

OUTPUT_ROOT = "output"

SIDEBAR_ID = "SideBarMenu_Root"
CONTENT_ID = "DocContainer"

session = requests.Session()
session.headers.update({
    "User-Agent": "Mozilla/5.0 (DocCrawler)"
})


def extract_sidebar_links_with_playwright(start_url: str, guide_base: str) -> list[str]:
    urls = []

    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()
        page.goto(start_url, wait_until="networkidle")

        page.wait_for_selector(f"#{SIDEBAR_ID}")

        links = page.query_selector_all(f"#{SIDEBAR_ID} a[href]")

        for link in links:
            href = link.get_attribute("href")
            if not href:
                continue

            full = urljoin(guide_base, href)
            if full.startswith(guide_base):
                clean = full.split("#")[0]
                if clean not in urls:
                    urls.append(clean)

        browser.close()

    return urls


def get_soup(url: str) -> BeautifulSoup:
    r = session.get(url)
    r.raise_for_status()
    return BeautifulSoup(r.text, "html.parser")


def extract_guide_base(url: str) -> str:
    parts = urlparse(url).path.strip("/").split("/")
    return urljoin(url, "/" + "/".join(parts[:4]) + "/")


def extract_content_markdown(soup: BeautifulSoup) -> str:
    content = soup.find(id=CONTENT_ID)
    if not content:
        raise RuntimeError("DocContainer not found")

    return md(str(content), heading_style="ATX")


def url_to_output_path(url: str) -> str:
    parts = urlparse(url).path.strip("/").split("/")
    *folders, page = parts
    return os.path.join(OUTPUT_ROOT, *folders, f"{page}.md")


def save_markdown(path: str, content: str):
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "w", encoding="utf-8") as f:
        f.write(content)


def main():
    start_url = input("Enter the starting page URL:\n").strip()

    print("🔍 Resolving sidebar via browser...")
    guide_base = extract_guide_base(start_url)

    urls = extract_sidebar_links_with_playwright(start_url, guide_base)
    print(f"📄 Found {len(urls)} pages")

    for url in urls:
        print(f"➡️  Processing {url}")
        soup = get_soup(url)
        markdown = extract_content_markdown(soup)
        save_markdown(url_to_output_path(url), markdown)

    print("✅ Done")


if __name__ == "__main__":
    main()
