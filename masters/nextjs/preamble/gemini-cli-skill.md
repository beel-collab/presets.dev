# Next.js Gemini CLI Skill for a Tenant Cache Audit

A Gemini CLI skill for a Next.js tenant-cache and Server Action audit. Gemini CLI puts `name` and `description` in the prompt, then calls `activate_skill` and shows a consent prompt with the skill name, purpose, and directory. Decline the prompt and the skill body stays out of the turn. Do not pass an install flag that skips consent.

## Install

The workspace path is `.gemini/skills/nextjs-tenant-cache-audit/SKILL.md`. `name` matches the directory. `.agents/skills` is an alias that outranks `.gemini/skills` at the same tier, so this release does not also copy the folder there. A Codex skill already using that alias would win and this file would never run.

List it with `/skills list` or `gemini skills list`. Disable it with `/skills disable nextjs-tenant-cache-audit` rather than deleting the file if you need it gone for one checkout. Workspace scope is the project directory. The user-scope default of those commands is not this file.

A sampled Gemini CLI autocomplete prefix for Next.js skills was empty. The skill is still the on-demand half of the Next.js stack. It is not a `GEMINI.md` section, not a TOML command, and not a preview subagent.

## What was checked

The Gemini CLI skills overview and the creating-skills guide were read on 11 November 2026. Gemini CLI was not started. The decision table was run with the Node fixture only.
