# Next.js Copilot Skill for a Tenant Cache Audit

A GitHub Copilot skill that audits Next.js Server Actions and tenant cache keys. The description is the trigger. Copilot injects `SKILL.md` when the request matches. You can also call it by the skill name where the surface lists skills.

## Install

The project path is `.github/skills/nextjs-tenant-cache-audit/SKILL.md`. Copilot also looks at `.claude/skills/` and `.agents/skills/` in the repository, and at personal folders under `~/.copilot/skills/` and `~/.agents/skills/`. Put this skill in `.github/skills/` only. A second folder with the same `name` makes the winner depend on the surface.

`name` is required, lowercase, at most 64 characters, and matches the directory. `description` is required and stays under 1,024 characters. The native file sets those two fields and no permission grant.

Cloud sessions, Copilot CLI, and the IDE do not all see the same skill roots. This preset was not executed in any of them. A cloud-agent run would not prove IDE behavior.

## What was checked

The skill shape was compared with GitHub's Copilot CLI skill guide and the agent-skills concept page on 11 November 2026. The decision table was run with the Node fixture only.
