---
id: "antigravity-vue-rules"
slug: "antigravity/vue/vue-rules"
title: "Vue Antigravity CLI Rules: Script Setup, Composables and SSR"
description: "Antigravity CLI rules for Vue: Script Setup, Composables and SSR. Append to GEMINI.md. Structure, security, and tests. Vue 3.5.45, Nov 2026."
type: "rule"
tools:
  - "antigravity"
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
  - "Antigravity CLI docs 2026-11-12; CLI not run"
created: "2026-11-11"
updated: "2026-11-11"
libs:
  - "vue@3.5.45"
updated_for: "Vue 3.5.45, Nov 2026"
---

# Vue Antigravity CLI Rules: Script Setup, Composables and SSR

## Install

Install the native export at `GEMINI.md` or `AGENTS.md` as an appended section.
Copy that export, not this catalog file. Catalog fields such as `tools` and `author` are for presets.dev.
Install one tool's skill for a checkout. Do not drop every tool's copy into `.agents/skills` under the same name.

<!-- native:start -->

# Vue Antigravity CLI Rules: Script Setup, Composables and SSR

Section to append to `GEMINI.md` for Vue. Antigravity CLI also reads `AGENTS.md`. Confirm the loaded rules before you rely on them.

## Updated for Vue 3.5.45, Nov 2026

## Project shape

New components use `<script setup lang="ts">` when the project is on Vue 3 and TypeScript. Follow the existing single-file component layout. A composable is named `useSomething` and lives next to the feature that owns it.

Do not mix Options API and Composition API in a new component. An old Options component stays until you are asked to convert that file.

## Reactivity

`ref` and `reactive` are the state. A `computed` derives a value. Do not copy a prop into a `ref` unless you need a local editable copy, and then say so.

Since Vue 3.5, destructuring `defineProps()` in `<script setup>` stays reactive. The compiler rewrites those bindings. Do not flag that. Destructuring a `reactive()` object, or a Pinia store without `storeToRefs`, still copies plain values and drops reactivity. On 3.4 and earlier, `defineProps()` destructure is also a plain copy unless the project turned the transform on.

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

## What changed in this major

Vue 3.5 compiles destructured `defineProps()` so the bindings stay reactive.

## Deprecated APIs to never generate

Do not generate `Vue.filter`, or a Vue 2 `new Vue()` app.

## Commands

Run the Vue unit test script.

## Example

```vue
<script setup lang="ts">
const { label = "Save" } = defineProps<{ label?: string }>()
</script>
```
On Vue 3.5 that binding stays reactive.
