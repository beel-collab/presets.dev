#!/usr/bin/env python3
"""Build original-release catalog files and native install payloads.

Each stack lives in masters/<id>/ with stack.json, standards.md, and skill.md.
Catalog frontmatter stays in the catalog file. Native exports rebuild the small
frontmatter each tool actually reads.
"""

from __future__ import annotations

import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
CREATED = "2026-11-11"
MARKER = "<!-- native:start -->"
AUTHOR = {"name": "presets.dev", "github": "beel-collab"}
TOOLS = ("cursor", "copilot", "claude", "windsurf", "cline", "codex", "antigravity")
# Retired tool directory. Orphan cleanup deletes generated files still under this name.
RETIRED_TOOLS = ("gemini-cli",)
TOOL_LABEL = {
    "cursor": "Cursor",
    "copilot": "Copilot",
    "claude": "Claude Code",
    "windsurf": "Windsurf",
    "cline": "Cline",
    "codex": "Codex",
    "antigravity": "Antigravity CLI",
}
TESTED = {
    "cursor": "Cursor docs 2026-11-11; app not executed",
    "copilot": "Copilot docs 2026-11-11; app not executed",
    "claude": "Claude Code docs 2026-11-11; CLI not run",
    "windsurf": "Devin and Cascade docs 2026-11-11; not run",
    "cline": "Cline docs 2026-11-11; app not executed",
    "codex": "Codex docs 2026-11-11; CLI not executed",
    "antigravity": "Antigravity CLI docs 2026-11-12; CLI not run",
}
FIXTURE = "node v22.23.4 fixture 2026-11-11"
CATALOG_FRONT_ORDER = [
    "id",
    "slug",
    "title",
    "description",
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
    "globs",
    "alwaysApply",
]
FORMAT_KEYS = {
    "cursor-rule": ["description", "globs", "alwaysApply"],
    "copilot-instructions": ["applyTo"],
    "claude-rule": ["paths"],
    "windsurf-rule": ["description", "trigger"],
    "cline-rule": ["paths"],
    "skill": ["name", "description"],
    "cursor-skill": ["name", "description", "paths"],
    "plain": [],
}
NATIVE_ORDER = {
    "cursor-rule": ["description", "globs", "alwaysApply"],
    "copilot-instructions": ["applyTo"],
    "claude-rule": ["paths"],
    "windsurf-rule": ["description", "trigger"],
    "cline-rule": ["paths"],
    "skill": ["name", "description"],
    "cursor-skill": ["name", "description", "paths"],
    "plain": [],
}


def q(value: str) -> str:
    return json.dumps(value, ensure_ascii=False)


def emit_frontmatter(data: dict, order: list[str]) -> str:
    lines = ["---"]
    for key in order:
        if key not in data:
            continue
        value = data[key]
        if isinstance(value, bool):
            lines.append(f"{key}: {'true' if value else 'false'}")
        elif isinstance(value, str):
            lines.append(f"{key}: {q(value)}")
        elif isinstance(value, list):
            lines.append(f"{key}:")
            for item in value:
                if not isinstance(item, str):
                    raise TypeError(f"{key} items must be strings")
                lines.append(f"  - {q(item)}")
        elif isinstance(value, dict):
            lines.append(f"{key}:")
            for sub_key, sub_value in value.items():
                if not isinstance(sub_value, str):
                    raise TypeError(f"{key}.{sub_key} must be a string")
                lines.append(f"  {sub_key}: {q(sub_value)}")
        else:
            raise TypeError(f"unsupported frontmatter value for {key}")
    lines.append("---")
    return "\n".join(lines) + "\n"


def join_sections(parts: list[str]) -> str:
    cleaned = [part.strip() for part in parts if part and part.strip()]
    return "\n\n".join(cleaned) + "\n"


def catalog_slug(rel: str) -> str:
    if rel.endswith(".mdc"):
        return rel[:-4]
    if rel.endswith(".md"):
        return rel[:-3]
    raise ValueError(rel)


def load_stacks() -> list[dict]:
    found: list[dict] = []
    for path in sorted((ROOT / "masters").glob("*/stack.json")):
        data = json.loads(path.read_text(encoding="utf-8"))
        data["root"] = path.parent
        found.append(data)
    found.sort(key=lambda item: item["order"])
    return found


def standards_title(tool: str, spec: dict) -> str:
    product = spec["product"]
    focus = spec["focus"]
    titles = {
        "cursor": f"{product} Rules for Cursor: {focus}",
        "copilot": f"{product} Copilot Instructions: {focus}",
        "claude": f"{product} Claude Code Rules: {focus}",
        "windsurf": f"{product} Windsurf Rules: {focus}",
        "cline": f"{product} Cline Rules: {focus}",
        "codex": f"{product} Codex Instructions: {focus}",
        "antigravity": f"{product} Antigravity CLI Rules: {focus}",
    }
    return titles[tool]


def standards_description(tool: str, spec: dict) -> str:
    product = spec["product"]
    focus = spec["focus"]
    text = {
        "cursor": (
            f"Cursor rules for {product}: {focus}. "
            f"Structure, data, errors, security, performance, and tests. {spec['updated_for']}."
        ),
        "copilot": (
            f"Copilot instructions for {product}: {focus}. "
            f"Structure, data, errors, security, performance, and tests. {spec['updated_for']}."
        ),
        "claude": (
            f"Claude Code rules for {product}: {focus}. "
            f"Structure, data, errors, security, performance, and tests. {spec['updated_for']}."
        ),
        "windsurf": (
            f"Windsurf rules for {product}: {focus}. "
            f"Structure, data, errors, security, performance, and tests. {spec['updated_for']}."
        ),
        "cline": (
            f"Cline rules for {product}: {focus}. "
            f"Structure, data, errors, security, performance, and tests. {spec['updated_for']}."
        ),
        "codex": (
            f"Codex instructions for {product}: {focus}. "
            f"Append to AGENTS.md. Structure, security, and tests. {spec['updated_for']}."
        ),
        "antigravity": (
            f"Antigravity CLI rules for {product}: {focus}. "
            f"Append to GEMINI.md. Structure, security, and tests. {spec['updated_for']}."
        ),
    }
    return text[tool]


def skill_title(tool: str, spec: dict) -> str:
    return f"{spec['product']} {spec['skill_label']} Skill for {TOOL_LABEL[tool]}"


def skill_catalog_description(tool: str, spec: dict) -> str:
    text = spec["native_skill_description"]
    if len(text) > 400:
        raise SystemExit(f"{spec['id']}: native skill description exceeds the catalog limit")
    return text


def shared_skill_host(spec: dict) -> str:
    skill = spec["skill_name"]
    return (
        f"Shared skill `{skill}` for {spec['product']}. "
        f"Codex and Antigravity CLI both read `.agents/skills/{skill}/SKILL.md`. "
        f"Install this one file. Codex calls it with `${skill}` or `/skills`. "
        f"Do not also copy the Cursor skill to that path."
    )


def host_line(tool: str, spec: dict, role: str) -> str:
    product = spec["product"]
    skill = spec["skill_name"]
    if role == "standards":
        return {
            "cursor": (
                f"File-scoped Cursor rule for {product}. "
                f"It attaches when a matching file is in context."
            ),
            "copilot": (
                f"Path-specific Copilot instructions for {product}. "
                f"They apply through `applyTo` and leave `.github/copilot-instructions.md` in place."
            ),
            "claude": (
                f"Path-scoped Claude Code rule for {product}. "
                f"It loads when a matching file is read. It does not replace `CLAUDE.md`."
            ),
            "windsurf": (
                f"Devin rule for {product}. Install the `.devin/rules` file. "
                f"The trigger is model decision. Do not also copy it into `.windsurf/rules`."
            ),
            "cline": (
                f"Conditional Cline rule for {product}. "
                f"Install it under `.clinerules/` only."
            ),
            "codex": (
                f"Section to append to `AGENTS.md` for {product}. "
                f"This is project guidance, not a custom agent."
            ),
            "antigravity": (
                f"Section to append to `GEMINI.md` for {product}. "
                f"Antigravity CLI also reads `AGENTS.md`. Confirm the loaded rules before you rely on them."
            ),
        }[tool]
    return {
        "cursor": (
            f"Cursor skill `{skill}` for {product}. "
            f"Run it with `/{skill}`, or let Agent select it when the request matches. "
            f"`paths` only limits automatic surfacing."
        ),
        "copilot": (
            f"Copilot skill `{skill}` for {product}. "
            f"The description decides when Copilot loads it. Keep this copy under `.github/skills`."
        ),
        "claude": (
            f"Claude Code skill `{skill}` for {product}. "
            f"The command is `/{skill}`. Leave the normal permission prompts on."
        ),
        "windsurf": (
            f"Devin skill `{skill}` for {product}. "
            f"Invoke it with `/{skill}`. Install only `.devin/skills`. This file is not a subagent."
        ),
        "cline": (
            f"Cline skill `{skill}` for {product}. "
            f"`/{skill}` forces it. A global skill of the same name overrides this project file."
        ),
        "codex": shared_skill_host(spec),
        "antigravity": shared_skill_host(spec),
    }[tool]


def install_section(tool: str, spec: dict, role: str) -> str:
    stack = spec["id"]
    skill = spec["skill_name"]
    rules = f"{stack}-rules"
    if role == "standards":
        target = {
            "cursor": f"`.cursor/rules/{rules}.mdc`",
            "copilot": f"`.github/instructions/{stack}.instructions.md`",
            "claude": f"`.claude/rules/{rules}.md`",
            "windsurf": f"`.devin/rules/{rules}.md`",
            "cline": f"`.clinerules/{rules}.md` (do not also copy it to `.cline/rules/`)",
            "codex": "`AGENTS.md` as an appended section, not a replacement and not a custom agent",
            "antigravity": "`GEMINI.md` or `AGENTS.md` as an appended section",
        }[tool]
    else:
        target = {
            "cursor": f"`.cursor/skills/{skill}/SKILL.md`",
            "copilot": f"`.github/skills/{skill}/SKILL.md`",
            "claude": f"`.claude/skills/{skill}/SKILL.md`",
            "windsurf": f"`.devin/skills/{skill}/SKILL.md`",
            "cline": f"`.cline/skills/{skill}/SKILL.md`",
            "codex": f"`.agents/skills/{skill}/SKILL.md` (one file shared with Antigravity CLI)",
            "antigravity": f"`.agents/skills/{skill}/SKILL.md` (one file shared with Codex)",
        }[tool]
    return "\n".join(
        [
            "## Install",
            "",
            f"Install the native export at {target}.",
            "Copy that export, not this catalog file. Catalog fields such as `tools` and `author` are for presets.dev.",
            "Install one tool's skill for a checkout. Do not drop every tool's copy into `.agents/skills` under the same name.",
        ]
    )


def rule_frontmatter_description(spec: dict) -> str:
    return (
        f"{spec['product']} standards for {spec['focus']}. "
        f"Use when editing this stack. {spec['updated_for']}."
    )


def catalog_paths(spec: dict) -> dict[str, dict[str, str]]:
    stack = spec["id"]
    skill = spec["skill_name"]
    return {
        "standards": {
            "cursor": f"cursor/{stack}/{stack}-rules.mdc",
            "copilot": f"copilot/{stack}/{stack}-rules.instructions.md",
            "claude": f"claude/{stack}/{stack}-rules.md",
            "windsurf": f"windsurf/{stack}/{stack}-rules.md",
            "cline": f"cline/{stack}/{stack}-rules.md",
            "codex": f"codex/{stack}/{stack}-rules.md",
            "antigravity": f"antigravity/{stack}/{stack}-rules.md",
        },
        "skill": {
            "cursor": f"cursor/{stack}/{skill}/SKILL.md",
            "copilot": f"copilot/{stack}/{skill}/SKILL.md",
            "claude": f"claude/skills/{stack}/{skill}/SKILL.md",
            "windsurf": f"windsurf/{stack}/{skill}/SKILL.md",
            "cline": f"cline/{stack}/{skill}/SKILL.md",
            "codex": f"codex/{stack}/{skill}/SKILL.md",
            "antigravity": f"antigravity/{stack}/{skill}/SKILL.md",
        },
    }


def native_exports(spec: dict) -> dict[str, dict[str, list[dict]]]:
    stack = spec["id"]
    skill = spec["skill_name"]
    rules = f"{stack}-rules"
    paths = spec["paths"]
    globs = ", ".join(paths)
    apply_to = ",".join(paths)
    description = rule_frontmatter_description(spec)
    skill_description = spec["native_skill_description"]
    skill_front = {"name": skill, "description": skill_description}
    cursor_skill = {**skill_front, "paths": paths}
    base = f"release/{stack}/native"
    return {
        "standards": {
            "cursor": [
                {
                    "path": f"{base}/cursor/.cursor/rules/{rules}.mdc",
                    "format": "cursor-rule",
                    "frontmatter": {
                        "description": description,
                        "globs": globs,
                        "alwaysApply": False,
                    },
                }
            ],
            "copilot": [
                {
                    "path": f"{base}/copilot/.github/instructions/{stack}.instructions.md",
                    "format": "copilot-instructions",
                    "frontmatter": {"applyTo": apply_to},
                }
            ],
            "claude": [
                {
                    "path": f"{base}/claude/.claude/rules/{rules}.md",
                    "format": "claude-rule",
                    "frontmatter": {"paths": paths},
                }
            ],
            "windsurf": [
                {
                    "path": f"{base}/windsurf/.devin/rules/{rules}.md",
                    "format": "windsurf-rule",
                    "frontmatter": {"description": description, "trigger": "model_decision"},
                },
            ],
            "cline": [
                {
                    "path": f"{base}/cline/.clinerules/{rules}.md",
                    "format": "cline-rule",
                    "frontmatter": {"paths": paths},
                }
            ],
            "codex": [
                {
                    "path": f"{base}/codex/AGENTS.{stack}-section.md",
                    "format": "plain",
                    "banner": "<!-- Append this section to AGENTS.md. Do not replace the existing file. This is project guidance, not a custom agent. -->",
                    "frontmatter": {},
                }
            ],
            "antigravity": [
                {
                    "path": f"{base}/antigravity/GEMINI.{stack}-section.md",
                    "format": "plain",
                    "banner": "<!-- Append this section to GEMINI.md. Do not replace the existing file. /context lists loaded GEMINI.md files. -->",
                    "frontmatter": {},
                }
            ],
        },
        "skill": {
            "cursor": [
                {
                    "path": f"{base}/cursor/.cursor/skills/{skill}/SKILL.md",
                    "format": "cursor-skill",
                    "frontmatter": cursor_skill,
                }
            ],
            "copilot": [
                {
                    "path": f"{base}/copilot/.github/skills/{skill}/SKILL.md",
                    "format": "skill",
                    "frontmatter": skill_front,
                }
            ],
            "claude": [
                {
                    "path": f"{base}/claude/.claude/skills/{skill}/SKILL.md",
                    "format": "skill",
                    "frontmatter": skill_front,
                }
            ],
            "windsurf": [
                {
                    "path": f"{base}/windsurf/.devin/skills/{skill}/SKILL.md",
                    "format": "skill",
                    "frontmatter": skill_front,
                },
            ],
            "cline": [
                {
                    "path": f"{base}/cline/.cline/skills/{skill}/SKILL.md",
                    "format": "skill",
                    "frontmatter": skill_front,
                }
            ],
            "codex": [
                {
                    "path": f"{base}/agents/.agents/skills/{skill}/SKILL.md",
                    "format": "skill",
                    "frontmatter": skill_front,
                }
            ],
            "antigravity": [
                {
                    "path": f"{base}/agents/.agents/skills/{skill}/SKILL.md",
                    "format": "skill",
                    "frontmatter": skill_front,
                }
            ],
        },
    }


def require(spec: dict, key: str) -> None:
    if key not in spec or spec[key] in ("", [], None):
        raise SystemExit(f"{spec.get('id', '?')}: missing {key}")


def validate_spec(spec: dict) -> None:
    for key in (
        "id",
        "order",
        "product",
        "focus",
        "updated_for",
        "libs",
        "tags",
        "paths",
        "skill_name",
        "skill_label",
        "native_skill_description",
    ):
        require(spec, key)
    if not spec["root"].joinpath("standards.md").is_file():
        raise SystemExit(f"{spec['id']}: missing standards.md")
    if not spec["root"].joinpath("skill.md").is_file():
        raise SystemExit(f"{spec['id']}: missing skill.md")
    if len(spec["tags"]) > 11:
        raise SystemExit(f"{spec['id']}: too many tags")
    if len(spec["native_skill_description"]) > 1024:
        raise SystemExit(f"{spec['id']}: native skill description is too long")
    if "Do not use" not in spec["native_skill_description"]:
        raise SystemExit(f"{spec['id']}: native skill description needs a Do not use clause")
    globs = ", ".join(spec["paths"])
    if len(globs) > 200:
        raise SystemExit(f"{spec['id']}: cursor globs are {len(globs)} characters")
    if len(spec["skill_name"]) > 64:
        raise SystemExit(f"{spec['id']}: skill name exceeds 64 characters")
    for tool in TOOLS:
        for title, description in (
            (standards_title(tool, spec), standards_description(tool, spec)),
            (skill_title(tool, spec), skill_catalog_description(tool, spec)),
        ):
            if not 4 <= len(title) <= 120:
                raise SystemExit(f"{spec['id']} {tool}: title length {len(title)}: {title}")
            if not 20 <= len(description) <= 400:
                raise SystemExit(f"{spec['id']} {tool}: description length {len(description)}")
        tested = [TESTED[tool]]
        if spec.get("fixture"):
            tested.append(FIXTURE)
        for item in tested:
            if not 2 <= len(item) <= 80:
                raise SystemExit(f"{spec['id']} {tool}: tested_with length {len(item)}")
        if len(rule_frontmatter_description(spec)) > 500:
            raise SystemExit(f"{spec['id']}: native rule description is too long")


def entries_for(spec: dict) -> list[dict]:
    paths = catalog_paths(spec)
    exports = native_exports(spec)
    built: list[dict] = []
    for tool in TOOLS:
        tested = [TESTED[tool]]
        if spec.get("fixture"):
            tested.append(FIXTURE)
        built.append(
            {
                "tool": tool,
                "role": "standards",
                "type": "instruction" if tool == "copilot" else "rule",
                "id": f"{tool}-{spec['id']}-rules",
                "catalog_path": paths["standards"][tool],
                "title": standards_title(tool, spec),
                "description": standards_description(tool, spec),
                "tested_with": tested,
                "tags": spec["tags"],
                "exports": exports["standards"][tool],
                "extra": {"globs": ", ".join(spec["paths"]), "alwaysApply": False} if tool == "cursor" else {},
            }
        )
        skill_tags = list(spec["tags"])
        kind = spec.get("skill_tag")
        if kind and kind not in skill_tags and len(skill_tags) < 12:
            skill_tags.append(kind)
        built.append(
            {
                "tool": tool,
                "role": "skill",
                "type": "skill",
                "id": f"{tool}-{spec['skill_name']}",
                "catalog_path": paths["skill"][tool],
                "title": skill_title(tool, spec),
                "description": skill_catalog_description(tool, spec),
                "tested_with": tested,
                "tags": skill_tags,
                "exports": exports["skill"][tool],
                "extra": {},
            }
        )
    return built


def render_entry(spec: dict, item: dict) -> str:
    standards = (spec["root"] / "standards.md").read_text(encoding="utf-8")
    skill = (spec["root"] / "skill.md").read_text(encoding="utf-8")
    body = standards if item["role"] == "standards" else skill
    title = item["title"]
    if item["role"] == "skill" and item["tool"] in {"codex", "antigravity"}:
        heading = f"# {spec['product']} {spec['skill_label']}"
    else:
        heading = f"# {title}"
    native = join_sections([heading, host_line(item["tool"], spec, item["role"]), body])
    preamble = join_sections(
        [
            f"# {title}",
            install_section(item["tool"], spec, item["role"]),
        ]
    )
    catalog = emit_frontmatter(
        {
            "id": item["id"],
            "slug": catalog_slug(item["catalog_path"]),
            "title": title,
            "description": item["description"],
            "type": item["type"],
            "tools": [item["tool"]],
            "stack": spec["id"],
            "tags": item["tags"],
            "author": AUTHOR,
            "license": "MIT",
            "origin": "original",
            "version": "1.0.0",
            "tested_with": item["tested_with"],
            "created": CREATED,
            "updated": CREATED,
            "libs": spec["libs"],
            "updated_for": spec["updated_for"],
            **item["extra"],
        },
        CATALOG_FRONT_ORDER,
    )
    catalog += "\n" + join_sections([preamble, MARKER, native])
    return catalog, native


def content_index(groups: list[tuple[dict, list[dict]]]) -> dict:
    entries = []
    for spec, items in groups:
        for item in items:
            entries.append(
                {
                    "catalog": item["catalog_path"],
                    "tool": item["tool"],
                    "role": item["role"],
                    "type": item["type"],
                    "stack": spec["id"],
                }
            )
    claude_rules = [
        row for row in entries if row["tool"] == "claude" and row["role"] == "standards"
    ]
    return {
        "note": (
            "All release catalog files, including Claude standards at "
            "claude/<stack>/<stack>-rules.md. A filename scan that only accepts "
            "CLAUDE.md skips those 30. presets-web still has to read this index."
        ),
        "count": len(entries),
        "claude_standards": len(claude_rules),
        "entries": entries,
    }


def mapping_markdown(rows: list[tuple[dict, dict]]) -> str:
    lines = [
        "# Native install map",
        "",
        "Generated from `masters/*/stack.json`. Install the native file, not the catalog source.",
        "Catalog frontmatter is presets.dev metadata.",
        "",
        "Windsurf installs only under `.devin/` for current Devin. Do not also copy the file into `.windsurf/`.",
        "Codex standards append to `AGENTS.md`. Antigravity CLI standards append to `GEMINI.md` or `AGENTS.md`. Do not replace those files.",
        "Codex and Antigravity CLI share one skill file at `release/<stack>/native/agents/.agents/skills/<skill>/SKILL.md`. Install it once. Do not also put the Cursor copy at `.agents/skills` under the same name.",
        "",
        "| Stack | Tool | Role | Catalog | Install |",
        "| --- | --- | --- | --- | --- |",
    ]
    for spec, item in rows:
        for exported in item["exports"]:
            lines.append(
                f"| {spec['id']} | {item['tool']} | {item['role']} | `{item['catalog_path']}` | `{exported['path']}` |"
            )
    lines.append("")
    return "\n".join(lines)


def stacks_document(groups: list[tuple[dict, list[dict]]]) -> dict:
    return {
        "release": "original-2026-11",
        "tools": list(TOOLS),
        "note": (
            "Each complete stack has one standards file and one SKILL.md for every tool. "
            "Support files and native exports are not catalog entries. "
            "antigravity is Antigravity CLI, which replaced Gemini CLI for personal accounts. "
            "The index is stacks.json because manifest.json is gitignored."
        ),
        "stacks": [
            {
                "id": spec["id"],
                "status": "complete",
                "entries": [
                    {
                        "catalog": item["catalog_path"],
                        "tool": item["tool"],
                        "role": item["role"],
                        "type": item["type"],
                        "exports": [exported["path"] for exported in item["exports"]],
                    }
                    for item in items
                ],
            }
            for spec, items in groups
        ],
    }


def build() -> dict[str, str]:
    files: dict[str, str] = {}
    groups: list[tuple[dict, list[dict]]] = []
    rows: list[tuple[dict, dict]] = []
    seen_ids: set[str] = set()
    seen_skills: set[str] = set()
    for spec in load_stacks():
        validate_spec(spec)
        if spec["id"] in seen_ids:
            raise SystemExit(f"duplicate stack {spec['id']}")
        if spec["skill_name"] in seen_skills:
            raise SystemExit(f"duplicate skill name {spec['skill_name']}")
        seen_ids.add(spec["id"])
        seen_skills.add(spec["skill_name"])
        items = entries_for(spec)
        groups.append((spec, items))
        for item in items:
            catalog, native = render_entry(spec, item)
            files[item["catalog_path"]] = catalog
            for exported in item["exports"]:
                kind = exported["format"]
                keys = list(exported.get("frontmatter", {}))
                if set(keys) != set(FORMAT_KEYS[kind]):
                    raise SystemExit(f"{exported['path']}: frontmatter keys {keys}")
                if kind == "plain":
                    body = join_sections([exported["banner"], native_body_from_catalog(catalog)])
                else:
                    body = emit_frontmatter(exported["frontmatter"], NATIVE_ORDER[kind])
                    body += "\n" + native_body_from_catalog(catalog)
                if kind == "windsurf-rule" and len(body) > 12000:
                    raise SystemExit(
                        f"{exported['path']}: {len(body)} characters exceeds the 12000 Cascade rule limit"
                    )
                previous = files.get(exported["path"])
                if previous is not None and previous != body:
                    raise SystemExit(f"{exported['path']}: two tools wrote different contents")
                files[exported["path"]] = body
            rows.append((spec, item))
    files["release/original-2026-11/stacks.json"] = json.dumps(stacks_document(groups), indent=2) + "\n"
    files["release/original-2026-11/content-index.json"] = json.dumps(content_index(groups), indent=2) + "\n"
    files["release/README.md"] = mapping_markdown(rows)
    return files


def native_body_from_catalog(catalog: str) -> str:
    marker = f"{MARKER}\n\n"
    index = catalog.find(marker)
    if index == -1:
        raise SystemExit("catalog file is missing the native marker")
    return catalog[index + len(marker) :]


# Written by the retirement pass, not by the generator.
KEEP_RELEASE = {"release/original-2026-11/retirement-map.json"}


def managed_orphans(expected: set[str]) -> list[str]:
    orphans: list[str] = []
    release = ROOT / "release"
    if release.is_dir():
        for path in release.rglob("*"):
            if path.is_file():
                rel = path.relative_to(ROOT).as_posix()
                if rel not in expected and rel not in KEEP_RELEASE:
                    orphans.append(rel)
    for tool in (*TOOLS, *RETIRED_TOOLS):
        base = ROOT / tool
        if not base.is_dir():
            continue
        for path in base.rglob("*"):
            if not path.is_file():
                continue
            if path.suffix.lower() not in {".md", ".mdc"}:
                continue
            rel = path.relative_to(ROOT).as_posix()
            if rel in expected:
                continue
            text = path.read_text(encoding="utf-8", errors="ignore")
            if MARKER in text:
                orphans.append(rel)
    return sorted(set(orphans))


def remove_empty_dirs(start: Path) -> None:
    if not start.is_dir():
        return
    for path in sorted(start.rglob("*"), reverse=True):
        if path.is_dir():
            try:
                path.rmdir()
            except OSError:
                pass


def main() -> int:
    check = "--check" in sys.argv
    files = build()
    expected = set(files)
    mismatches: list[str] = []
    orphans = managed_orphans(expected)
    if check:
        for rel, text in files.items():
            path = ROOT / rel
            current = path.read_text(encoding="utf-8") if path.is_file() else None
            if current != text:
                mismatches.append(rel)
        if mismatches or orphans:
            print("release files drifted:")
            print("\n".join(mismatches + [f"orphan {rel}" for rel in orphans]))
            print("run: python scripts/assemble_release.py")
            return 1
        print(f"release matches: {len(files)} file(s), {len(files) - 2} generated content file(s)")
        return 0
    for rel, text in files.items():
        path = ROOT / rel
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(text, encoding="utf-8")
    for rel in orphans:
        path = ROOT / rel
        if path.is_file():
            path.unlink()
    remove_empty_dirs(ROOT / "release")
    for tool in (*TOOLS, *RETIRED_TOOLS):
        remove_empty_dirs(ROOT / tool)
    print(f"release wrote: {len(files)} file(s); removed {len(orphans)} orphan(s)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
