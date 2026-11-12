---
name: "nextjs-code-review"
description: "Review a Next.js App Router change for structure, Server Actions, data fetching, security, and tests. Use for a Next.js code review or a pre-merge check. Do not use for a CSS-only tweak, a non-Next.js repository, or a major upgrade nobody asked for."
paths:
  - "app/**/*.ts"
  - "app/**/*.tsx"
  - "src/app/**/*.ts"
  - "src/app/**/*.tsx"
  - "next.config.ts"
  - "proxy.ts"
  - "src/proxy.ts"
---

# Next.js Code Review Skill for Cursor

Cursor skill `nextjs-code-review` for Next.js. Run it with `/nextjs-code-review`, or let Agent select it when the request matches. `paths` only limits automatic surfacing.

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

## Stop

Stop when there is no manifest, when the checkout is not Next.js, or when the user asks for a deploy, a secret, or a production cache flush.

## Severity

`high` is a bug a caller can hit or a secret that leaks. `medium` is a broken contract that needs a specific input. `low` is a cleanup that does not change behaviour.

## Output

```
## Findings
- high | path:line | what is wrong | what to do instead

## No findings
Say "No findings" and list the files you opened. A search you skipped is not a clean result.

## Example
Input: a one-line change that matches a rule in the standards.
Output: either one finding with file and line, or "No findings" when the change is the valid pattern named in the standards.
```

Do not flag the valid pattern named in the standards. Flag the mistake next to it.
