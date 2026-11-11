# Next.js Codex Instructions for Server Actions and Caching

Project guidance for Codex on a Next.js App Router. Codex reads `AGENTS.md`. That file is concatenated instructions, not a custom agent profile, so this catalog entry is `type: rule`.

## Install

Append the native section to the repository `AGENTS.md`. Do not replace a file that already has other guidance. Codex reads `AGENTS.override.md` first in each directory and then ignores `AGENTS.md` there, so an override silences this section. Use an override only when you mean to replace the whole directory's instructions.

Discovery walks from the Git root down to the working directory and stops at `project_doc_max_bytes`, 32 KiB by default. A long `AGENTS.md` can drop this section. Keep the section near the end of the root file, or place a copy in the app directory if that is where Codex is launched. Restart Codex after an edit. The instruction chain is built at the start of a run.

Personal prompts in `~/.codex/prompts/` are deprecated. Do not put this guidance there.

The audit procedure is a skill at `.agents/skills/nextjs-tenant-cache-audit/SKILL.md`, invoked with `$nextjs-tenant-cache-audit` or `/skills`. Install that skill only for Codex. Cursor and Gemini CLI also discover `.agents/skills`, and a second copy with the same folder name is ambiguous.

## What was checked

Codex's `AGENTS.md` discovery document and skills document were read on 11 November 2026. Codex was not started. The decision table was run with the Node fixture named in the section text. Observed suggestion phrases for this stack include "codex skill nextjs" and "codex next js skills". Those phrases belong to the skill entry.
