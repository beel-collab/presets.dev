---
id: "gemini-cli-vue-code-review"
slug: "gemini-cli/vue/vue-code-review/SKILL"
title: "Vue Code Review Skill for Gemini CLI"
description: "Gemini CLI skill for a Vue code review. Use when you want that code review on a Vue change. Do not use it for a different stack."
type: "skill"
tools:
  - "gemini-cli"
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
  - "Gemini CLI docs 2026-11-11; CLI not run"
created: "2026-11-11"
updated: "2026-11-11"
libs:
  - "vue@3.5.45"
updated_for: "Vue 3.5.45, Nov 2026"
---

# Vue Code Review Skill for Gemini CLI

## Install

Install the native export at `.gemini/skills/vue-code-review/SKILL.md`.
Copy that export, not this catalog file. Catalog fields such as `tools` and `author` are for presets.dev.
Install one tool's skill for a checkout. Do not drop every tool's copy into `.agents/skills` under the same name.

<!-- native:start -->

# Vue Code Review Skill for Gemini CLI

Gemini CLI skill `vue-code-review` for Vue. Activation calls `activate_skill` and waits for consent. Keep this copy under `.gemini/skills`.

## When to run

Run this review for a Vue 3 change: a component, a composable, a store binding, or "check this reactivity".

## When to leave it

Stop for a non-Vue repository, or a request to convert Vue 2 that the user did not make. Do not upgrade Vue as part of the review.

## Steps

1. Read the installed Vue major. A Vue 2 file edited with Vue 3-only syntax is a high finding unless the task is the migration.
2. Search the diff for a destructure of `reactive()` or of a store without `storeToRefs` or `toRefs`. That is a finding when the fields are used later as if they were reactive.
3. Search for `window`, `document`, and `localStorage` in setup on a component that also renders on the server. That is a high finding.
4. Check watchers for cleanup, props for mutation, and `v-html` for unsanitized input.
5. Look for a test that renders the component and updates the source of truth. Missing coverage on a new composable is a medium finding. Run the project's Vue test command only if the user asked. Otherwise write `not run`.

## Output

Findings with severity, file, line, the reactivity or SSR mistake, and a fix. Include the Vue version.

## Stop

Stop when the user asks you to rewrite the app from Options API to script setup without naming the files.
