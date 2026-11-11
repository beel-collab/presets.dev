# Next.js Claude Code Skill for a Tenant Cache Audit

A Claude Code skill for a Next.js tenant-cache and Server Action audit. The slash command is `/nextjs-tenant-cache-audit`. Claude can also load it when the description matches the request.

## Install

The project path is `.claude/skills/nextjs-tenant-cache-audit/SKILL.md`. The catalog copy lives under `claude/skills/nextjs/` because that is this repository's layout. The installed folder name is the skill name, one level below `.claude/skills/`.

Native frontmatter is `name` and `description` only. `allowed-tools` would pre-approve tools for the invoking turn, which is a permission grant, not a sandbox. This audit stays on the normal permission prompts. Do not add `Bash` or `Edit` there to make the audit "automatic".

`description` is what Claude lists, and the listing truncates the combined description around 1,536 characters. The native description is much shorter and states the non-trigger.

A personal skill of the same command name can hide the project skill. Check `/` after install and keep the project file if both appear.

## What was checked

Skill location, `name`, and `description` were compared with the Claude Code skills document on 11 November 2026. Claude Code was not started. The decision table was run with the Node fixture only.
