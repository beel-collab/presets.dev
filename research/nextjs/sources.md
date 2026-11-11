# Next.js research notes

Facts for the original Next.js presets. This file is not a catalog entry.

Checked 11 November 2026.

## Versions

The npm `latest` document for `next` was 16.4.6. Its engine field requires Node 20.9.0 or newer. Its React peer includes React 19. The GitHub release `v16.4.6` on 9 November 2026 is a bugfix backport (route-handler compression and Turbopack garbage collection among the notes). The security patch line is 16.4.5, published 3 November 2026, and 15.5.29 on the 15.5 maintenance line.

## Cache and actions

Cache Components are opt-in with `cacheComponents: true`. A `'use cache'` function should set `cacheLife` and can set `cacheTag`. `updateTag` expires a tag from a Server Action for a read-your-own-writes path. `revalidateTag` takes a tag and a cache profile such as `'max'`.

`next/root-params` exposes async getters generated from root dynamic segments. A cached function records the root params it actually reads. The getters are for Server Components, not Client Components, Server Actions, or Route Handlers.

`cookies()`, `headers()`, and `searchParams` inside a cached call stack fail with `next-request-in-use-cache`, which can show up at `next start` after a passing build.

## November 2026 advisories named in the official post

The post at `https://nextjs.org/blog/november-2026-security-release` describes:

- Cross-tenant disclosure when one public `use cache` function is also called through `unstable_cache` and reads a root param.
- Cross-root-param disclosure from nested `use cache` functions that finish the outer entry before a slow inner value records its root param.
- Binary `use cache` arguments that can share one cache identity.
- Shared fallback-shell poisoning on self-hosted `next start` when Cache Components are on and partial prefetching is off, for a specific dynamic route shape.
- Cross-client response mixups when a fetched `Response` is forwarded with stale compression framing.
- `HttpOnly` cookie exposure through `x-middleware-set-cookie` when an Edge handler uses `NextResponse.cookies.set()`.
- An SVG rejection bypass in image optimization when a remote image is misclassified.

## Demand

Observed suggestion phrases: "cursor rules nextjs", "cursor rules nextjs typescript", "copilot instructions nextjs", "codex skill nextjs", "codex next js skills". The sampled Cline and Gemini CLI prefixes for this stack did not return a relevant suggestion. Those two tool phrases stay hypotheses.

## Local check

`fixtures/nextjs/tenant-cache/policy.test.mjs` locks the version floor and the action and cache gates. It does not start Next.js.
