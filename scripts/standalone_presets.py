"""Package catalog contributions for existing presets-dev CLI versions."""

from __future__ import annotations

import json
import re
from collections.abc import Callable
from pathlib import Path

from ci_common import git
from lint_presets import (
    CLAUDE_LAYOUT_DIRS,
    ROOT,
    SUPPORTING_DIRS,
    TOOLS,
    is_catalog,
    is_supporting,
    load_schema,
    parse_frontmatter,
    split_frontmatter,
    validate_data,
)

SAFE_SEGMENT = re.compile(r"[a-zA-Z0-9_.-]+")
WINDOWS_DEVICE = re.compile(r"CON|PRN|AUX|NUL|(?:COM|LPT)[1-9]", re.IGNORECASE)
SKILL_NAME = re.compile(r"[a-z0-9]+(?:-[a-z0-9]+)*")
WEB_CATEGORIES = {"rule": "rules", "instruction": "instructions", "agent": "agents", "skill": "skills"}
WEB_SUBTYPE_SUFFIX = re.compile(r"\.(agent|instructions|prompt)\.md$")
WEB_EXTENSION = re.compile(r"\.(md|mdc)$")
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


def catalog_route(rel: str, kind: str) -> tuple[str, str, str, str]:
    parts = Path(rel).parts
    tool = parts[0]
    tech = parts[2] if tool == "claude" and parts[1] in CLAUDE_LAYOUT_DIRS else parts[1]
    filename = parts[-1]
    category = WEB_CATEGORIES[kind]
    # Catalog-only agents still use the website's original filename/folder categories.
    if kind == "agent":
        if tool == "claude" and parts[1] in CLAUDE_LAYOUT_DIRS:
            category = parts[1]
        elif tool != "claude" and filename != "AGENTS.md" and not filename.endswith(".agent.md"):
            category = "instructions" if tool == "copilot" else "rules"
    if kind == "skill":
        slug = parts[-2]
    elif filename == "CLAUDE.md" or (filename == "AGENTS.md" and tool != "claude"):
        slug = tech
    else:
        slug = WEB_EXTENSION.sub("", WEB_SUBTYPE_SUFFIX.sub("", filename))
    return tool, category, tech, slug


def catalog_identity(route: tuple[str, str, str, str]) -> tuple[str, str, str]:
    """Match the website's preset ID, which omits the technology."""
    tool, category, _, slug = route
    return tool, category, slug


def portable_segment(segment: str) -> bool:
    stem = segment.split(".", 1)[0]
    return bool(SAFE_SEGMENT.fullmatch(segment) and not segment.endswith(".") and not WINDOWS_DEVICE.fullmatch(stem))


def install_target(export: str) -> str:
    # The CLI removes the release and tool prefix. Section exports retain
    # their ID here because the installer uses that ID to mark their sections.
    return export.split("/", 4)[4].casefold()


def skill_support(source: Path, target: str, eligible: set[str]) -> dict[str, bytes]:
    files = {}
    names: dict[str, str] = {}
    prefix = source.relative_to(ROOT).as_posix() + "/"
    for rel in sorted(path for path in eligible if path.startswith(prefix)):
        relative = Path(rel[len(prefix):])
        if relative.parts[0] not in SUPPORTING_DIRS:
            continue
        child = ROOT / rel
        if child.resolve() != child or not all(portable_segment(part) for part in relative.parts):
            raise SystemExit(f"{rel}: use regular files with filenames that work on Windows, macOS and Linux")
        if not child.is_file():
            continue
        for path in (relative, *relative.parents):
            spelling = path.as_posix()
            previous = names.setdefault(spelling.casefold(), spelling)
            if previous != spelling:
                raise SystemExit(f"{rel}: skill paths {previous!r} and {spelling!r} differ only by case")
        files[f"{target}/{relative.as_posix()}"] = child.read_bytes()
    return files


def retirement_paths() -> set[str]:
    path = ROOT / "release/original-2026-11/retirement-map.json"
    if not path.is_file():
        return set()
    return {row["old_file"] for row in json.loads(path.read_text(encoding="utf-8"))["entries"]}


def build_standalone(
    files: dict[str, str | bytes],
    originals: list[dict],
    emit_frontmatter: Callable[[dict, list[str]], str],
    obsolete_catalog: set[str],
) -> list[dict]:
    listed = git("-C", str(ROOT), "ls-files", "--cached", "--others", "--exclude-standard", "-z", "--", *TOOLS)
    eligible = {rel for rel in listed.split("\0") if rel and not rel.endswith("/")}
    candidates = sorted(rel for rel in eligible - files.keys() - obsolete_catalog if is_catalog(rel) and not is_supporting(rel))
    schema = load_schema() if candidates else {}
    retired = retirement_paths() if candidates else set()
    redirects = json.loads((ROOT / "website/path-redirects.json").read_text(encoding="utf-8")) if candidates else {}
    original_entries = [entry for stack in originals for entry in stack["entries"]]
    seen_ids = {stack["id"] for stack in originals}
    skill_names = {Path(entry["catalog"]).parent.name for entry in original_entries if entry["role"] == "skill"}
    catalog_ids = {
        catalog_identity(catalog_route(entry["catalog"], entry["type"])): entry["catalog"] for entry in original_entries
    }
    targets = {install_target(export): export for entry in original_entries for export in entry["exports"]}
    stacks = []
    for rel in candidates:
        source = ROOT / rel
        if source.resolve() != source:
            raise SystemExit(f"{rel}: a preset must be a regular file")
        if not source.is_file():
            continue  # A tracked preset can be removed in the same PR.
        if rel in retired:
            raise SystemExit(f"{rel}: this catalog path is retired. Choose a fresh filename.")
        data, errors = parse_frontmatter(rel)
        if data is None:
            raise SystemExit("\n".join(errors))
        errors = validate_data(rel, data, schema, require_tool_dir=True)
        if errors:
            raise SystemExit("\n".join(errors))
        route = catalog_route(rel, data["type"])
        for depth in range(1, len(route) + 1):
            url = "/" + "/".join(route[:depth])
            if url in redirects:
                raise SystemExit(f"{rel}: public route {url} is reserved by a permanent redirect. Choose a different path.")
        if data["type"] == "agent":
            continue
        identity = catalog_identity(route)
        if identity in catalog_ids:
            raise SystemExit(f"{rel}: public catalog ID conflicts with {catalog_ids[identity]}")
        catalog_ids[identity] = rel

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
            if skill_name in skill_names:
                raise SystemExit(f"{rel}: skill install name {skill_name!r} is already in use")
            skill_names.add(skill_name)
            native = f"{target}/SKILL.md"
            front = {"name": skill_name, "description": data["description"]}
            support = skill_support(source.parent, f"{prefix}/{target}", eligible)
        else:
            native, front = standards_export(tool, preset_id, data)
        export = f"{prefix}/{native}"
        if not all(portable_segment(part) for part in export.split("/")):
            raise SystemExit(f"{rel}: generated install path {export} needs a filename that works on Windows, macOS and Linux")
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
        for filename in (export, *support):
            target = install_target(filename)
            if target in targets:
                raise SystemExit(f"{rel}: install path {target!r} conflicts with {targets[target]}")
            targets[target] = filename
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
