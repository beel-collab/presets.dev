---
id: "gemini-cli-vue-rules"
slug: "gemini-cli/vue/vue-rules"
title: "Vue Gemini CLI Rules: Script Setup, Composables and SSR"
description: "Gemini CLI rules for Vue: Script Setup, Composables and SSR. Append to GEMINI.md. Structure, security, and tests. Vue 3.5.45, Nov 2026."
type: "rule"
tools:
  - "gemini-cli"
stack: "vue"
tags:
  - "vue"
  - "typescript"
  - "composables"
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

# Vue Gemini CLI Rules: Script Setup, Composables and SSR

## Install

Install the native export at `GEMINI.md` as an appended section, then check `/memory show`.
Copy that export, not this catalog file. Catalog fields such as `tools` and `author` are for presets.dev.
Install one tool's skill for a checkout. Do not drop every tool's copy into `.agents/skills` under the same name.

<!-- native:start -->

# Vue Gemini CLI Rules: Script Setup, Composables and SSR

Section to append to `GEMINI.md` for Vue. Confirm with `/memory show`. The review skill waits for consent before it runs.

## Updated for Vue 3.5.45, Nov 2026

Vue 3.5.45 is the npm `latest` release checked on 11 November 2026. Recent 3.5 fixes touched hydration, Suspense, KeepAlive, and reactivity. Read the installed version. Do not rewrite a Vue 2 codebase in Composition API unless the task asks.

## Project shape

New components use `<script setup lang="ts">` when the project is on Vue 3 and TypeScript. Follow the existing single-file component layout. A composable is named `useSomething` and lives next to the feature that owns it.

Do not mix Options API and Composition API in a new component. An old Options component stays until you are asked to convert that file.

## Reactivity

`ref` and `reactive` are the state. A `computed` derives a value. Do not copy a prop into a `ref` unless you need a local editable copy, and then say so.

Destructuring a `reactive` object into plain variables drops the reactivity. Destructure from `props` only with `toRefs`, or read `props.field` in the template and in computeds. `storeToRefs` is the same rule for a Pinia store, when the project uses Pinia.

A watcher has a cleanup. Stop a timer, an observer, and a request when the scope disposes. `watchEffect` is for a side effect you can rerun. It is not a place to derive state you could compute.

## Props, emits, and templates

Declare props and emits with types. A prop is read-only. Emit the change and let the parent own the value. `v-for` uses a stable key, not the index, when the list can reorder.

The template stays declarative. A heavy expression moves into a computed. Do not mutate a prop or an external singleton from the template.

## SSR and errors

On a Nuxt or other SSR app, do not touch `window` during setup. Guard it, or run the browser work in `onMounted`. A random id or a clock during setup will mismatch hydration. Suspense and KeepAlive need the keys and fallbacks the project already uses. Do not invent a second cache around them.

Show an error state in the component that failed. Do not swallow a failed request and render an empty list that looks successful.

## Security, performance, and tests

`v-html` gets sanitized content or nothing. Do not bind a user string into HTML.

A large list uses the virtualization the project already has. Do not deep-watch a huge object by habit. A computed is cheaper than a watch that writes another ref.

Test a component with the project's Vue Test Utils or Testing Library setup. Assert the rendered text and the emitted event. Cover the lost-reactivity case when you change a store binding: the text updates when the store updates.

## Mistakes to avoid

- Destructuring a reactive object and expecting it to stay live.
- `window` during setup on an SSR page.
- A prop mutated in the child.
- A watcher with no cleanup.
- A Vue 2 pattern pasted into a script-setup component.
