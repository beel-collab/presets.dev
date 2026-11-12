#!/usr/bin/env python3
"""Flag dead https links in research/<stack>/sources.md.

Not part of the default CI job: some docs hosts answer 403 to this network.
Run it when you change a source URL. Exit 1 when a URL returns 404 or 410.
"""

from __future__ import annotations

import re
import sys
import urllib.error
import urllib.request
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
URLS = re.compile(r"https://[^\s>\"]+")
AGENT = {"User-Agent": "presets-dev-source-check/1.0"}


def links() -> list[tuple[str, str]]:
    found: list[tuple[str, str]] = []
    for path in sorted((ROOT / "research").glob("*/sources.md")):
        text = path.read_text(encoding="utf-8")
        rel = path.relative_to(ROOT).as_posix()
        if "https://" not in text:
            print(f"{rel}: no https URL")
            found.append((rel, ""))
            continue
        for match in URLS.findall(text):
            found.append((rel, match.rstrip(".,")))
    return found


def status(url: str) -> int | str:
    request = urllib.request.Request(url, headers=AGENT)
    try:
        with urllib.request.urlopen(request, timeout=25) as response:
            return response.status
    except urllib.error.HTTPError as error:
        return error.code
    except Exception as error:  # noqa: BLE001 - report the failure, do not hide it
        return str(error)


def main() -> int:
    dead: list[str] = []
    for rel, url in links():
        if not url:
            dead.append(f"{rel}: no https URL")
            continue
        code = status(url)
        if code in {404, 410}:
            dead.append(f"{rel}: {code} {url}")
            print(dead[-1])
        else:
            print(f"{code} {url}")
    if dead:
        print(f"dead links: {len(dead)}")
        return 1
    print("source links ok")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
