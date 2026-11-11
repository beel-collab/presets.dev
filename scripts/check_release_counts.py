#!/usr/bin/env python3
"""Verify original-release catalog counts and native install files.

A stack marked complete in release/original-2026-11/manifest.json must contain
exactly one standards file and one SKILL.md for each release tool. The full
420 count applies when all 30 stacks are marked complete. This checkpoint
enforces the same per-stack contract for every stack that is complete.
"""

from __future__ import annotations

import json
import sys
from pathlib import Path

import yaml

sys.path.insert(0, str(Path(__file__).resolve().parent))

from lint_presets import ROOT, load_schema, parse_frontmatter, validate_data

MANIFEST = ROOT / "release" / "original-2026-11" / "manifest.json"
RELEASE_TOOLS = ("cursor", "copilot", "claude", "windsurf", "cline", "codex", "gemini-cli")
ALLOWED_NATIVE = {
    "cursor-rule": {"description", "globs", "alwaysApply"},
    "copilot-instructions": {"applyTo"},
    "claude-rule": {"paths"},
    "windsurf-rule": {"description", "trigger"},
    "cline-rule": {"paths"},
    "skill": {"name", "description"},
    "cursor-skill": {"name", "description", "paths"},
}
CATALOG_KEYS = {
    "id",
    "slug",
    "title",
    "type",
    "tools",
    "stack",
    "tags",
    "author",
    "license",
    "origin",
    "version",
    "tested_with",
    "created",
    "updated",
    "libs",
    "updated_for",
    "also_for",
    "model",
    "globs",
    "alwaysApply",
}
TRIGGERS = {"always_on", "manual", "model_decision", "agent", "glob"}


def split_frontmatter(text: str) -> tuple[dict | None, str]:
    if not text.startswith("---\n"):
        return None, text
    end = text.find("\n---\n", 4)
    if end == -1:
        return None, text
    data = yaml.safe_load(text[4:end])
    body = text[end + 5 :]
    if not isinstance(data, dict):
        return None, text
    return data, body


def infer_format(path: str, data: dict | None) -> str:
    if data is None:
        return "plain"
    keys = set(data)
    if keys == {"applyTo"}:
        return "copilot-instructions"
    if keys == {"paths"} and "/.clinerules/" in f"/{path}":
        return "cline-rule"
    if keys == {"paths"}:
        return "claude-rule"
    if "alwaysApply" in keys:
        return "cursor-rule"
    if "trigger" in keys:
        return "windsurf-rule"
    if "paths" in keys and "name" in keys:
        return "cursor-skill"
    if keys == {"name", "description"}:
        return "skill"
    return "unknown"


def check_native(rel: str, errors: list[str]) -> None:
    path = ROOT / rel
    if not path.is_file():
        errors.append(f"{rel}: native export missing")
        return
    text = path.read_text(encoding="utf-8")
    if not text.endswith("\n") or text.endswith("\n\n"):
        errors.append(f"{rel}: native file must end with one newline")
    data, body = split_frontmatter(text)
    kind = infer_format(rel, data)
    if kind == "unknown":
        errors.append(f"{rel}: native frontmatter is not an allowlisted shape")
        return
    if data is None:
        if rel.endswith("SKILL.md"):
            errors.append(f"{rel}: skill export is missing frontmatter")
        if "<!-- native:start -->" in text:
            errors.append(f"{rel}: native export still contains the catalog marker")
        return
    extra = set(data) - ALLOWED_NATIVE[kind]
    if extra:
        errors.append(f"{rel}: native frontmatter has catalog or unknown keys {sorted(extra)}")
    leaked = CATALOG_KEYS & set(data)
    if kind == "cursor-rule":
        leaked -= {"globs", "alwaysApply"}
    if leaked:
        errors.append(f"{rel}: native frontmatter leaked catalog keys {sorted(leaked)}")
    if kind in {"skill", "cursor-skill"}:
        name = data.get("name")
        description = data.get("description")
        folder = Path(rel).parent.name
        if name != folder:
            errors.append(f"{rel}: skill name {name!r} does not match folder {folder!r}")
        if not isinstance(description, str) or not description.strip():
            errors.append(f"{rel}: skill description is empty")
        elif len(description) > 1024:
            errors.append(f"{rel}: skill description is {len(description)} characters")
        if "Do not use" not in description and "Skip it" not in description and "not " not in description.lower():
            errors.append(f"{rel}: skill description needs a non-trigger")
    if kind == "cline-rule":
        paths = data.get("paths")
        if not isinstance(paths, list) or not paths or not all(isinstance(item, str) and item for item in paths):
            errors.append(f"{rel}: cline paths must be a non-empty list of strings")
    if kind == "claude-rule":
        paths = data.get("paths")
        if not isinstance(paths, list) or not paths:
            errors.append(f"{rel}: claude paths must be a non-empty list")
    if kind == "windsurf-rule":
        if data.get("trigger") not in TRIGGERS:
            errors.append(f"{rel}: windsurf trigger is not a documented value")
        if len(text) > 12000:
            errors.append(f"{rel}: {len(text)} characters exceeds the 12000 Cascade rule limit")
    if kind == "cursor-rule" and data.get("alwaysApply") is not False:
        errors.append(f"{rel}: this Next.js Cursor rule must stay file-scoped")
    if "<!-- native:start -->" in body:
        errors.append(f"{rel}: native export still contains the catalog marker")


def main() -> int:
    errors: list[str] = []
    if not MANIFEST.is_file():
        print("release manifest missing")
        return 1
    document = json.loads(MANIFEST.read_text(encoding="utf-8"))
    if document.get("tools") != list(RELEASE_TOOLS):
        errors.append("manifest tools must be the seven release tools, including gemini-cli")
    schema = load_schema()
    complete = [stack for stack in document.get("stacks", []) if stack.get("status") == "complete"]
    if not complete:
        errors.append("manifest has no complete stack")
    seen_catalog: set[str] = set()
    for stack in complete:
        stack_id = stack.get("id")
        rows = stack.get("entries", [])
        if len(rows) != len(RELEASE_TOOLS) * 2:
            errors.append(f"{stack_id}: expected {len(RELEASE_TOOLS) * 2} entries, found {len(rows)}")
        by_tool: dict[str, dict[str, dict]] = {}
        for row in rows:
            tool = row.get("tool")
            role = row.get("role")
            by_tool.setdefault(tool, {})
            if role in by_tool[tool]:
                errors.append(f"{stack_id}: duplicate {tool} {role}")
            by_tool[tool][role] = row
        for tool in RELEASE_TOOLS:
            roles = by_tool.get(tool, {})
            if set(roles) != {"standards", "skill"}:
                errors.append(f"{stack_id}: {tool} roles are {sorted(roles)}")
                continue
            skill = roles["skill"]
            standards = roles["standards"]
            if skill.get("type") != "skill" or not str(skill.get("catalog", "")).endswith("/SKILL.md"):
                errors.append(f"{stack_id}: {tool} skill is not a SKILL.md")
            if standards.get("type") not in {"rule", "instruction"}:
                errors.append(f"{stack_id}: {tool} standards type must be rule or instruction")
            if standards.get("type") == "agent":
                errors.append(f"{stack_id}: {tool} standards must not be an agent")
        for row in rows:
            rel = row.get("catalog", "")
            seen_catalog.add(rel)
            if f"/{stack_id}/" not in f"/{rel}":
                errors.append(f"{rel}: path does not contain the stack id")
            data, parse_errors = parse_frontmatter(rel)
            errors.extend(parse_errors)
            if data is None:
                continue
            errors.extend(validate_data(rel, data, schema, require_tool_dir=True))
            if data.get("stack") != stack_id:
                errors.append(f"{rel}: stack field is not {stack_id}")
            if data.get("tools") != [row.get("tool")]:
                errors.append(f"{rel}: tools do not match the manifest")
            if data.get("type") != row.get("type"):
                errors.append(f"{rel}: type does not match the manifest")
            author = data.get("author") if isinstance(data.get("author"), dict) else {}
            if author.get("name") != "presets.dev":
                errors.append(f"{rel}: author.name must be presets.dev")
            if "updated_for" not in data:
                errors.append(f"{rel}: updated_for is required for a release entry")
            if "<!-- native:start -->" not in (ROOT / rel).read_text(encoding="utf-8"):
                errors.append(f"{rel}: missing native:start marker")
            exports = row.get("exports") or []
            if not exports:
                errors.append(f"{rel}: missing native exports")
            for exported in exports:
                if not str(exported).startswith(f"release/{stack_id}/native/"):
                    errors.append(f"{exported}: export is outside the stack native directory")
                check_native(str(exported), errors)
    from lint_presets import catalog_files, loose_frontmatter

    for rel in catalog_files():
        if rel in seen_catalog:
            continue
        data = loose_frontmatter(rel)
        if isinstance(data, dict) and data.get("stack") in {stack["id"] for stack in complete}:
            errors.append(f"{rel}: extra catalog file for a complete stack")
    if len(seen_catalog) != len(complete) * len(RELEASE_TOOLS) * 2:
        errors.append(
            f"catalog count {len(seen_catalog)} does not match "
            f"{len(complete)} complete stack(s) times 14"
        )
    if errors:
        print(f"release counts failed ({len(errors)} issue(s)):")
        print("\n".join(errors))
        return 1
    print(
        "release counts ok: "
        f"{len(complete)} complete stack(s), "
        f"{len(seen_catalog)} catalog entries, "
        f"{len(RELEASE_TOOLS)} tools"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
