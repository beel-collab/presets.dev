---
id: "windsurf-vue-code-review"
slug: "windsurf/vue/vue-code-review/SKILL"
title: "Vue Code Review Skill for Windsurf"
description: "Review a Vue 3 change for lost reactivity, composable cleanup, and SSR safety. Use for a Vue code review. Do not use for a Vue 2 Options API migration nobody asked for, or a non-Vue repository."
type: "skill"
tools:
  - "windsurf"
stack: "vue"
tags:
  - "vue"
  - "typescript"
  - "composables"
  - "code-review"
author:
  name: "presets.dev"
  github: "beel-collab"
license: "MIT"
origin: "original"
version: "1.0.0"
tested_with:
  - "Devin and Cascade docs 2026-11-11; not run"
created: "2026-11-11"
updated: "2026-11-11"
libs:
  - "vue@3.5.45"
updated_for: "Vue 3.5.45, Nov 2026"
---

# Vue Code Review Skill for Windsurf

## Install

Install the native export at `.devin/skills/vue-code-review/SKILL.md`.
Copy that export, not this catalog file. Catalog fields such as `tools` and `author` are for presets.dev.
Install one skill file per name. Cursor, GitHub Copilot, Codex, Antigravity CLI, and Devin can all read `.agents/skills`, so a second copy with the same name collides.

<!-- native:start -->

# Vue Code Review Skill for Windsurf

Devin skill `vue-code-review` for Vue. Invoke it with `/vue-code-review`. Install only `.devin/skills`. This file is not a subagent.

## When to run

Run this review for a Vue 3 change: a component, a composable, a store binding, or "check this reactivity".

## When to leave it

Stop for a non-Vue repository, or a request to convert Vue 2 that the user did not make. Do not upgrade Vue as part of the review.

## Steps

1. Read the installed Vue major. A Vue 2 file edited with Vue 3-only syntax is a high finding unless the task is the migration.
2. Search the diff for a destructure of `reactive()` or of a store without `storeToRefs`. That is a finding when the fields are used later as if they were reactive. On Vue 3.5 or newer, `const { id } = defineProps<...>()` is valid and must not be flagged. On 3.4 and earlier, that props destructure is a finding unless the reactive-props transform is enabled.
3. Search for `window`, `document`, and `localStorage` in setup on a component that also renders on the server. That is a high finding.
4. Check watchers for cleanup, props for mutation, and `v-html` for unsanitized input.
5. Look for a test that renders the component and updates the source of truth. Missing coverage on a new composable is a medium finding. Run the project's Vue test command only if the user asked. Otherwise write `not run`.

## Output

Findings with severity, file, line, the reactivity or SSR mistake, and a fix. Include the Vue version.

```
## Findings
- high | path:line | what is wrong | what to do instead

## No findings
Say "No findings" and list the files you opened. A search you skipped is not a clean result.

## Example
Input: a Vue 3.5 `<script setup>` does `const { label } = defineProps<{ label: string }>()`.
Output: No findings. Vue 3.5 compiles that destructure so it stays reactive. Flag `const { count } = reactive(state)` without `toRefs`.
```

Do not flag the valid pattern named in the standards. Flag the mistake next to it.

## Stop

Stop when the user asks you to rewrite the app from Options API to script setup without naming the files.

## Severity

`high` is a bug a caller can hit or a secret that leaks. `medium` is a broken contract that needs a specific input. `low` is a cleanup that does not change behaviour.
