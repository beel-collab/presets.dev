# Svelte sources

Fetched 12 November 2026.

- Registry: https://registry.npmjs.org/svelte reports `latest` 5.57.3. https://registry.npmjs.org/@sveltejs/kit reports `latest` 3.2.0.
- https://svelte.dev/docs/kit/migrating-to-sveltekit-3 says Kit 3 does not use `svelte.config.js` (config is the `sveltekit()` Vite plugin), removes `$app/stores` in favour of `$app/state`, and replaces `$lib` with `#lib` via `package.json` imports that include the file extension.
- https://svelte.dev/docs/ai/mcp documents the official Svelte MCP server. The remote endpoint is https://mcp.svelte.dev/mcp. The local package is `@sveltejs/mcp`.
