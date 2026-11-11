"""Git helpers shared by the preset CI scripts."""

from __future__ import annotations

import os
import subprocess
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def git(*args: str) -> str:
    result = subprocess.run(
        ["git", *args],
        cwd=ROOT,
        text=True,
        capture_output=True,
        check=False,
    )
    if result.returncode != 0:
        raise RuntimeError(
            f"git {' '.join(args)} failed: {result.stderr.strip()}"
        )
    return result.stdout


def rev_exists(ref: str) -> bool:
    result = subprocess.run(
        ["git", "rev-parse", "--verify", "--quiet", ref],
        cwd=ROOT,
        capture_output=True,
    )
    return result.returncode == 0


def resolve_base() -> str:
    raw = os.environ.get("BASE_SHA", "").strip()
    if raw and raw.lower() != "null" and set(raw) != {"0"} and rev_exists(raw):
        return raw
    for candidate in ("origin/main", "main"):
        if rev_exists(candidate):
            return candidate
    if rev_exists("HEAD^"):
        return "HEAD^"
    return "HEAD"


def changed_files(base: str) -> list[str]:
    found: set[str] = set()
    if base != "HEAD":
        three = subprocess.run(
            ["git", "diff", "--name-only", "--diff-filter=ACMR", f"{base}...HEAD"],
            cwd=ROOT,
            text=True,
            capture_output=True,
        )
        if three.returncode == 0:
            found.update(three.stdout.splitlines())
        else:
            found.update(
                git("diff", "--name-only", "--diff-filter=ACMR", base, "HEAD").splitlines()
            )
    if os.environ.get("GITHUB_ACTIONS") != "true":
        found.update(git("diff", "--name-only", "--diff-filter=ACMR", "HEAD").splitlines())
        found.update(
            git("diff", "--name-only", "--cached", "--diff-filter=ACMR").splitlines()
        )
        found.update(git("ls-files", "--others", "--exclude-standard").splitlines())
    files: list[str] = []
    for rel in sorted(found):
        rel = rel.strip().replace("\\", "/")
        if not rel or rel.endswith("/"):
            continue
        if (ROOT / rel).is_file():
            files.append(rel)
    return files
