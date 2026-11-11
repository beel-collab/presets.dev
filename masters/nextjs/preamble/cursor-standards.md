# Next.js Cursor Rules for Server Actions and Safe Caching

Cursor rules for a Next.js TypeScript App Router. The searchable job is "cursor rules nextjs" and "cursor rules nextjs typescript": validated Server Actions and tenant-safe caching.

## Install

The native file belongs at `.cursor/rules/nextjs-app-router-caching.mdc`. Cursor ignores a plain `.md` file in `.cursor/rules` because a project rule needs `description`, `globs`, and `alwaysApply`. Copy the native export, not this catalog file. Catalog keys such as `id`, `slug`, `tools`, and `author` are for presets.dev.

`alwaysApply` is false. The globs cover `app/` and `src/app/` TypeScript plus the Next config, so the rule attaches when one of those files is in context. Mention `@nextjs-app-router-caching` when you want it on a file the globs miss. It does not replace User Rules or Team Rules. Team Rules win when guidance conflicts.

Use the companion skill `nextjs-tenant-cache-audit` for a review that should not sit in every matching edit.

## What was checked

The rule fields were compared with the Cursor rules document on 11 November 2026. The Cursor application was not opened. The decision table was run with the Node fixture named in the rule text.
