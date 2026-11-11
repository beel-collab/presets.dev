---
id: "codex-nextjs-app-router-caching"
slug: "codex/nextjs/app-router-caching"
title: "Next.js Codex Instructions for Server Actions and Caching"
description: "Codex project guidance for Next.js App Router work: validated Server Actions and tenant-safe caching on 16.4.6. Append it to AGENTS.md. It is not a custom agent."
type: "rule"
tools:
  - "codex"
stack: "nextjs"
tags:
  - "nextjs"
  - "typescript"
  - "server-actions"
  - "caching"
  - "app-router"
author:
  name: "presets.dev"
  github: "beel-collab"
license: "MIT"
origin: "original"
version: "1.0.0"
tested_with:
  - "Codex docs 2026-11-11; CLI not executed"
  - "node v22.23.4 fixture 2026-11-11"
created: "2026-11-11"
updated: "2026-11-11"
libs:
  - "next@16.4.6"
updated_for: "Next.js 16.4.6, security fixes since 16.4.5 (2026-11-11)"
---

# Next.js Codex Instructions for Server Actions and Caching

Project guidance for Codex on a Next.js App Router. Codex reads `AGENTS.md`. That file is concatenated instructions, not a custom agent profile, so this catalog entry is `type: rule`.

## Install

Append the native section to the repository `AGENTS.md`. Do not replace a file that already has other guidance. Codex reads `AGENTS.override.md` first in each directory and then ignores `AGENTS.md` there, so an override silences this section. Use an override only when you mean to replace the whole directory's instructions.

Discovery walks from the Git root down to the working directory and stops at `project_doc_max_bytes`, 32 KiB by default. A long `AGENTS.md` can drop this section. Keep the section near the end of the root file, or place a copy in the app directory if that is where Codex is launched. Restart Codex after an edit. The instruction chain is built at the start of a run.

Personal prompts in `~/.codex/prompts/` are deprecated. Do not put this guidance there.

The audit procedure is a skill at `.agents/skills/nextjs-tenant-cache-audit/SKILL.md`, invoked with `$nextjs-tenant-cache-audit` or `/skills`. Install that skill only for Codex. Cursor and Gemini CLI also discover `.agents/skills`, and a second copy with the same folder name is ambiguous.

## What was checked

Codex's `AGENTS.md` discovery document and skills document were read on 11 November 2026. Codex was not started. The decision table was run with the Node fixture named in the section text. Observed suggestion phrases for this stack include "codex skill nextjs" and "codex next js skills". Those phrases belong to the skill entry.

## Sources checked on 11 November 2026

- npm `latest` for `next` resolved to 16.4.6. The registry record lists Node `>=20.9.0` and a React 19 peer.
- GitHub release `v16.4.6` (9 November 2026) is a bugfix backport and does not add the Cache Components model by itself.
- GitHub release `v16.4.5` (3 November 2026) lists the security fixes.
- The Next.js post "November 2026 Security Release" names the patched versions 16.4.5 and 15.5.29 and describes the tenant, binary-argument, shell, response-framing, Edge cookie, and SVG issues. Advisory ids cited in the preset body were taken from that post and the matching GitHub advisories.
- Next.js docs for `use cache`, `next/root-params`, `cacheTag`, and revalidation, fetched the same day: explicit `cacheLife`, tags, `updateTag` inside Server Actions, `revalidateTag` with a cache profile, and the ban on `cookies()`, `headers()`, and `searchParams` inside a cached call stack.
- The decision table was executed with `node --test fixtures/nextjs/tenant-cache/policy.test.mjs` in this repository. Cursor, Copilot, Claude Code, Windsurf, Devin, Cline, Codex, and Gemini CLI were not launched.

<!-- native:start -->

# Next.js guidance for Server Actions and caching

Section for the repository `AGENTS.md`. Codex concatenates instruction files up to the configured byte cap and treats them as guidance, not as an isolated agent. Append this section. Do not replace other guidance already in the file. The audit procedure is the `$nextjs-tenant-cache-audit` skill. Written for Next.js 16.4.6.

## Version line

These rules were checked against Next.js 16.4.6, the `latest` npm release on 11 November 2026. It was published on 9 November 2026 as a bugfix backport and includes the 16.4.5 security fixes from 3 November 2026. The 15.5 patch named beside it is 15.5.29. This line requires Node 20.9.0 or newer, and React 19 satisfies the 16.4.6 peer range.

Keep a 15.x app on that patched 15.5 line unless the task asks for a major upgrade. Do not aim at a canary. Do not change application code for the 16.4.6 compression or Turbopack fixes.

If the installed `next` version is 16.x and below 16.4.5, or 15.5.x and below 15.5.29, say that the November 2026 advisories still apply before adding a cached function. 16.4.5 and 16.4.6 are the 16.x builds this text was checked against. 15.5.29 is the 15.5 build named in the same security release. A higher version clears that numeric floor and still needs a fresh read of its own notes before you treat new APIs as safe. Another 15 minor is not covered by the 15.5.29 line. Next.js 14 and earlier do not use this Cache Components model. Do not paste `'use cache'` into those apps as part of an unrelated edit.

## Where this applies

Use these rules for App Router routes, layouts, Server Actions, Route Handlers, `next.config.ts` (or the `.js` / `.mjs` form), and helpers that call `'use cache'`, `cacheTag`, `cacheLife`, `updateTag`, `revalidateTag`, or `unstable_cache`.

Pages Router files under `pages/` stay as they are unless the task asks for a migration. Leave `cacheComponents` off when the config does not already set it and the task did not ask to turn it on.

## Read the project first

Read the installed `next` version from `package.json` and the lockfile. Read the Next config for `cacheComponents` and `partialPrefetching`. Find the session helper and the input validator the app already uses, and call those. Do not add a second validation library.

Record the version you found in the change summary.

## Server and client files

A file is a Server Component until it starts with `"use client"`. Data loading, database access, and anything that can see a secret stay in Server Components.

Add `"use client"` for state, an effect, a browser-only API, or an event handler. When one control needs that, put the control in a small client child and pass serializable props in. A layout or page does not need `"use client"` because a single button has `onClick`.

A client file does not import `next/headers`, `next/root-params`, or a database client.

## Server Actions

A function in a file marked `"use server"`, or a function marked `"use server"` itself, is a public endpoint. Anyone who can reach the deployment can call it. Hiding the button is not access control.

An action that writes follows this order:

1. Resolve the session on the server. With no session, return an error and write nothing.
2. Take the tenant id and the user id from that session. Drop a tenant id, user id, or role supplied by the client.
3. Validate the rest of the input with the project's parser. Reject unexpected fields. Cap the length of strings.
4. Write with the session tenant id in the query.
5. After the write commits, expire that tenant's cache tag with `updateTag`.

Return the small result the client already handles. Do not return the session, the raw database row, or fields that belong to another tenant.

`updateTag` is for Server Actions. It expires the tag so the next render waits for fresh data. Use it when the person who submitted the form must see their write. `revalidateTag` takes the tag and a cache profile such as `'max'`, and it may serve stale content while a refresh runs. Call that form from a Route Handler, or from an action when a short delay is acceptable. The one-argument `revalidateTag(tag)` call is the old shape. Do not use it on 16.4.

## Cache Components

Follow this section when `cacheComponents` is already true, or when the task itself turns it on.

A cached function starts with the `'use cache'` directive. Inside the function, call `cacheLife` with a named profile so the lifetime is visible at the call. When the rows belong to one tenant, call `cacheTag` with a tag that contains that tenant id.

The root-param getter is generated from the root dynamic segment. A folder named `[tenant]` is imported as `tenant` from `next/root-params`. The type for that export appears after `next dev`, `next build`, or `next typegen`. If the import does not typecheck, the segment is not a root param yet. Stop and read the app directory instead of inventing a getter. These getters are for Server Components. They are not for Client Components, Server Actions, or Route Handlers.

Only a root param the cached function actually reads becomes part of its cache key. Read it inside the cached function. Put the same id in the tag.

```ts
import { cacheLife, cacheTag } from 'next/cache'
import { tenant } from 'next/root-params'

export async function listPublicNotes() {
  'use cache'
  cacheLife('hours')
  const tenantId = await tenant()
  cacheTag(`tenant:${tenantId}:notes`)
  return db.note.findMany({
    where: { tenantId, visibility: 'public' },
    select: { id: true, body: true },
  })
}
```

`db` in that sample stands for the app's existing data access. The sample stores public, tenant-scoped fields only.

Public copy that is the same for every tenant can use a shared tag. A row that includes one tenant's content cannot. Per-user inboxes, session payloads, and account lists stay out of `'use cache'`.

A cached function, and any helper it calls, must not read `cookies()`, `headers()`, or `searchParams`. The runtime error is `next-request-in-use-cache`. On a dynamic route the build can pass and `next start` can throw. Read a cookie in the uncached parent. Pass a plain value down only when the cached result is still safe to share across callers. A session cookie is not such a value.

Do not pass `Buffer` or `Uint8Array` values into a cached function to tell users or accounts apart. Distinct binary arguments have collapsed to one cache identity. That bug is GHSA-rhh4-g77r-r9qj, patched in 16.4.5. Identify a user with a string from the server session, and keep that per-user result out of the shared cache.

Do not wrap a public `'use cache'` function in `unstable_cache`, and do not call one function both ways. During a cold fill, a call through `unstable_cache` can store one root param's result for a different caller. That bug is GHSA-mfr8-8qww-v76h, patched in 16.4.5. The patch is not a reason to mix the two APIs.

A nested `'use cache'` function that reads a root param should return plain awaited data. An object that mixes a finished value with a promise still in flight can let the outer entry be stored before the root-param dependency is recorded. That bug is GHSA-vc7v-qv4w-wrv8, patched in 16.4.5.

`use cache: private` is the rare escape hatch for request data that cannot be passed in as an argument. It is not the default for a tenant list. `use cache: remote` delegates to a platform cache handler and adds latency and cost. Switch to either directive only when the task asks for that handler.

A tenant-blind key is still wrong on serverless hosting. Prerendered output is reused, and a self-hosted Node process keeps the in-memory entry.

For a self-hosted `next start` server with `cacheComponents: true`, set `partialPrefetching: true` unless the project has a written reason to leave it off. The unset and `false` values were part of the shared fallback-shell poisoning bug on 16.4.0 through 16.4.4, GHSA-vvgp-ww4w-46vf. Version 16.4.5 contains the patch. Keep the flag explicit.

## Other fixes from the November 2026 release

On an Edge route handler, set session cookies through the Node.js `cookies().set()` path rather than `NextResponse.cookies.set()`. The Edge path could echo the cookie in `x-middleware-set-cookie`, which same-origin script can read even when the cookie is `HttpOnly`. That bug is GHSA-f3mh-rxg3-f5g2, patched in 16.4.5.

Leave `images.dangerouslyAllowSVG` at `false`. A remote image from an allowed host could be misread and reach the SVG decoder. That bug is GHSA-7qx7-33qx-rqx2, patched in 16.4.5. Turning SVG optimization on is not the fix.

On a self-hosted app, do not return a fetched `Response` unchanged when the client can influence that response. A decompressed body paired with the original compressed framing can be assigned to the wrong client behind some HTTP/1.1 proxies. That bug is GHSA-pc58-hwjq-p385, patched in 16.4.5. Build a new response with the fields you intend to send.

## Worked example

This desk-notes pair was written for this preset. `node --test fixtures/nextjs/tenant-cache/policy.test.mjs` checks the decision rules in the presets.dev repository. It does not boot Next.js or the app you are editing.

Replace an action that accepts `tenantId` from the client and a `'use cache'` reader tagged only `notes`. The action below takes the author from the session and checks the text itself:

```ts
'use server'

import { updateTag } from 'next/cache'

const limit = 2000

export async function saveNote(input: { body?: unknown }) {
  const session = await requireSession()
  if (!session) return { ok: false as const, error: 'Sign in required' }
  if (typeof input.body !== 'string') {
    return { ok: false as const, error: 'Note text is required' }
  }
  const body = input.body.trim()
  if (body.length < 1 || body.length > limit) {
    return { ok: false as const, error: 'Note text must be 1 to 2000 characters' }
  }
  await db.note.create({
    data: {
      tenantId: session.tenantId,
      authorId: session.userId,
      body,
      visibility: 'public',
    },
  })
  updateTag(`tenant:${session.tenantId}:notes`)
  return { ok: true as const }
}
```

`requireSession` and `db` are the app's own helpers. Pair the action with the `listPublicNotes` reader above. That reader stays in a Server Component module, because a root-param getter does not belong inside the action.

## Checks

From the presets.dev checkout:

```bash
node --test fixtures/nextjs/tenant-cache/policy.test.mjs
```

The suite rejects `16.4.4` and `15.5.28`, accepts `16.4.5`, `16.4.6`, and `15.5.29`, and flags a missing session, a client-supplied tenant id, a shared notes tag, a cookie read inside the cache, and a binary cache argument.

In an application repo, run the scripts that repo already has, such as `npm test` or `npx tsc --noEmit`, and paste the result you saw. Do not claim a command ran when it did not. Do not deploy.

## Boundaries

Do not raise `next` across a major version unless the task asks. Do not point `next start` at a production database. Do not print cookies or service credentials. Do not flush a hosted cache store. Do not flip `cacheComponents` on as a side effect of another change.

## Failures to catch

A `"use client"` file whose only job is rendering fetched data belongs under a Server Component parent, with serializable props passed down.

An action that inserts a row before it has a session needs the session check first, plus a case where a signed-out caller gets an error and the row count stays the same.

A `'use cache'` reader tagged only `notes`, while the rows contain tenant content, needs the tenant id in the key and in the tag. A patched Next.js version does not repair an application key that still omits the tenant.
