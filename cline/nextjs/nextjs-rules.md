---
id: "cline-nextjs-rules"
slug: "cline/nextjs/nextjs-rules"
title: "Next.js Cline Rules: App Router, TypeScript and Server Actions"
description: "Cline rules for Next.js: App Router, TypeScript and Server Actions. Structure, data, errors, security, performance, and tests. Next.js 16.4.6, Nov 2026."
type: "rule"
tools:
  - "cline"
stack: "nextjs"
tags:
  - "nextjs"
  - "typescript"
  - "app-router"
  - "server-actions"
author:
  name: "presets.dev"
  github: "beel-collab"
license: "MIT"
origin: "original"
version: "1.0.0"
tested_with:
  - "Cline docs 2026-11-11; app not executed"
  - "node v22.23.4 fixture 2026-11-11"
created: "2026-11-11"
updated: "2026-11-11"
libs:
  - "next@16.4.6"
updated_for: "Next.js 16.4.6, Nov 2026"
---

# Next.js Cline Rules: App Router, TypeScript and Server Actions

## Install

Install the native export at `.clinerules/nextjs-rules.md` (do not also copy it to `.cline/rules/`).
Copy that export, not this catalog file. Catalog fields such as `tools` and `author` are for presets.dev.
Install one tool's skill for a checkout. Do not drop every tool's copy into `.agents/skills` under the same name.

<!-- native:start -->

# Next.js Cline Rules: App Router, TypeScript and Server Actions

Conditional Cline rule for Next.js. Install it under `.clinerules/` only. Use `nextjs-code-review` for a review.

## Updated for Next.js 16.4.6, Nov 2026

16.4.6 is the npm `latest` release checked on 11 November 2026. It is a bugfix backport and includes the security fixes from 16.4.5 (3 November 2026). The 15.5 patch for those fixes is 15.5.29. Keep a 15.x app on that patch unless the task asks for a major upgrade. This line wants Node 20.9 or newer and accepts React 19. Do not aim at a canary, and do not rewrite an app for the 16.4.6 compression or Turbopack fixes.

Read `package.json`, the lockfile, and `next.config` before editing. Match the directories and helpers the app already uses.

## Project shape

Prefer the App Router in `app/` or `src/app/`. A file is a Server Component until it starts with `"use client"`. Put `page`, `layout`, `loading`, `error`, and `not-found` where the router already expects them. Colocate a route's data helper next to that route.

Leave `pages/` alone unless the task is a migration. Do not mix App Router conventions into a Pages Router file, and do not start a second routing tree.

Route Handlers live in `route.ts`. They are HTTP endpoints. Give them a method, a status, and a bounded body. Middleware, when the project has it, stays a gate for redirects and coarse checks. It is not the place for database work.

## TypeScript

Keep the project's strict compiler settings. Type props with the helpers the project already generates, and rerun `next typegen` or `next dev` when those helpers are stale. Validate data that crosses a network or a form boundary with the parser the repo already uses. Do not add a second validation library.

`any` and a bare `as` hide a real mismatch. Narrow the value, or parse it. A client module cannot import `next/headers`, a database client, or a module marked `server-only`.

## Server and client components

Fetch and hold secrets in Server Components. Add `"use client"` for state, an effect, a browser API, or an event handler. If one button needs that, put the button in a small client child and pass serializable props in. A layout does not need `"use client"` because a single control has `onClick`.

Do not pass functions, class instances, or database rows into a client component. Pass the fields the view renders.

## Data, caching, and mutations

Start independent server reads together so they do not waterfall. Stream a slow region with `Suspense` and a `loading` file instead of blocking the whole page.

Turn on `cacheComponents` only when the config already has it or the task asks. Inside `'use cache'`, set `cacheLife` and, when the payload is tenant-specific, `cacheTag` with that tenant in the tag. Read a root param inside the cached function. The getter name matches the root segment, and the types appear after `next dev`, `next build`, or `next typegen`. Root-param getters are for Server Components, not for Client Components, Server Actions, or Route Handlers.

Do not call `cookies()`, `headers()`, or `searchParams` inside a cached function or a helper it calls. That fails with `next-request-in-use-cache`, sometimes only at `next start`. Do not pass `Buffer` or `Uint8Array` values through `'use cache'` to identify a user. Do not wrap the same public cached function in `unstable_cache`. A patched 16.4.5 does not make a shared cache key safe. Per-user inboxes stay out of `'use cache'`.

For a self-hosted `next start` app with Cache Components, set `partialPrefetching: true` unless the project has a written reason not to. Versions before 16.4.5 could poison a shared fallback shell when that flag was off.

A Server Action is a public endpoint. Check the session before any write. Take the user and the tenant from that session, not from the form. Validate the rest of the input and cap string length. After a successful write, expire that tenant's tag with `updateTag` when the user must see their own change. Use `revalidateTag(tag, 'max')` when a stale response is acceptable, or when the caller is a Route Handler. The one-argument `revalidateTag(tag)` form is the old call.

```ts
'use server'

export async function saveNote(input: { body?: unknown }) {
  const session = await requireSession()
  if (!session) return { ok: false as const, error: 'Sign in required' }
  if (typeof input.body !== 'string') return { ok: false as const, error: 'Note text is required' }
  const body = input.body.trim()
  if (body.length < 1 || body.length > 2000) {
    return { ok: false as const, error: 'Note text must be 1 to 2000 characters' }
  }
  await db.note.create({
    data: { tenantId: session.tenantId, authorId: session.userId, body },
  })
  updateTag(`tenant:${session.tenantId}:notes`)
  return { ok: true as const }
}
```

`requireSession`, `db`, and `updateTag` stand in for the app's own imports. The cached reader for those notes stays in a Server Component module and includes the same tenant id in its tag.

## Errors

Use `not-found` when the record is missing and `error.tsx` for an unexpected failure in that segment. Return a small result object from an action. Do not throw a stack, a SQL string, or another tenant's row to the client. Log the internal detail on the server.

## Security

Authorization lives in the action, the route, or the data helper. Hiding a button is not access control. On an Edge route, set session cookies with the Node `cookies().set()` path rather than `NextResponse.cookies.set()`. Leave `images.dangerouslyAllowSVG` at `false`. On a self-hosted app, build a new `Response` instead of returning a fetched one unchanged.

If `next` is 16.x below 16.4.5, or 15.5.x below 15.5.29, say so before adding cached functions. A version above 16.4.6 clears that floor and still needs its own notes read. Do not print cookies or service credentials.

## Performance

Keep client JavaScript small. Do not mark a page `"use client"` to avoid thinking about a server fetch. Avoid request waterfalls. Do not cache personalized data under a tag that every visitor shares. Serve images through the project's image component.

## Tests

Add a case for a signed-out caller, a payload that fails validation, and a read that stays inside one tenant. Use the test runner the repo already has. Paste the result you saw. Do not claim a command ran when it did not, and do not deploy from a review.

## Mistakes to avoid

- A `"use client"` file whose only job is rendering fetched data.
- An action that writes before it has a session, or that trusts a client-supplied tenant id.
- A `'use cache'` tag of `notes` on rows that belong to one tenant.
- `any` or `as` used to quiet a type error at a trust boundary.
- A major `next` upgrade, or `cacheComponents: true`, added as a side effect of another task.
