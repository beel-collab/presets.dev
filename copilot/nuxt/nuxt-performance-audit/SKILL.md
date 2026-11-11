---
id: "copilot-nuxt-performance-audit"
slug: "copilot/nuxt/nuxt-performance-audit/SKILL"
title: "Nuxt Performance Audit Skill for Copilot"
description: "Copilot skill for a Nuxt performance audit. Use when you want that performance audit on a Nuxt change. Do not use it for a different stack."
type: "skill"
tools:
  - "copilot"
stack: "nuxt"
tags:
  - "nuxt"
  - "vue"
  - "ssr"
  - "performance"
author:
  name: "presets.dev"
  github: "beel-collab"
license: "MIT"
origin: "original"
version: "1.0.0"
tested_with:
  - "Copilot docs 2026-11-11; app not executed"
created: "2026-11-11"
updated: "2026-11-11"
libs:
  - "nuxt@4.6.4"
updated_for: "Nuxt 4.6.4, Nov 2026"
---

# Nuxt Performance Audit Skill for Copilot

## Install

Install the native export at `.github/skills/nuxt-performance-audit/SKILL.md`.
Copy that export, not this catalog file. Catalog fields such as `tools` and `author` are for presets.dev.
Install one tool's skill for a checkout. Do not drop every tool's copy into `.agents/skills` under the same name.

<!-- native:start -->

# Nuxt Performance Audit Skill for Copilot

Copilot skill `nuxt-performance-audit` for Nuxt. The description decides when Copilot loads it. Keep this copy under `.github/skills`.

## When to run

Run this audit when a Nuxt page is slow, double-fetches, hydrates badly, or might be leaking config.

## When to leave it

Stop for a Vue app that is not Nuxt. Do not upgrade Nuxt or enable experimental flags unless the user asked.

## Steps

1. Read the installed Nuxt major. A Nuxt 3-only config key on Nuxt 4 is a finding.
2. Search setup blocks for bare `fetch` or `$fetch` used for data that `useAsyncData` should own. A duplicate server-then-client fetch is a high finding.
3. Check `useAsyncData` keys. A key that ignores a route param is a high finding.
4. Read `runtimeConfig`. A secret outside `public` that is referenced from a client component is a high finding. `routeTypedFetch` turned on without a request is a finding.
5. Look for `window` during setup.
6. Run the project's test or a single page load only if the user asked. Otherwise write `not run`.

## Output

Findings with severity, file, line, the extra fetch or the leaked key, and a fix. Do not print secret values.

## Stop

Stop when the user asks you to log `runtimeConfig` or to disable SSR to hide a hydration bug.
