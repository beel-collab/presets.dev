#!/usr/bin/env python3
"""Compare original-release prose with the existing copied catalog.

The seven tool adaptations of one master are an intentional family and are not
compared with each other. A release file fails when it shares a 40-word run
with a legacy catalog file, or when its 8-word shingle Jaccard overlap with a
legacy file is at least 0.80. Code fences are ignored so short API lines are
not treated as copied prose.
"""

from __future__ import annotations

import hashlib
import json
import re
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))

from lint_presets import ROOT, catalog_files

MANIFEST = ROOT / "release" / "original-2026-11" / "manifest.json"
FENCE = re.compile(r"```.*?```", re.DOTALL)
FRONT = re.compile(r"^---\n.*?\n---\n", re.DOTALL)
WORD = re.compile(r"[A-Za-z0-9']+")
JACCARD_LIMIT = 0.80
RUN = 40
SHINGLE = 8


def prose_words(text: str) -> list[str]:
    without_front = FRONT.sub(" ", text)
    without_code = FENCE.sub(" ", without_front)
    return WORD.findall(without_code.lower())


def digest(words: list[str]) -> str:
    return hashlib.sha1(" ".join(words).encode("utf-8")).hexdigest()


def shingles(words: list[str], size: int) -> set[str]:
    if len(words) < size:
        return set()
    return {digest(words[index : index + size]) for index in range(len(words) - size + 1)}


def release_catalog_paths() -> set[str]:
    document = json.loads(MANIFEST.read_text(encoding="utf-8"))
    found: set[str] = set()
    for stack in document.get("stacks", []):
        if stack.get("status") != "complete":
            continue
        for row in stack.get("entries", []):
            found.add(row["catalog"])
    return found


def main() -> int:
    if not MANIFEST.is_file():
        print("similarity check: release manifest missing")
        return 1
    release_paths = release_catalog_paths()
    if not release_paths:
        print("similarity check: no complete release entries")
        return 1
    release_words = {
        rel: prose_words((ROOT / rel).read_text(encoding="utf-8")) for rel in sorted(release_paths)
    }
    release_shingles = {rel: shingles(words, SHINGLE) for rel, words in release_words.items()}
    release_runs = {rel: shingles(words, RUN) for rel, words in release_words.items()}
    run_owner: dict[str, str] = {}
    for rel, grams in release_runs.items():
        for gram in grams:
            run_owner.setdefault(gram, rel)
    errors: list[str] = []
    top: list[tuple[float, str, str]] = []
    for rel in catalog_files():
        if rel in release_paths:
            continue
        try:
            text = (ROOT / rel).read_text(encoding="utf-8")
        except UnicodeDecodeError:
            continue
        words = prose_words(text)
        if len(words) < SHINGLE:
            continue
        legacy = shingles(words, SHINGLE)
        if len(words) >= RUN:
            for index in range(len(words) - RUN + 1):
                gram = digest(words[index : index + RUN])
                owner = run_owner.get(gram)
                if owner:
                    errors.append(f"{owner}: shares a {RUN}-word run with {rel}")
                    break
        for owner, grams in release_shingles.items():
            if not grams or not legacy:
                continue
            shared = len(grams & legacy)
            if shared == 0:
                continue
            score = shared / (len(grams) + len(legacy) - shared)
            if score >= JACCARD_LIMIT:
                errors.append(f"{owner}: Jaccard {score:.2f} with {rel}")
            if score > 0.05:
                top.append((score, owner, rel))
    top.sort(reverse=True)
    if top:
        score, owner, rel = top[0]
        print(f"similarity nearest legacy overlap: {score:.3f} {owner} ~ {rel}")
    else:
        print("similarity nearest legacy overlap: none above 0.05")
    if errors:
        unique = list(dict.fromkeys(errors))
        print(f"similarity check failed ({len(unique)} issue(s)):")
        print("\n".join(unique[:50]))
        return 1
    print(f"similarity check ok: {len(release_paths)} release file(s) against the copied catalog")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
