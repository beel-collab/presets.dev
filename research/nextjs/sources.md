# Next.js sources

Fetched 12 November 2026.

- Registry: https://registry.npmjs.org/next reports `latest` 16.4.6.
- https://nextjs.org/blog/next-16 introduces Next.js 16, including the caching APIs and the move from `middleware` to `proxy`.
- https://nextjs.org/docs/app/api-reference/file-conventions/proxy documents `proxy` on the Node.js runtime. `middleware.ts` is the deprecated Edge name.
- https://nextjs.org/docs/app/api-reference/directives/use-cache documents the cache key: arguments and values read inside the function.
- https://nextjs.org/docs/app/api-reference/functions/cacheTag documents tags as invalidation, not as the cache key.
- https://nextjs.org/docs/app/api-reference/functions/updateTag and https://nextjs.org/docs/app/api-reference/functions/revalidateTag document the current tag calls. `revalidateTag` takes a tag and a cache profile.
- https://nextjs.org/blog/november-2026-security-release (3 November 2026) names the patched versions 16.4.5 and 15.5.29, including cross-tenant cache disclosure.
- https://nextjs.org/blog/next-16 also describes the Next.js Devtools MCP server and `AGENTS.md` for agents.
- `node --test fixtures/nextjs/tenant-cache/policy.test.mjs` checks the decision table. It does not boot Next.js.
