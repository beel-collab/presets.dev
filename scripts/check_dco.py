#!/usr/bin/env python3
"""Require a Developer Certificate of Origin sign-off on each commit."""

from __future__ import annotations

import re
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))

from ci_common import git, resolve_base, rev_exists

SIGNED_OFF = re.compile(r"^Signed-off-by:\s*(.+?)\s*<([^>]+)>\s*$", re.MULTILINE)


def commits_since(base: str) -> list[dict[str, str]]:
    if base == "HEAD" or not rev_exists(base):
        return []
    raw = git(
        "log",
        f"{base}..HEAD",
        "--format=%H%x1f%an%x1f%ae%x1f%P%x1f%B%x1e",
    )
    commits: list[dict[str, str]] = []
    for chunk in raw.split("\x1e"):
        chunk = chunk.strip("\n")
        if not chunk.strip():
            continue
        sha, author, email, parents, body = chunk.split("\x1f", 4)
        commits.append(
            {
                "sha": sha,
                "author": author,
                "email": email,
                "parents": parents,
                "body": body,
            }
        )
    return commits


def main() -> int:
    base = resolve_base()
    missing: list[str] = []
    checked = 0
    for commit in commits_since(base):
        parents = commit["parents"].split()
        if len(parents) > 1:
            continue
        checked += 1
        author = commit["author"].strip()
        email = commit["email"].strip()
        matched = False
        for name, signed_email in SIGNED_OFF.findall(commit["body"]):
            if name.strip() == author and signed_email.strip().casefold() == email.casefold():
                matched = True
                break
        if matched:
            continue
        missing.append(
            f"{commit['sha'][:12]} {author} <{email}>\n"
            f"  add a trailer line: Signed-off-by: {author} <{email}>\n"
            "  git commit -s records it. See https://developercertificate.org/"
        )
    if missing:
        print(f"DCO sign-off missing on {len(missing)} commit(s) (range {base}..HEAD):")
        print("\n".join(missing))
        return 1
    print(f"DCO: {checked} commit(s) signed off (range {base}..HEAD)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
