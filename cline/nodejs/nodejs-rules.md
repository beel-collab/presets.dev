---
id: "cline-nodejs-rules"
slug: "cline/nodejs/nodejs-rules"
title: "Node.js Cline Rules: ESM, Cancellation and Streams"
description: "Cline rules for Node.js: ESM, Cancellation and Streams. Structure, data, errors, security, performance, and tests. Node.js 26.13.1 LTS, Nov 2026."
type: "rule"
tools:
  - "cline"
stack: "nodejs"
tags:
  - "nodejs"
  - "esm"
  - "streams"
author:
  name: "presets.dev"
  github: "beel-collab"
license: "MIT"
origin: "original"
version: "1.0.0"
tested_with:
  - "Cline docs 2026-11-11; app not executed"
created: "2026-11-11"
updated: "2026-11-11"
libs:
  - "node@26.13.1"
updated_for: "Node.js 26.13.1 LTS, Nov 2026"
---

# Node.js Cline Rules: ESM, Cancellation and Streams

## Install

Install the native export at `.clinerules/nodejs-rules.md` (do not also copy it to `.cline/rules/`).
Copy that export, not this catalog file. Catalog fields such as `tools` and `author` are for presets.dev.
Install one tool's skill for a checkout. Do not drop every tool's copy into `.agents/skills` under the same name.

<!-- native:start -->

# Node.js Cline Rules: ESM, Cancellation and Streams

Conditional Cline rule for Node.js. Install it under `.clinerules/` only.

## Updated for Node.js 26.13.1 LTS, Nov 2026

Node.js 26.13.1 Lithium is the active LTS reported by nodejs.org on 11 November 2026. The newest dist tag that day was a v27 alpha. Do not target the alpha. Read `engines` and `.nvmrc` and stay on the line the project already runs. Do not bump Node because a newer LTS exists unless the task asks.

## Project shape

Match the module system. A project with `"type": "module"` is ESM. Do not add a `require` in an ESM file or an `import` in a CommonJS file without the interop the project already uses. File extensions in ESM imports follow the local style.

Scripts, the test command, and the start command come from `package.json`. The lockfile is committed. Do not mix npm, pnpm, and yarn in one change.

## Requests and cancellation

Every outbound call takes a timeout and an `AbortSignal`. When the request that triggered the work is aborted, abort the downstream calls. Do not retry without a cap, a delay, and a check that the signal is still active. A retry of a non-idempotent POST needs an explicit reason.

Handle `unhandledRejection` by failing the process or by catching at the boundary. An empty `catch` hides a broken request.

## Streams and the event loop

A stream has a consumer that respects backpressure. Do not `read()` an unbounded upload into a single buffer. Pipe errors are handled on both sides.

Do not run CPU-heavy work, `readFileSync` on a large file, or a tight JSON parse of a huge payload on the request path. Move it off the request or bound the size. `fs` sync methods do not belong in a server handler.

## Errors and security

Validate body size, content type, and schema before you use the payload. Return a status and a small error body. Do not put a stack trace in the response.

Secrets come from the environment. Do not log `Authorization` headers or cookies. A child process does not interpolate user input into a shell string.

## Performance

Keep dependencies that run at startup small. A connection pool has a max and an idle timeout. Cache a computed value only when it is safe to share across requests. Do not cache a response that includes a user's data under a process-global key.

## Tests

Use the runner the project already has. Cover a timeout, an aborted request, and a payload that is too large. Run the test command and record the output. Do not claim a run you did not do.

## Mistakes to avoid

- ESM and CommonJS mixed in a new file.
- A retry loop with no cancellation and no cap.
- A swallowed rejection.
- A synchronous filesystem or CPU call inside a request handler.
- Targeting the v27 alpha, or upgrading the LTS line unasked.

## What changed in this major

Stay on the 26.13 LTS line. Do not target the v27 alpha. `AbortSignal` and timeouts are the cancellation tools.

## Deprecated APIs to never generate

`url.parse` is deprecated. Use the WHATWG `URL` class. An unbounded retry is a missing cancellation, not a removed API.

## Commands

Run the package test script. Do not target the v27 alpha.

## Example

```ts
const res = await fetch(url, { signal: AbortSignal.timeout(5_000) })
```
