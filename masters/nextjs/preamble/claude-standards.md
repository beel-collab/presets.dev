# Next.js Claude Code Rules for Server Actions and Caching

A path-scoped Claude Code rule for the Next.js App Router. It covers validated Server Actions and tenant-safe caching, and it stays out of the session until a matching file is read.

## Install

Place the native export at `.claude/rules/nextjs-app-router-caching.md`. Claude Code reads `paths` and ignores other frontmatter keys, so the native file has that list only. Paths are relative to the directory that contains `.claude`. The patterns cover `app/` and `src/app/` TypeScript and the Next config. A path-scoped rule loads when Claude reads or edits a matching file. It does not load for the whole session the way a root `CLAUDE.md` does.

Do not replace an existing `CLAUDE.md` or `CLAUDE.local.md`. If you want a one-line pointer in `CLAUDE.md`, add it by hand. Imports use `@path` outside code fences. This preset does not add an import, because a bad import pulls another file into every session.

The audit procedure is the skill `nextjs-tenant-cache-audit` under `.claude/skills/`. A rule is persistent context. A skill loads when the request matches.

## What was checked

The `paths` field was compared with the Claude Code `CLAUDE.md` and rules document on 11 November 2026. Claude Code was not started. The decision table was run with the Node fixture named in the rule text.
