---
id: "codex-svelte-code-review"
slug: "codex/svelte/svelte-code-review/SKILL"
title: "Svelte Code Review Skill for Codex"
description: "Codex skill for a Svelte code review. Use when you want that code review on a Svelte change. Do not use it for a different stack."
type: "skill"
tools:
  - "codex"
stack: "svelte"
tags:
  - "svelte"
  - "sveltekit"
  - "runes"
  - "code-review"
author:
  name: "presets.dev"
  github: "beel-collab"
license: "MIT"
origin: "original"
version: "1.0.0"
tested_with:
  - "Codex docs 2026-11-11; CLI not executed"
created: "2026-11-11"
updated: "2026-11-11"
libs:
  - "svelte@5.57.3"
  - "@sveltejs/kit@3.2.0"
updated_for: "Svelte 5.57.3 and SvelteKit 3.2.0, Nov 2026"
---

# Svelte Code Review Skill for Codex

## Install

Install the native export at `.agents/skills/svelte-code-review/SKILL.md`.
Copy that export, not this catalog file. Catalog fields such as `tools` and `author` are for presets.dev.
Install one tool's skill for a checkout. Do not drop every tool's copy into `.agents/skills` under the same name.

<!-- native:start -->

# Svelte Code Review Skill for Codex

Codex skill `svelte-code-review` for Svelte. Call it with `$svelte-code-review` or `/skills`. Do not install the other tools' copies beside it.

## When to run

Run this review for a Svelte component, a SvelteKit load or action, or a config change.

## When to leave it

Stop for a non-Svelte repository. Do not upgrade Svelte or Kit unless the user asked.

## Steps

1. Read the Svelte and Kit majors. Svelte 4 syntax in a rune component, or a Kit 2 config key on Kit 3, is a high finding.
2. Search for module-level mutable state in server code. User data stored there is a high finding.
3. Check `+page.ts` and `.svelte` files for a server-only import. That is a high finding.
4. Check `{@html}`, form actions that trust a hidden user id, and `$effect` loops.
5. Look for a hydration hazard: `window` or `Math.random` during init.
6. Run the project's test command only if the user asked. Otherwise write `not run`.

## Output

Findings with severity, file, line, the boundary that broke, and a fix. Include both majors.

## Stop

Stop when the user asks you to convert the whole app to runes or to Kit 3 in one review.
