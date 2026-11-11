<!-- Append this section to AGENTS.md. Do not replace the existing file. This is project guidance, not a custom agent. -->

# Nuxt Codex Instructions: SSR Data, Nitro and Runtime Config

Section to append to `AGENTS.md` for Nuxt. This is project guidance, not a custom agent. Use `$nuxt-performance-audit` for a review.

## Updated for Nuxt 4.6.4, Nov 2026

Nuxt 4.6.4 is the npm `latest` release checked on 11 November 2026. Current apps import server utilities from the Nuxt server paths the project already uses, and typed fetch has been rebuilt. `routeTypedFetch` is still experimental. Do not turn it on unless the task asks. Read `nuxt.config` and the installed major before you copy a Nuxt 3 snippet into a Nuxt 4 app.

## Project shape

Pages and layouts live in the project's app directory. Server routes live under `server/`. A Vue component follows the Vue 3 rune or composition style the repo uses. Do not import `server/` code into a component that renders in the browser.

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
