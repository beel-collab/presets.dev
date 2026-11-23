"""Package catalog contributions for existing presets-dev CLI versions."""

from __future__ import annotations

import json
import re
from collections.abc import Callable
from pathlib import Path

from lint_presets import (
    ROOT,
    SUPPORTING_DIRS,
    catalog_files,
    is_supporting,
    load_schema,
    parse_frontmatter,
    split_frontmatter,
    validate_data,
)

SAFE_SEGMENT = re.compile(r"[a-zA-Z0-9_.-]+")
SKILL_NAME = re.compile(r"[a-z0-9]+(?:-[a-z0-9]+)*")
SKILL_ROOTS = {
    "cursor": "cursor/.cursor/skills",
    "copilot": "copilot/.github/skills",
    "claude": "claude/.claude/skills",
    "windsurf": "windsurf/.devin/skills",
    "cline": "cline/.cline/skills",
    "codex": "agents/.agents/skills",
    "antigravity": "agents/.agents/skills",
}


def standards_export(tool: str, preset_id: str, data: dict) -> tuple[str, dict]:
    globs = data.get("globs", [])
    patterns = [globs] if isinstance(globs, str) else globs
    if tool == "cursor":
        front = {"description": data["description"], "alwaysApply": data.get("alwaysApply", False)}
        if patterns:
            front["globs"] = ", ".join(patterns)
        return f"cursor/.cursor/rules/{preset_id}.mdc", front
    if tool == "copilot":
        return f"copilot/.github/instructions/{preset_id}.instructions.md", {"applyTo": ",".join(patterns) or "**"}
    if tool == "windsurf":
        return f"windsurf/.devin/rules/{preset_id}.md", {
            "description": data["description"],
            "trigger": "model_decision",
        }
    if tool == "claude":
        return f"claude/.claude/rules/{preset_id}.md", {"paths": patterns} if patterns else {}
    if tool == "cline":
        return f"cline/.clinerules/{preset_id}.md", {"paths": patterns} if patterns else {}
    filename = "AGENTS" if tool == "codex" else "GEMINI"
    return f"{tool}/{filename}.{preset_id}-section.md", {}


def skill_support(source: Path, target: str) -> dict[str, bytes]:
    files = {}
    for folder in sorted(SUPPORTING_DIRS):
        support = source / folder
        if support.is_symlink():
            raise SystemExit(f"{support.relative_to(ROOT)}: skill support may not be a symlink")
        for child in sorted(support.rglob("*")):
            relative = child.relative_to(source)
            if child.is_symlink() or not all(SAFE_SEGMENT.fullmatch(part) for part in relative.parts):
                raise SystemExit(f"{child.relative_to(ROOT)}: use plain filenames in skill support")
            if child.is_file():
                files[f"{target}/{relative.as_posix()}"] = child.read_bytes()
    return files


def retirement_paths() -> set[str]:
    path = ROOT / "release/original-2026-11/retirement-map.json"
    if not path.is_file():
        return set()
    return {row["old_file"] for row in json.loads(path.read_text(encoding="utf-8"))["entries"]}


def build_standalone(
    files: dict[str, str | bytes],
    official_ids: set[str],
    official_skills: set[str],
    emit_frontmatter: Callable[[dict, list[str]], str],
) -> list[dict]:
    excluded = retirement_paths() | files.keys()
    candidates = sorted(set(catalog_files()) - excluded)
    schema = load_schema() if candidates else {}
    seen_ids = set(official_ids)
    seen_skill_targets = set()
    stacks = []
    for rel in candidates:
        if is_supporting(rel):
            continue
        source = ROOT / rel
        if source.resolve() != source:
            raise SystemExit(f"{rel}: a preset must be a regular file")
        data, errors = parse_frontmatter(rel)
        if data is None:
            raise SystemExit("\n".join(errors))
        errors = validate_data(rel, data, schema, require_tool_dir=True)
        if errors:
            raise SystemExit("\n".join(errors))
        if data["type"] == "agent":
            continue

        preset_id = data["id"]
        if preset_id in seen_ids:
            raise SystemExit(f"{rel}: CLI install ID {preset_id!r} is already in use")
        seen_ids.add(preset_id)
        tool = rel.split("/", 1)[0]
        prefix = f"release/{preset_id}/native"
        role = "skill" if data["type"] == "skill" else "standards"
        support = {}
        if role == "skill":
            if source.name != "SKILL.md":
                raise SystemExit(f"{rel}: a skill must use a SKILL.md file")
            skill_name = source.parent.name
            if len(skill_name) > 64 or not SKILL_NAME.fullmatch(skill_name):
                raise SystemExit(f"{rel}: use a kebab-case skill name up to 64 characters")
            target = f"{SKILL_ROOTS[tool]}/{skill_name}"
            if skill_name in official_skills or target in seen_skill_targets:
                raise SystemExit(f"{rel}: skill install name {skill_name!r} is already in use")
            seen_skill_targets.add(target)
            native = f"{target}/SKILL.md"
            front = {"name": skill_name, "description": data["description"]}
            support = skill_support(source.parent, f"{prefix}/{target}")
        else:
            native, front = standards_export(tool, preset_id, data)
        _, body = split_frontmatter(source.read_text(encoding="utf-8"))
        if not body.strip():
            raise SystemExit(f"{rel}: add instructions to the preset")
        if "<!-- native:start -->" in body or (
            role == "standards" and tool in {"codex", "antigravity"} and "<!-- presets.dev:" in body
        ):
            raise SystemExit(f"{rel}: the body contains a reserved install marker")
        text = (emit_frontmatter(front, list(front)) + "\n" if front else "") + body.strip("\n") + "\n"
        if role == "standards" and tool == "windsurf" and len(text) > 12000:
            raise SystemExit(f"{rel}: the native rule exceeds 12000 characters")
        export = f"{prefix}/{native}"
        files[export] = text
        files.update(support)
        stacks.append({
            "id": preset_id,
            # The released CLI checks this flag before planning an install.
            "status": "complete",
            "kind": "standalone",
            "entries": [{
                "catalog": rel,
                "tool": tool,
                "role": role,
                "type": data["type"],
                "exports": [export, *support],
            }],
        })
    return stacks
