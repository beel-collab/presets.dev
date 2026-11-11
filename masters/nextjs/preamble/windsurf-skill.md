# Next.js Windsurf Skill for a Tenant Cache Audit

An on-demand audit skill, with two install paths because the product split. Current Devin CLI loads `.devin/skills/<name>/SKILL.md` and invokes it as `/nextjs-tenant-cache-audit`. Devin also imports legacy `.windsurf/skills/`. The native export writes both folders with the same `name`, `description`, and body.

## Install

Prefer `.devin/skills/nextjs-tenant-cache-audit/SKILL.md` on a current Devin CLI. Add `.windsurf/skills/nextjs-tenant-cache-audit/SKILL.md` when you still run Cascade or you want the import path filled. Do not point the two folders at different text.

Devin's default `triggers` are user and model. This export leaves `triggers` unset so that default stands, and it does not set `allowed-tools` or `permissions`. Those fields auto-approve tools. The audit should keep the client's normal prompts.

`name` defaults to the directory. It is set anyway so the slash command is obvious. This is not a Devin subagent: `subagent` stays off, and there is no file under `.devin/agents/`.

Cascade was not opened and Devin CLI was not started. Windsurf's older skills URL now serves Devin's customization docs, so the legacy path is documented as an import source rather than as a client this release executed.

## What was checked

Devin's skill frontmatter and the configuration-import page were read on 11 November 2026. The decision table was run with the Node fixture only.
