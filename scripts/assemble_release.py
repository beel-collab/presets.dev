#!/usr/bin/env python3
"""Build the original-release catalog files and native install payloads.

Masters under masters/ are the source. Catalog files are what the site indexes.
Native files under release/ are what a project should install. Catalog frontmatter
is never copied into a native file.
"""

from __future__ import annotations

import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
STACK = "nextjs"
UPDATED_FOR = "Next.js 16.4.6, security fixes since 16.4.5 (2026-11-11)"
CREATED = "2026-11-11"
SKILL_NAME = "nextjs-tenant-cache-audit"
MARKER = "<!-- native:start -->"
PATHS = [
    "app/**/*.ts",
    "app/**/*.tsx",
    "src/app/**/*.ts",
    "src/app/**/*.tsx",
    "next.config.ts",
    "next.config.mjs",
    "next.config.js",
]
CURSOR_GLOBS = ", ".join(PATHS)
COPILOT_APPLY = ",".join(PATHS)
RULE_DESCRIPTION = (
    "Next.js App Router standards for validated Server Actions and tenant-safe caching. "
    "Use when editing routes, actions, cache helpers, or Next.js config."
)
SKILL_DESCRIPTION = (
    "Audit Next.js App Router Server Actions and Cache Components for tenant leaks "
    "and missing authentication. Use for a nextjs cache audit, a tenant isolation review, "
    "a Server Action review, or the November 2026 Next.js cache advisories. "
    "Do not use for CSS, new marketing pages, Playwright tests, or repositories that are not Next.js."
)
AUTHOR = {"name": "presets.dev", "github": "beel-collab"}
TAGS = ["nextjs", "typescript", "server-actions", "caching", "app-router"]
SKILL_TAGS = TAGS + ["audit"]
LIBS = ["next@16.4.6"]
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


def read(rel: str) -> str:
    return (ROOT / rel).read_text(encoding="utf-8").strip() + "\n"


def join_sections(parts: list[str]) -> str:
    cleaned = [part.strip() for part in parts if part.strip()]
    return "\n\n".join(cleaned) + "\n"


def catalog_slug(rel: str) -> str:
    if rel.endswith(".mdc"):
        return rel[:-4]
    if rel.endswith(".md"):
        return rel[:-3]
    raise ValueError(rel)


def entry(
    *,
    tool: str,
    role: str,
    type_name: str,
    catalog_path: str,
    title: str,
    description: str,
    tested_with: str,
    exports: list[dict],
    extra: dict | None = None,
) -> dict:
    return {
        "tool": tool,
        "role": role,
        "type": type_name,
        "id": f"{tool}-nextjs-{ 'tenant-cache-audit' if role == 'skill' else 'app-router-caching' }",
        "catalog_path": catalog_path,
        "title": title,
        "description": description,
        "tested_with": [tested_with, FIXTURE],
        "tags": SKILL_TAGS if role == "skill" else TAGS,
        "preamble": f"masters/nextjs/preamble/{tool}-{role}.md",
        "host": f"masters/nextjs/host/{tool}-{role}.md",
        "body": "masters/nextjs/skill.md" if role == "skill" else "masters/nextjs/standards.md",
        "extra": extra or {},
        "exports": exports,
    }


def native_skill(tool_dir: str, frontmatter: dict, install_suffix: str) -> dict:
    return {
        "path": f"release/nextjs/native/{tool_dir}/{install_suffix}",
        "format": "cursor-skill" if "paths" in frontmatter else "skill",
        "frontmatter": frontmatter,
    }


ENTRIES = [
    entry(
        tool="cursor",
        role="standards",
        type_name="rule",
        catalog_path="cursor/nextjs/app-router-caching.mdc",
        title="Next.js Cursor Rules for Server Actions and Safe Caching",
        description=(
            "Cursor rules for Next.js TypeScript App Router projects: validated Server Actions "
            "and tenant-safe caching on 16.4.6. Use when editing routes, actions, or cached server data."
        ),
        tested_with="Cursor docs 2026-11-11; app not executed",
        extra={"globs": CURSOR_GLOBS, "alwaysApply": False},
        exports=[
            {
                "path": "release/nextjs/native/cursor/.cursor/rules/nextjs-app-router-caching.mdc",
                "format": "cursor-rule",
                "frontmatter": {
                    "description": RULE_DESCRIPTION,
                    "globs": CURSOR_GLOBS,
                    "alwaysApply": False,
                },
            }
        ],
    ),
    entry(
        tool="copilot",
        role="standards",
        type_name="instruction",
        catalog_path="copilot/nextjs/app-router-caching.instructions.md",
        title="Next.js Copilot Instructions for Server Actions and Caching",
        description=(
            "Copilot instructions for Next.js App Router projects: validated Server Actions "
            "and tenant-safe caching on 16.4.6. Use when editing routes, actions, or cached server data."
        ),
        tested_with="Copilot docs 2026-11-11; app not executed",
        exports=[
            {
                "path": "release/nextjs/native/copilot/.github/instructions/nextjs-app-router-caching.instructions.md",
                "format": "copilot-instructions",
                "frontmatter": {"applyTo": COPILOT_APPLY},
            }
        ],
    ),
    entry(
        tool="claude",
        role="standards",
        type_name="rule",
        catalog_path="claude/nextjs/app-router-caching.md",
        title="Next.js Claude Code Rules for Server Actions and Caching",
        description=(
            "Claude Code rules for Next.js App Router projects: validated Server Actions "
            "and tenant-safe caching on 16.4.6. Use when editing routes, actions, or cached server data."
        ),
        tested_with="Claude Code docs 2026-11-11; CLI not run",
        exports=[
            {
                "path": "release/nextjs/native/claude/.claude/rules/nextjs-app-router-caching.md",
                "format": "claude-rule",
                "frontmatter": {"paths": PATHS},
            }
        ],
    ),
    entry(
        tool="windsurf",
        role="standards",
        type_name="rule",
        catalog_path="windsurf/nextjs/app-router-caching.md",
        title="Next.js Windsurf Rules for Server Actions and Safe Caching",
        description=(
            "Windsurf and Devin rules for Next.js App Router projects: validated Server Actions "
            "and tenant-safe caching on 16.4.6. Use when editing routes, actions, or cached server data."
        ),
        tested_with="Devin and Cascade docs 2026-11-11; not run",
        exports=[
            {
                "path": "release/nextjs/native/windsurf/.devin/rules/nextjs-app-router-caching.md",
                "format": "windsurf-rule",
                "frontmatter": {"description": RULE_DESCRIPTION, "trigger": "model_decision"},
            },
            {
                "path": "release/nextjs/native/windsurf/.windsurf/rules/nextjs-app-router-caching.md",
                "format": "windsurf-rule",
                "frontmatter": {"description": RULE_DESCRIPTION, "trigger": "model_decision"},
            },
        ],
    ),
    entry(
        tool="cline",
        role="standards",
        type_name="rule",
        catalog_path="cline/nextjs/app-router-caching.md",
        title="Next.js Cline Rules for Server Actions and Safe Caching",
        description=(
            "Cline rules for Next.js App Router projects: validated Server Actions and "
            "tenant-safe caching on 16.4.6. Use when editing routes, actions, or cached server data."
        ),
        tested_with="Cline docs 2026-11-11; app not executed",
        exports=[
            {
                "path": "release/nextjs/native/cline/.clinerules/nextjs-app-router-caching.md",
                "format": "cline-rule",
                "frontmatter": {"paths": PATHS},
            }
        ],
    ),
    entry(
        tool="codex",
        role="standards",
        type_name="rule",
        catalog_path="codex/nextjs/app-router-caching.md",
        title="Next.js Codex Instructions for Server Actions and Caching",
        description=(
            "Codex project guidance for Next.js App Router work: validated Server Actions "
            "and tenant-safe caching on 16.4.6. Append it to AGENTS.md. It is not a custom agent."
        ),
        tested_with="Codex docs 2026-11-11; CLI not executed",
        exports=[
            {
                "path": "release/nextjs/native/codex/AGENTS.nextjs-section.md",
                "format": "plain",
                "banner": "<!-- Append this section to AGENTS.md. Do not replace the existing file. This is project guidance, not a custom agent. -->",
                "frontmatter": {},
            }
        ],
    ),
    entry(
        tool="gemini-cli",
        role="standards",
        type_name="rule",
        catalog_path="gemini-cli/nextjs/app-router-caching.md",
        title="Next.js Gemini CLI Rules for Server Actions and Caching",
        description=(
            "Gemini CLI context for Next.js App Router projects: validated Server Actions "
            "and tenant-safe caching on 16.4.6. Append it to GEMINI.md instead of replacing that file."
        ),
        tested_with="Gemini CLI docs 2026-11-11; CLI not run",
        exports=[
            {
                "path": "release/nextjs/native/gemini-cli/GEMINI.nextjs-section.md",
                "format": "plain",
                "banner": "<!-- Append this section to GEMINI.md. Do not replace the existing file. Confirm with /memory show. -->",
                "frontmatter": {},
            }
        ],
    ),
    entry(
        tool="cursor",
        role="skill",
        type_name="skill",
        catalog_path=f"cursor/nextjs/{SKILL_NAME}/SKILL.md",
        title="Next.js Cursor Skill for a Tenant Cache Audit",
        description=(
            "Cursor skill that audits Next.js Server Actions and tenant cache keys on 16.4.6. "
            "Use for a cache or authentication review. Skip it for styling and non-Next.js apps."
        ),
        tested_with="Cursor docs 2026-11-11; app not executed",
        exports=[
            native_skill(
                "cursor",
                {"name": SKILL_NAME, "description": SKILL_DESCRIPTION, "paths": PATHS},
                f".cursor/skills/{SKILL_NAME}/SKILL.md",
            )
        ],
    ),
    entry(
        tool="copilot",
        role="skill",
        type_name="skill",
        catalog_path=f"copilot/nextjs/{SKILL_NAME}/SKILL.md",
        title="Next.js Copilot Skill for a Tenant Cache Audit",
        description=(
            "Copilot skill that audits Next.js Server Actions and tenant cache keys on 16.4.6. "
            "Use for a cache or authentication review. Skip it for styling and non-Next.js apps."
        ),
        tested_with="Copilot docs 2026-11-11; app not executed",
        exports=[
            native_skill(
                "copilot",
                {"name": SKILL_NAME, "description": SKILL_DESCRIPTION},
                f".github/skills/{SKILL_NAME}/SKILL.md",
            )
        ],
    ),
    entry(
        tool="claude",
        role="skill",
        type_name="skill",
        catalog_path=f"claude/skills/nextjs/{SKILL_NAME}/SKILL.md",
        title="Next.js Claude Code Skill for a Tenant Cache Audit",
        description=(
            "Claude Code skill that audits Next.js Server Actions and tenant cache keys on 16.4.6. "
            "Use for a cache or authentication review. Skip it for styling and non-Next.js apps."
        ),
        tested_with="Claude Code docs 2026-11-11; CLI not run",
        exports=[
            native_skill(
                "claude",
                {"name": SKILL_NAME, "description": SKILL_DESCRIPTION},
                f".claude/skills/{SKILL_NAME}/SKILL.md",
            )
        ],
    ),
    entry(
        tool="windsurf",
        role="skill",
        type_name="skill",
        catalog_path=f"windsurf/nextjs/{SKILL_NAME}/SKILL.md",
        title="Next.js Windsurf Skill for a Tenant Cache Audit",
        description=(
            "Windsurf and Devin skill that audits Next.js Server Actions and tenant cache keys on 16.4.6. "
            "Use for a cache or authentication review. Skip it for styling and non-Next.js apps."
        ),
        tested_with="Devin and Cascade docs 2026-11-11; not run",
        exports=[
            native_skill(
                "windsurf",
                {"name": SKILL_NAME, "description": SKILL_DESCRIPTION},
                f".devin/skills/{SKILL_NAME}/SKILL.md",
            ),
            native_skill(
                "windsurf",
                {"name": SKILL_NAME, "description": SKILL_DESCRIPTION},
                f".windsurf/skills/{SKILL_NAME}/SKILL.md",
            ),
        ],
    ),
    entry(
        tool="cline",
        role="skill",
        type_name="skill",
        catalog_path=f"cline/nextjs/{SKILL_NAME}/SKILL.md",
        title="Next.js Cline Skill for a Tenant Cache Audit",
        description=(
            "Cline skill that audits Next.js Server Actions and tenant cache keys on 16.4.6. "
            "Use for a cache or authentication review. Skip it for styling and non-Next.js apps."
        ),
        tested_with="Cline docs 2026-11-11; app not executed",
        exports=[
            native_skill(
                "cline",
                {"name": SKILL_NAME, "description": SKILL_DESCRIPTION},
                f".cline/skills/{SKILL_NAME}/SKILL.md",
            )
        ],
    ),
    entry(
        tool="codex",
        role="skill",
        type_name="skill",
        catalog_path=f"codex/nextjs/{SKILL_NAME}/SKILL.md",
        title="Next.js Codex Skill for a Tenant Cache Audit",
        description=(
            "Codex skill for Next.js that audits Server Actions and tenant-safe cache keys. "
            "Use when the request is a codex skill nextjs review, not a styling or Playwright task."
        ),
        tested_with="Codex docs 2026-11-11; CLI not executed",
        exports=[
            native_skill(
                "codex",
                {"name": SKILL_NAME, "description": SKILL_DESCRIPTION},
                f".agents/skills/{SKILL_NAME}/SKILL.md",
            )
        ],
    ),
    entry(
        tool="gemini-cli",
        role="skill",
        type_name="skill",
        catalog_path=f"gemini-cli/nextjs/{SKILL_NAME}/SKILL.md",
        title="Next.js Gemini CLI Skill for a Tenant Cache Audit",
        description=(
            "Gemini CLI skill that audits Next.js Server Actions and tenant cache keys on 16.4.6. "
            "Use for a cache or authentication review. Skip it for styling and non-Next.js apps."
        ),
        tested_with="Gemini CLI docs 2026-11-11; CLI not run",
        exports=[
            native_skill(
                "gemini-cli",
                {"name": SKILL_NAME, "description": SKILL_DESCRIPTION},
                f".gemini/skills/{SKILL_NAME}/SKILL.md",
            )
        ],
    ),
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


def validate_entry(item: dict) -> None:
    title = item["title"]
    description = item["description"]
    if not 4 <= len(title) <= 120:
        raise SystemExit(f"{item['id']}: title length {len(title)}")
    if not 20 <= len(description) <= 400:
        raise SystemExit(f"{item['id']}: description length {len(description)}")
    for tested in item["tested_with"]:
        if not 2 <= len(tested) <= 80:
            raise SystemExit(f"{item['id']}: tested_with length {len(tested)}")
    if len(CURSOR_GLOBS) > 200:
        raise SystemExit("cursor globs exceed 200 characters")
    if len(SKILL_DESCRIPTION) > 1024:
        raise SystemExit("skill description exceeds 1024 characters")
    if item["role"] == "skill" and not item["catalog_path"].endswith("/SKILL.md"):
        raise SystemExit(f"{item['id']}: skill path must end in SKILL.md")
    for exported in item["exports"]:
        kind = exported["format"]
        if kind not in FORMAT_KEYS:
            raise SystemExit(f"unknown format {kind}")
        keys = list(exported.get("frontmatter", {}))
        if keys != [key for key in NATIVE_ORDER[kind] if key in exported.get("frontmatter", {})]:
            raise SystemExit(f"{exported['path']}: frontmatter key order {keys}")
        if set(keys) != set(FORMAT_KEYS[kind]):
            raise SystemExit(f"{exported['path']}: frontmatter keys {keys}")


def manifest_document(entries: list[dict]) -> dict:
    return {
        "release": "original-2026-11",
        "tools": ["cursor", "copilot", "claude", "windsurf", "cline", "codex", "gemini-cli"],
        "note": (
            "Complete stacks must contain one standards file and one SKILL.md "
            "for every tool in tools. Support files and native exports are not catalog entries. "
            "gemini-cli is Gemini CLI, not antigravity."
        ),
        "stacks": [
            {
                "id": STACK,
                "status": "complete",
                "entries": [
                    {
                        "catalog": item["catalog_path"],
                        "tool": item["tool"],
                        "role": item["role"],
                        "type": item["type"],
                        "exports": [exported["path"] for exported in item["exports"]],
                    }
                    for item in entries
                ],
            }
        ],
    }


def mapping_markdown(entries: list[dict]) -> str:
    lines = [
        "# Next.js native install map",
        "",
        "These files are generated from `masters/nextjs`. Install the native file, not the catalog source.",
        "Catalog frontmatter is presets.dev metadata and is not valid product frontmatter.",
        "",
        "Windsurf ships two copies of the same text: `.devin/` for current Devin CLI and `.windsurf/` for legacy Cascade.",
        "Codex and Gemini CLI standards are sections to append. Do not overwrite an existing `AGENTS.md` or `GEMINI.md`.",
        "Install one tool's skill. Do not place every tool's copy in `.agents/skills` under the same name.",
        "",
        "| Tool | Role | Catalog source | Install file |",
        "| --- | --- | --- | --- |",
    ]
    for item in entries:
        for exported in item["exports"]:
            lines.append(
                f"| {item['tool']} | {item['role']} | `{item['catalog_path']}` | `{exported['path']}` |"
            )
    lines.append("")
    return "\n".join(lines)


def build() -> dict[str, str]:
    sources = read("masters/nextjs/sources.md")
    files: dict[str, str] = {}
    for item in ENTRIES:
        validate_entry(item)
        native_body = join_sections([read(item["host"]), read(item["body"])])
        catalog = emit_frontmatter(
            {
                "id": item["id"],
                "slug": catalog_slug(item["catalog_path"]),
                "title": item["title"],
                "description": item["description"],
                "type": item["type"],
                "tools": [item["tool"]],
                "stack": STACK,
                "tags": item["tags"],
                "author": AUTHOR,
                "license": "MIT",
                "origin": "original",
                "version": "1.0.0",
                "tested_with": item["tested_with"],
                "created": CREATED,
                "updated": CREATED,
                "libs": LIBS,
                "updated_for": UPDATED_FOR,
                **item["extra"],
            },
            CATALOG_FRONT_ORDER,
        )
        catalog += "\n" + join_sections([read(item["preamble"]), sources, MARKER, native_body])
        files[item["catalog_path"]] = catalog
        for exported in item["exports"]:
            kind = exported["format"]
            if kind == "plain":
                body = join_sections([exported["banner"], native_body])
            else:
                body = emit_frontmatter(exported["frontmatter"], NATIVE_ORDER[kind])
                body += "\n" + native_body
            if kind == "windsurf-rule" and len(body) > 12000:
                raise SystemExit(f"{exported['path']}: {len(body)} characters exceeds the 12000 Cascade rule limit")
            files[exported["path"]] = body
    document = manifest_document(ENTRIES)
    files["release/original-2026-11/manifest.json"] = json.dumps(document, indent=2) + "\n"
    files["release/nextjs/native/README.md"] = mapping_markdown(ENTRIES)
    return files


def main() -> int:
    check = "--check" in sys.argv
    files = build()
    mismatches: list[str] = []
    for rel, text in files.items():
        path = ROOT / rel
        if check:
            current = path.read_text(encoding="utf-8") if path.is_file() else None
            if current != text:
                mismatches.append(rel)
            continue
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(text, encoding="utf-8")
    if mismatches:
        print("release files drifted:")
        print("\n".join(mismatches))
        print("run: python scripts/assemble_release.py")
        return 1
    action = "matches" if check else "wrote"
    print(f"release {action}: {len(files)} file(s), {len(ENTRIES)} catalog entries")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
