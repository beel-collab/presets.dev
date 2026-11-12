---
description: "Svelte standards for Runes, Load Functions and SSR. Use when editing this stack. Svelte 5.57.3 and SvelteKit 3.2.0, Nov 2026."
trigger: "model_decision"
---

# Svelte Windsurf Rules: Runes, Load Functions and SSR

Devin rule for Svelte. Install the `.devin/rules` file. The trigger is model decision. Do not also copy it into `.windsurf/rules`.

## Updated for Svelte 5.57.3 and SvelteKit 3.2.0, Nov 2026
Do not upgrade dependencies or the framework version unless the task asks.

Svelte 5.57.3 and `@sveltejs/kit` 3.2.0 are the npm latest versions read for this release. Svelte 5 uses runes. On SvelteKit 3, configuration is the `sveltekit()` Vite plugin in `vite.config.js`. `svelte.config.js` is not read. `$app/stores` is gone. Import `page` from `$app/state` and read `page`, not `$page`. `$lib` is not generated. Declare `#lib` and `#lib/*` in `package.json` `imports`, and include the file extension. Kit 3 wants Node 22.17 or newer, TypeScript 6, and Vite 8. A Kit 2 app keeps `svelte.config.js` and `$lib` until the task is the migration. Do not convert a Svelte 4 component to runes unless the task asks.

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
- A new `svelte.config.js`, `$app/stores` import, or `$lib` alias in a Kit 3 app.
- Module-scope state that leaks across requests.
- `{@html}` on user content.
- A database import in a file that runs in the browser.

## What changed in this major

SvelteKit 3 reads the `sveltekit()` Vite plugin, not `svelte.config.js`. Use `$app/state` and `#lib`.

## Deprecated APIs to never generate

In Kit 3, `svelte.config.js` is unsupported. Put `sveltekit()` in `vite.config.js`. `$app/stores` is removed. Import from `$app/state`. `$lib` is replaced by `#lib` with the file extension in `package.json` imports.

## Commands

Run the project's `vite` test or `npm test`.

## Example

```svelte
<script>
  import { page } from '$app/state'
  const id = $derived(page.params.id)
</script>
```

## Agent tooling

The Svelte team publishes an MCP server at https://mcp.svelte.dev/mcp, and a local server via `npx -y @sveltejs/mcp`. Setup is documented at https://svelte.dev/docs/ai/mcp. Use it when the project already has it. Do not add the server as a side effect of a review.
