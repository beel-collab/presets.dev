---
name: "nextjs-tenant-cache-audit"
description: "Audit Next.js App Router Server Actions and Cache Components for tenant leaks and missing authentication. Use for a nextjs cache audit, a tenant isolation review, a Server Action review, or the November 2026 Next.js cache advisories. Do not use for CSS, new marketing pages, Playwright tests, or repositories that are not Next.js."
---

# Next.js tenant-cache audit

Gemini CLI skill `nextjs-tenant-cache-audit`. Selecting it calls `activate_skill` and must wait for the consent prompt. A refusal ends the skill. Do not continue the audit from memory of this file after consent was declined.

## When to run

Run this audit when the request is about Next.js Server Actions, `'use cache'`, cache tags, tenant isolation, or the November 2026 Next.js cache advisories. Phrases that count: "audit the server actions", "check tenant cache keys", "review use cache", "are cached notes leaking across tenants".

## When to stop without a report

Do not run the audit for a CSS change, a new static page with no server data, a Playwright authoring task, a React-only upgrade, or a repository that is not Next.js. Say which of those you noticed and wait.

## What you may change

Read the repository. Do not edit it unless the request also asks for a fix. Do not install packages, deploy, print secrets, or flush a remote cache.

## Steps

1. Confirm `next` is a direct dependency. If it is not, stop with "not a Next.js app" and name the manifest you read.
2. Read the installed version from the manifest and the lockfile. Apply the floor below. A 16.x version below 16.4.5, or a 15.5 version below 15.5.29, is a high finding named `below-security-floor`. Continue the audit so application-level key bugs are still listed. Do not bump the dependency unless the request asked for an upgrade. A version above 16.4.6, or a 15.5 version above 15.5.29, is `above-reviewed`: the known floor is met, and this skill was not re-checked against that build. A different 15 minor or a 14.x app is `version-not-covered`. An unreadable version is `unparsed`. Do not describe those three results as patched.
3. Read `next.config.ts`, `next.config.mjs`, or `next.config.js`. Record `cacheComponents` and `partialPrefetching`. If Cache Components are off, skip the `'use cache'` checks and say so. Still review Server Actions.
4. Search for `"use server"`, `'use cache'`, `unstable_cache`, `cacheTag`, `updateTag`, `revalidateTag`, `cookies(`, `headers(`, `NextResponse.cookies.set`, and `dangerouslyAllowSVG`.
5. Review every Server Action that writes. The session check has to happen before the write. The tenant id and the user id have to come from the session. The remaining input has to be checked, with a length cap on free text. A client field named `tenantId`, `userId`, or `role` that is stored is a high finding.
6. Review every `'use cache'` function when Cache Components are on. Tenant-scoped rows need a tag and a key that include the tenant id. A root param used for that split is read inside the cached function, from `next/root-params`, and the getter name matches the root segment. `cookies()`, `headers()`, and `searchParams` inside the cached call stack are a high finding. `Buffer` or `Uint8Array` arguments used to identify a person are a high finding. The same function also passed through `unstable_cache` is a high finding. A nested cached function that returns a pending promise beside a finished value, while reading a root param, is a high finding. A per-user payload stored under `'use cache'` is a high finding.
7. Look for `revalidateTag` called with one argument. On 16.4 the call takes a tag and a profile such as `'max'`. `updateTag` belongs in a Server Action, after the write, and the tag should name the tenant when the data does.
8. Ask, or infer from the config and README, whether production is `next start` on a host the project runs itself. Report `shared-fallback-shell` only when `cacheComponents` is true, `partialPrefetching` is not true, and the app is self-hosted. If the host is unknown, say unknown. Do not upgrade that to a confirmed hit.
9. If an Edge handler sets a sensitive cookie with `NextResponse.cookies.set()`, report `edge-cookie-header`. If `images.dangerouslyAllowSVG` is true, report `svg-optimization-enabled`. If a route returns a fetched `Response` object unchanged, report `forwarded-response`.
10. Run the adverse check. A tag of `notes` on rows that contain a tenant id is a finding even when the query's `where` clause looks right. A marketing page cached with no tenant data and no user data is not a finding.
11. Run the non-trigger check. If the user asked for a color change or a new empty page, you should have stopped at the top of this skill. If you produced cache findings for that request, discard them.

## Output

Return findings first. Each finding has a severity of high, medium, or low, a file path, a line number, a short evidence quote, the failure, and a proposed fix. Then add a coverage block: the `next` version, the config flags, the search terms, the files you opened, and the commands you ran. If you ran no command, write `not run`. End with `no file edits` unless the user asked for fixes, in which case list the edits.

When nothing matched, say "No findings" and list the searches you actually performed. A skipped search is not a clean result.

## Floor used by the decision table

| Installed line | Result |
| --- | --- |
| 16.4.5 or 16.4.6 | `patched` |
| 16.x below 16.4.5 | `below-security-floor` |
| 16.x above 16.4.6 | `above-reviewed` |
| 15.5.29 | `patched` |
| 15.5 below 15.5.29 | `below-security-floor` |
| 15.5 above 15.5.29 | `above-reviewed` |
| Any other or unreadable version | `version-not-covered` or `unparsed` |

The fixture at `fixtures/nextjs/tenant-cache/policy.test.mjs` encodes this table and the action and cache gates. Running it checks the preset. It says nothing about the repository under review. Do not cite a passing fixture as evidence that the user's app is safe.

## Stop conditions

Stop when there is no manifest, when the user asks for a deploy, a secret, or a production cache flush, or when the checkout is not Next.js. Name the missing fact and wait.
