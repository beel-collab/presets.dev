---
id: "codex-svelte-rules"
slug: "codex/svelte/svelte-rules"
title: "Svelte Codex Instructions: Runes, Load Functions and SSR"
description: "Codex instructions for Svelte: Runes, Load Functions and SSR. Append to AGENTS.md. Structure, security, and tests. Svelte 5.57.3 and SvelteKit 3.2.0, Nov 2026."
type: "rule"
tools:
  - "codex"
stack: "svelte"
tags:
  - "svelte"
  - "sveltekit"
  - "runes"
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

# Svelte Codex Instructions: Runes, Load Functions and SSR

## Install

Install the native export at `AGENTS.md` as an appended section, not a replacement and not a custom agent.
Copy that export, not this catalog file. Catalog fields such as `tools` and `author` are for presets.dev.
Install one tool's skill for a checkout. Do not drop every tool's copy into `.agents/skills` under the same name.

<!-- native:start -->

# Svelte Codex Instructions: Runes, Load Functions and SSR

Section to append to `AGENTS.md` for Svelte. This is project guidance, not a custom agent. Use `$svelte-code-review` for a review.

## Updated for Svelte 5.57.3 and SvelteKit 3.2.0, Nov 2026

Svelte 5.57.3 and `@sveltejs/kit` 3.2.0 are the npm `latest` versions checked on 11 November 2026. Svelte 5 uses runes. SvelteKit 3 changes config and aliases compared with Kit 2. Read both majors before you edit. Do not apply a Kit 2 alias snippet to a Kit 3 app, and do not convert a Svelte 4 component to runes unless the task asks.

## Project shape

Routes live in the project's router directory. `+page`, `+layout`, `+page.server`, and `+server` mean different things. A load in `+page.server` runs on the server. A universal load runs on both. Do not import a database client into a universal load or a `.svelte` module that also runs in the browser.

Shared UI lives in `lib` the way the repo already does. A rune component uses `$props`, `$state`, and `$derived`. Do not add a Svelte 4 `export let` next to `$props` in new code.

## State

`$state` is what the component owns. `$derived` computes. `$effect` is a side effect with a cleanup, not a second derived store. Do not write `$state` from an effect that reads that same state.

A store at module scope in a server file is shared across requests. Do not put a user's data in a module-level variable. Request data stays in the load return value or in `event.locals`.

## Load, actions, and SSR

Return the data the page renders. Throw the project's `error()` or `redirect()` instead of a bare object. A form action validates with the project's schema and returns `fail()` with field errors. Do not trust a hidden user id.

The HTML from the server and the first client render match. A `Date.now()` or a random id during component init will hydrate wrong. Browser-only work goes in `onMount` or a dynamic import with `browser` from the env module.

## Security, performance, and tests

`{@html}` is sanitized or absent. Cookies and auth secrets stay in server files. A load does not over-fetch a table to render one field.

Use the project's Vitest and Playwright setup. A component test renders the rune component and updates state. An integration test posts the form action. Run the test command. Record the output.

## Mistakes to avoid

- Svelte 4 syntax in a new runes file.
- A Kit 2 alias or config key pasted into Kit 3.
- Module-scope state that leaks across requests.
- `{@html}` on user content.
- A database import in a file that runs in the browser.
