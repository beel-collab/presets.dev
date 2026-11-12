---
id: "cline-nuxt-rules"
slug: "cline/nuxt/nuxt-rules"
title: "Nuxt Cline Rules: SSR Data, Nitro and Runtime Config"
description: "Cline rules for Nuxt: SSR Data, Nitro and Runtime Config. Structure, data, errors, security, performance, and tests. Nuxt 4.6.4, Nov 2026."
type: "rule"
tools:
  - "cline"
stack: "nuxt"
tags:
  - "nuxt"
  - "vue"
  - "ssr"
author:
  name: "presets.dev"
  github: "beel-collab"
license: "MIT"
origin: "original"
version: "1.0.0"
tested_with:
  - "Cline docs 2026-11-11; app not executed"
created: "2026-11-11"
updated: "2026-11-11"
libs:
  - "nuxt@4.6.4"
updated_for: "Nuxt 4.6.4, Nov 2026"
---

# Nuxt Cline Rules: SSR Data, Nitro and Runtime Config

## Install

Install the native export at `.clinerules/nuxt-rules.md` (do not also copy it to `.cline/rules/`).
Copy that export, not this catalog file. Catalog fields such as `tools` and `author` are for presets.dev.
Install one tool's skill for a checkout. Do not drop every tool's copy into `.agents/skills` under the same name.

<!-- native:start -->

# Nuxt Cline Rules: SSR Data, Nitro and Runtime Config

Conditional Cline rule for Nuxt. Install it under `.clinerules/` only.

## Updated for Nuxt 4.6.4, Nov 2026
Do not upgrade dependencies or the framework version unless the task asks.

## Project shape

Pages and layouts live in the project's app directory. Server routes live under `server/`. A Vue component follows the script-setup style the repo uses. Do not import `server/` code into a component that renders in the browser.

`runtimeConfig` holds public and private keys. Only `runtimeConfig.public` is sent to the client. A secret in `public` is a leak. Read private config in a server route or a server plugin.

## Data fetching

Use `useAsyncData` or `useFetch` with a stable key. The key includes every input that changes the result, including the route param and the locale. An unstable key refetches forever or shows another param's payload.

Do not call bare `fetch` in `<script setup>` for data the server should already have loaded. That fetches once on the server and again on the client. `useAsyncData` dedupes when the key matches.

A server route validates its input and reads the session from the request. It does not trust a user id in the query string.

## SSR and hydration

The server HTML and the client hydration see the same data. Do not branch on `window` during setup. Use the Nuxt `import.meta.client` or `onMounted` path the project uses. A random value in setup breaks hydration.

Nitro presets and route rules stay as the config already sets them. Do not add a second cache layer that keys only on the URL when the response depends on the user.

## Errors, security, and tests

`createError` and `showError` are the project's error path. A failed fetch sets the error state. Do not render an empty page that looks successful.

Cookies and auth headers stay on the server. A plugin that runs on the client does not print `runtimeConfig` private keys.

Test a page with the project's Vitest or Playwright setup. Assert one network call for the initial data, not two. Run the test command. Record the output.

## Mistakes to avoid

- Bare `fetch` in setup for the initial payload.
- An `useAsyncData` key that omits the route param.
- A private key under `runtimeConfig.public`.
- `routeTypedFetch` enabled as an experiment nobody asked for.
- A Nuxt 3 config alias pasted into Nuxt 4 without reading the installed major.

## What changed in this major

Nuxt 4.6 keeps private `runtimeConfig` off the client. `routeTypedFetch` is experimental.

## Deprecated APIs to never generate

The Nuxt 2 `asyncData` and `fetch` component hooks were replaced. Use `useAsyncData` or `useFetch`.

## Commands

Run the Nuxt test script. Do not print `runtimeConfig`.

## Example

```ts
const id = ref(route.params.id)
const { data } = await useAsyncData(() => $fetch(`/api/notes/${id.value}`), { watch: [id] })
```
