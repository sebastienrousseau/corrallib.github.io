#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0 OR MIT
"""Finish the site that `ssg build` wrote, using the values in ssg.toml.

- Points og:url and the hreflang alternate at each page's own canonical
  URL (the layout's shared head cannot know it; ssg sets the canonical).
- Replaces the dev-server origin ssg leaves in some links with base_url.
- Writes one sitemap.xml for the whole site, dated by the last commit,
  so a rebuild of the same commit produces the same file.
- Writes CNAME and llms.txt, and copies robots.txt, .well-known/ and
  static/ (site files such as a logo) into the output.
- Fails the build if ssg's own 10-pillar quality gate reported issues.
"""

from __future__ import annotations

import json
import os
import re
import shutil
import subprocess
import sys
import tomllib
from pathlib import Path

CONFIG = tomllib.loads(Path("ssg.toml").read_text(encoding="utf-8"))
BASE = CONFIG["base_url"].rstrip("/")
OUT = Path(CONFIG["output_dir"])
SKIP_IN_SITEMAP = {"404", "offline", "thanks"}
CANONICAL = re.compile(r'<link rel="canonical" href="([^"]+)"\s*/?>')


def last_commit_date() -> str:
    date = os.environ.get("SITE_DATE")
    if date:
        return date
    out = subprocess.run(["git", "log", "-1", "--format=%cs"], capture_output=True, text=True, check=False)
    return out.stdout.strip() or "1970-01-01"


def fix_page(page: Path) -> str | None:
    text = page.read_text(encoding="utf-8")
    for dev in ("http://127.0.0.1:8000", "http://localhost:8000"):
        text = text.replace(dev, BASE)
    m = CANONICAL.search(text)
    url = m.group(1) if m else None
    if url:
        text = re.sub(r'(<meta property="og:url" content=")[^"]*(")', rf"\g<1>{url}\g<2>", text)
        text = re.sub(r'(<link rel="alternate" href=")[^"]*(" hreflang=)', rf"\g<1>{url}\g<2>", text)
    page.write_text(text, encoding="utf-8")
    return url


def title_of(page: Path) -> str:
    m = re.search(r"<title>(.*?)</title>", page.read_text(encoding="utf-8"), flags=re.DOTALL)
    return m.group(1).strip() if m else page.parent.name


def main() -> None:
    date = last_commit_date()
    entries = []
    for page in sorted(OUT.rglob("*.html")):
        url = fix_page(page)
        top = page.relative_to(OUT).parts[0]
        if url and top not in SKIP_IN_SITEMAP:
            entries.append((url, title_of(page)))
    urls = "".join(
        f"  <url>\n    <loc>{u}</loc>\n    <lastmod>{date}</lastmod>\n  </url>\n" for u, _ in entries
    )
    (OUT / "sitemap.xml").write_text(
        '<?xml version="1.0" encoding="UTF-8"?>\n'
        f'<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n{urls}</urlset>\n',
        encoding="utf-8",
    )
    shutil.copy2("robots.txt", OUT / "robots.txt")
    shutil.copytree(".well-known", OUT / ".well-known", dirs_exist_ok=True)
    if Path("static").is_dir():
        shutil.copytree("static", OUT, dirs_exist_ok=True)
    domain = BASE.split("://", 1)[1]
    (OUT / "CNAME").write_text(domain + "\n", encoding="utf-8")
    pages = "".join(f"- [{t}]({u})\n" for u, t in entries)
    (OUT / "llms.txt").write_text(
        f"# {CONFIG['site_name']}\n\n> {CONFIG['site_description']}\n\n## Pages\n\n{pages}", encoding="utf-8"
    )
    print(f"post-build: {len(entries)} pages in sitemap.xml, dated {date}")
    report = json.loads((OUT / "quality-gate-report.json").read_text(encoding="utf-8"))
    issues = [f"{name}: {issue}" for name, p in report["pillars"].items() for issue in p["issues"]]
    if issues:
        print("quality gate failed:\n  " + "\n  ".join(issues), file=sys.stderr)
        sys.exit(1)
    print(f"quality gate: {report['passed_pillars']}/{report['total_pillars']} pillars, 0 issues")


if __name__ == "__main__":
    main()
