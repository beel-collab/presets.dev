# Next.js Cursor Skill for a Tenant Cache Audit

A Cursor Agent Skill for the Next.js tenant-cache and Server Action audit. Invoke it with `/nextjs-tenant-cache-audit`, or let Agent load it when the request matches the description and the open files match `paths`.

## Install

The native folder is `.cursor/skills/nextjs-tenant-cache-audit/SKILL.md`. `name` matches the folder. Cursor also discovers `.agents/skills/` and Claude and Codex skill directories. Do not copy this folder into `.agents/skills/` when a Codex skill with the same name is already there. Install the Cursor copy only.

`paths` limits when the skill is surfaced. A request that never touches a matching file will not auto-select it. Use the slash command in that case. `disable-model-invocation` is left unset so a clear audit request can select the skill.

This catalog file's frontmatter is not the skill frontmatter. Cursor wants `name`, `description`, and optional `paths`.

## What was checked

The skill fields were compared with the Cursor skills document on 11 November 2026. Cursor was not opened. The procedure's decision table was run with the Node fixture, which does not execute the skill inside Cursor.
