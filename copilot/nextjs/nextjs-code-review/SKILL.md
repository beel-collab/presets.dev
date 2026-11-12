---
id: "copilot-nextjs-code-review"
slug: "copilot/nextjs/nextjs-code-review/SKILL"
title: "Next.js Code Review Skill for Copilot"
description: "Review a Next.js App Router change for structure, Server Actions, data fetching, security, and tests. Use for a Next.js code review or a pre-merge check. Do not use for a CSS-only tweak, a non-Next.js repository, or a major upgrade nobody asked for."
type: "skill"
tools:
  - "copilot"
stack: "nextjs"
tags:
  - "nextjs"
  - "typescript"
  - "app-router"
  - "server-actions"
  - "code-review"
author:
  name: "presets.dev"
  github: "beel-collab"
license: "MIT"
origin: "original"
version: "1.0.0"
tested_with:
  - "Copilot docs 2026-11-11; app not executed"
  - "node v22.23.4 fixture 2026-11-11"
created: "2026-11-11"
updated: "2026-11-11"
libs:
  - "next@16.4.6"
updated_for: "Next.js 16.4.6, Nov 2026"
---

# Next.js Code Review Skill for Copilot

## Install

Install the native export at `.github/skills/nextjs-code-review/SKILL.md`.
Copy that export, not this catalog file. Catalog fields such as `tools` and `author` are for presets.dev.
Install one tool's skill for a checkout. Do not drop every tool's copy into `.agents/skills` under the same name.

<!-- native:start -->

# Next.js Code Review Skill for Copilot

Copilot skill `nextjs-code-review` for Next.js. The description decides when Copilot loads it. Keep this copy under `.github/skills`.

## When to run

Run this review for a Next.js change: a pull request, a feature, or a request to "review the app", "check this route", or "look at the server actions". Cover structure, data, auth, and tests. Caching is one part of the review, not the whole job.

## When to leave it

Stop for a CSS-only tweak, a repository that does not depend on `next`, or a request that names a different framework. Say what you found and wait. Do not upgrade `next` across a major version unless the request asked.

## Steps

1. Read the installed `next` version and the config. On 16.x, 16.4.5 is the security floor and 16.4.6 is the patch this review was written against. On 15.5, the floor is 15.5.29. A version below the floor is a high finding. A version above 16.4.6 is `above-reviewed`. An unreadable version is `unparsed`. Keep going so application bugs are still listed.
2. Map the change. Note App Router versus Pages Router, and which files are Server Components, client components, actions, and route handlers. A `"use client"` file that only displays server data is a finding. A client file that imports server-only modules is a finding.
3. Review each write. The session check happens first. The user id and tenant id come from the session. The other fields are validated, with a length cap on free text. A client-supplied role or tenant that is stored is a high finding.
4. Review data loading. Independent reads should not be forced into a waterfall. For `'use cache'`, the key (arguments and captured values) is the isolation boundary. A tenant's rows stored under a key that omits the tenant is a high finding. A shared `cacheTag` on a key that already includes the tenant is not a finding. `cookies()`, `headers()`, or `searchParams` inside that cache are a high finding. The same function also passed through `unstable_cache` is a high finding. Binary arguments used as a user id are a high finding. Cache Components that are off mean you skip this step and say so.
5. Review failures. Missing records use the not-found path. Unexpected failures are caught by a segment error boundary. Action results that the UI already understands stay small. Internal errors are not sent to the browser.
6. Review the security edges that show up in the diff: Edge cookie writes, `images.dangerouslyAllowSVG`, and a fetched `Response` returned unchanged from a self-hosted route.
7. Look at tests. A behavior change without a signed-out case, a bad payload, or a tenant-scoped read is a finding when the repo has a test runner. Run that runner only if the user asked you to change code or to execute checks. Record the command and the output. If you did not run it, write `not run`.

## Output

List findings first. Each one has a severity (`high`, `medium`, or `low`), a file, a line, a short quote, why it fails, and a fix. Then add the version, the config flags you saw, the searches you ran, and `no file edits` unless the user asked for fixes.

A clean review says "No findings" and lists the files you opened. A search you skipped is not a clean result.

```
## Findings
- high | path:line | what is wrong | what to do instead

## No findings
Say "No findings" and list the files you opened. A search you skipped is not a clean result.

## Example
Input: `app/notes/page.tsx` stores one tenant's rows in `'use cache'` and never reads that tenant id.
Output: high | app/notes/page.tsx:14 | the cache key omits the tenant | read the tenant inside the cached function so the key differs per tenant.
```

Do not flag the valid pattern named in the standards. Flag the mistake next to it.

## Stop

Stop when there is no manifest, when the checkout is not Next.js, or when the user asks for a deploy, a secret, or a production cache flush.

## Severity

`high` is a bug a caller can hit or a secret that leaks. `medium` is a broken contract that needs a specific input. `low` is a cleanup that does not change behaviour.
