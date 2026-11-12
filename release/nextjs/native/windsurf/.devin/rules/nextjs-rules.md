---
description: "Next.js standards for App Router, TypeScript and Server Actions. Use when editing this stack. Next.js 16.4.6, Nov 2026."
trigger: "model_decision"
---

# Next.js Windsurf Rules: App Router, TypeScript and Server Actions

Devin rule for Next.js. Install the `.devin/rules` file. The trigger is model decision. Do not also copy it into `.windsurf/rules`.

## Updated for Next.js 16.4.6, Nov 2026
Do not upgrade dependencies or the framework version unless the task asks.

Read `package.json`, the lockfile, and `next.config` before editing. Match the directories and helpers the app already uses.

## Project shape

Prefer the App Router in `app/` or `src/app/`. A file is a Server Component until it starts with `"use client"`. Put `page`, `layout`, `loading`, `error`, and `not-found` where the router already expects them. Colocate a route's data helper next to that route.

Leave `pages/` alone unless the task is a migration. Do not mix App Router conventions into a Pages Router file, and do not start a second routing tree.

Route Handlers live in `route.ts`. They are HTTP endpoints. Give them a method, a status, and a bounded body. On Next 16, request interception is `proxy.ts` (or `src/proxy.ts`) exporting `proxy`. It runs on the Node.js runtime and cannot be switched to Edge. `middleware.ts` is the deprecated name, still available only when the project must stay on the Edge runtime. Do not create a new `middleware.ts` on a 16 app. The proxy is a gate for redirects and coarse checks. It is not the place for database work.

## TypeScript

Keep the project's strict compiler settings. Type props with the helpers the project already generates, and rerun `next typegen` or `next dev` when those helpers are stale. Validate data that crosses a network or a form boundary with the parser the repo already uses. Do not add a second validation library.

`any` and a bare `as` hide a real mismatch. Narrow the value, or parse it. A client module cannot import `next/headers`, a database client, or a module marked `server-only`.

## Server and client components

Fetch and hold secrets in Server Components. Add `"use client"` for state, an effect, a browser API, or an event handler. If one button needs that, put the button in a small client child and pass serializable props in. A layout does not need `"use client"` because a single control has `onClick`.

Do not pass functions, class instances, or database rows into a client component. Pass the fields the view renders.

## Data, caching, and mutations

Start independent server reads together so they do not waterfall. Stream a slow region with `Suspense` and a `loading` file instead of blocking the whole page.

Turn on `cacheComponents` only when the config already has it or the task asks. The cache key is what isolates entries: arguments, and values the function reads, including a root param read inside the function. A tag from `cacheTag` is how you invalidate. It does not separate tenants. A shared tag such as `notes` is safe when the key already contains the tenant. `updateTag('notes')` then refreshes every tenant that used that tag, which is broader than a per-tenant tag and is a product choice, not a leak. The leak is a key that omits the tenant while the stored value contains that tenant's rows. Read the root param inside the cached function. The getter name matches the root segment, and the types appear after `next dev`, `next build`, or `next typegen`. Root-param getters are for Server Components, not for Client Components, Server Actions, or Route Handlers.

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

`requireSession`, `db`, and `updateTag` stand in for the app's own imports. The cached reader stays in a Server Component, reads the tenant inside `'use cache'` so the key differs per tenant, and calls `cacheTag(`tenant:${tenantId}:notes`)`. That is the same string `updateTag` expires. A shared `notes` tag on the reader would not be refreshed by this action.

## Errors

Use `not-found` when the record is missing and `error.tsx` for an unexpected failure in that segment. Return a small result object from an action. Do not throw a stack, a SQL string, or another tenant's row to the client. Log the internal detail on the server.

## Security

Authorization lives in the action, the route, or the data helper. Hiding a button is not access control. On an Edge route, set session cookies with the Node `cookies().set()` path rather than `NextResponse.cookies.set()`. Leave `images.dangerouslyAllowSVG` at `false`. On a self-hosted app, build a new `Response` instead of returning a fetched one unchanged.

If `next` is 16.x below 16.4.5, or 15.5.x below 15.5.29, say so before adding cached functions. A version above 16.4.6 clears that floor and still needs its own notes read. Do not print cookies or service credentials.

## Performance

Keep client JavaScript small. Do not mark a page `"use client"` to avoid thinking about a server fetch. Avoid request waterfalls. Do not cache one user's private payload under a key another user can hit. Serve images through the project's image component.

## Tests

Add a case for a signed-out caller, a payload that fails validation, and a read that stays inside one tenant. Use the test runner the repo already has. Paste the result you saw. Do not claim a command ran when it did not, and do not deploy from a review.

## Mistakes to avoid

- A `"use client"` file whose only job is rendering fetched data.
- An action that writes before it has a session, or that trusts a client-supplied tenant id.
- A `'use cache'` key that omits the tenant while the stored rows belong to one tenant. A shared tag on a correctly keyed function is fine.
- `any` or `as` used to quiet a type error at a trust boundary.
- A major `next` upgrade, or `cacheComponents: true`, added as a side effect of another task.

## What changed in this major

Next 16 uses `proxy.ts` exporting `proxy` (Node runtime). `middleware.ts` remains only for the deprecated Edge case. `revalidateTag` takes a tag and a cache profile.

## Deprecated APIs to never generate

`middleware.ts` is the deprecated name on Next 16. Write `proxy.ts` exporting `proxy`, unless the app must stay on the Edge runtime. One-argument `revalidateTag(tag)` is the old call. Pass a cache profile. `images.domains` is deprecated. Use `images.remotePatterns`.

## Commands

Run `npx tsc --noEmit` and the repo's test script. Do not deploy.

## Example

The Server Action in the data section is the worked example: session first, validated text, then `updateTag` of the same tenant tag the reader passed to `cacheTag`.

## Agent tooling

Next.js 16 ships a Devtools MCP server and tells agents to read project instructions from `AGENTS.md`. Use them when they are installed. See https://nextjs.org/blog/next-16 .
