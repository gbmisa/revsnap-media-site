#!/usr/bin/env python3
"""Bake the live site URL into Open Graph tags, canonical links, and sitemap.

Usage:
  python3 tools/set_site_url.py https://your-domain.com
  python3 tools/set_site_url.py            # reads SITE.url from js/site-config.js

Also writes that URL into js/site-config.js when you pass it on the CLI.
"""
from __future__ import annotations

import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
CONFIG = ROOT / "js" / "site-config.js"
PAGES = {
    "index.html": "/",
    "portfolio.html": "/portfolio.html",
    "services.html": "/services.html",
    "about.html": "/about.html",
    "contact.html": "/contact.html",
    "thanks.html": "/thanks.html",
}
OG_IMAGE = "/images/cars/007-1600.jpg"


def normalize_url(url: str) -> str:
    url = url.strip().rstrip("/")
    if not url:
        raise SystemExit(
            "No site URL set. Pass https://your-domain.com or fill SITE.url in js/site-config.js"
        )
    if not re.match(r"^https?://", url, re.I):
        raise SystemExit(f"URL must start with https:// — got: {url}")
    return url


def read_config_url() -> str:
    text = CONFIG.read_text(encoding="utf-8")
    m = re.search(r'url:\s*"([^"]*)"', text)
    return m.group(1) if m else ""


def write_config_url(url: str) -> None:
    text = CONFIG.read_text(encoding="utf-8")
    new, n = re.subn(r'url:\s*"[^"]*"', f'url: "{url}"', text, count=1)
    if n != 1:
        raise SystemExit("Could not update url in js/site-config.js")
    CONFIG.write_text(new, encoding="utf-8")


def upsert_meta(html: str, prop: str, content: str) -> str:
    pattern = rf'(<meta\s+property="{re.escape(prop)}"\s+content=")[^"]*(")'
    if re.search(pattern, html):
        return re.sub(pattern, rf"\1{content}\2", html, count=1)
    tag = f'<meta property="{prop}" content="{content}">'
    if re.search(r'<meta\s+property="og:type"', html):
        return re.sub(
            r'(<meta\s+property="og:type"[^>]*>)',
            rf"\1\n{tag}",
            html,
            count=1,
        )
    return re.sub(
        r'(<meta\s+name="description"[^>]*>)',
        rf"\1\n{tag}",
        html,
        count=1,
    )


def upsert_canonical(html: str, href: str) -> str:
    if re.search(r'<link\s+rel="canonical"', html):
        return re.sub(
            r'(<link\s+rel="canonical"\s+href=")[^"]*(")',
            rf"\1{href}\2",
            html,
            count=1,
        )
    return re.sub(
        r'(<meta\s+property="og:image"[^>]*>)',
        rf'\1\n<link rel="canonical" href="{href}">',
        html,
        count=1,
    )


def write_sitemap(base: str) -> None:
    entries = [
        ("/", "1.0"),
        ("/portfolio.html", "0.9"),
        ("/services.html", "0.9"),
        ("/about.html", "0.7"),
        ("/contact.html", "0.8"),
    ]
    lines = [
        '<?xml version="1.0" encoding="UTF-8"?>',
        '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">',
    ]
    for path, prio in entries:
        loc = f"{base}/" if path == "/" else f"{base}{path}"
        lines += [
            "  <url>",
            f"    <loc>{loc}</loc>",
            f"    <priority>{prio}</priority>",
            "  </url>",
        ]
    lines.append("</urlset>")
    lines.append("")
    (ROOT / "sitemap.xml").write_text("\n".join(lines), encoding="utf-8")


def write_robots(base: str) -> None:
    (ROOT / "robots.txt").write_text(
        "User-agent: *\n"
        "Allow: /\n"
        "\n"
        f"Sitemap: {base}/sitemap.xml\n",
        encoding="utf-8",
    )


def page_url(base: str, path: str) -> str:
    return f"{base}/" if path == "/" else f"{base}{path}"


def main() -> None:
    if len(sys.argv) > 1:
        url = normalize_url(sys.argv[1])
        write_config_url(url)
    else:
        url = normalize_url(read_config_url())

    og_image = f"{url}{OG_IMAGE}"

    for name, path in PAGES.items():
        page = ROOT / name
        if not page.exists():
            continue
        html = page.read_text(encoding="utf-8")
        purl = page_url(url, path)
        html = upsert_meta(html, "og:url", purl)
        html = upsert_meta(html, "og:image", og_image)
        html = upsert_canonical(html, purl)
        page.write_text(html, encoding="utf-8")
        print(f"  updated {name}")

    write_sitemap(url)
    write_robots(url)
    print(f"\nSite URL set to {url}")
    print("  wrote sitemap.xml and robots.txt")
    print("Re-run after you change domain.")


if __name__ == "__main__":
    main()
