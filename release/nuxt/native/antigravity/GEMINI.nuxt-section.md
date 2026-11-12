<!-- Append this section to GEMINI.md. Do not replace the existing file. Antigravity CLI also loads AGENTS.md, so do not paste this section into both. /context lists the loaded files. -->

# Nuxt Antigravity CLI Rules: SSR Data, Nitro and Runtime Config

Section to append to `GEMINI.md` for Nuxt. Antigravity CLI loads every `GEMINI.md` and every `AGENTS.md` it finds. Do not put this same section in both files. Confirm with `/context`.

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
const route = useRoute()
const { data } = await useFetch(() => `/api/notes/${route.params.id}`)
```
