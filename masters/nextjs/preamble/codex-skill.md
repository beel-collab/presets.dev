# Next.js Codex Skill for a Tenant Cache Audit

A Codex skill for the phrases "codex skill nextjs" and "codex next js skills": a tenant-cache and Server Action audit, not a general Next.js tutorial. Invoke it with `$nextjs-tenant-cache-audit` or `/skills`. Codex can also select it when the description matches.

## Install

The repository path is `.agents/skills/nextjs-tenant-cache-audit/SKILL.md`. Codex scans `.agents/skills` from the working directory up to the repo root. `~/.agents/skills` is the user scope. This release does not use `.codex/skills` as the canonical project path, and it does not use the deprecated `~/.codex/prompts/` files.

`name` and `description` are required. The description leads with the audit so it still matches if Codex shortens skill descriptions to fit the skills list. No `agents/openai.yaml` is included. Implicit invocation stays at the default. The description tells Codex when not to run the skill.

If two skills share `name`, Codex does not merge them. Both can show up in the picker. Install this folder once. Cursor and Gemini CLI also read `.agents/skills`, so a checkout that installs every tool's variant into that shared directory will mix hosts. Keep the Cursor skill under `.cursor/skills/` and the Gemini CLI skill under `.gemini/skills/`.

Restart Codex if a new skill does not appear.

## What was checked

Codex's skills document and the `AGENTS.md` guide were read on 11 November 2026. Codex was not started. The decision table was run with the Node fixture only.
