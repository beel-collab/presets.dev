---
id: "codex-nodejs-performance-audit"
slug: "codex/nodejs/nodejs-performance-audit/SKILL"
title: "Node.js Performance Audit Skill for Codex"
description: "Audit a Node.js service for event-loop blocking, missing cancellation, and unbounded streams or retries. Use for a Node.js performance audit. Do not use for a browser-only bug or a non-Node repository."
type: "skill"
tools:
  - "codex"
stack: "nodejs"
tags:
  - "nodejs"
  - "esm"
  - "streams"
  - "performance"
author:
  name: "presets.dev"
  github: "beel-collab"
license: "MIT"
origin: "original"
version: "1.0.0"
tested_with:
  - "Codex docs 2026-11-11; CLI not executed"
created: "2026-11-11"
updated: "2026-11-11"
libs:
  - "node@26.13.1"
updated_for: "Node.js 26.13.1 LTS, Nov 2026"
---

# Node.js Performance Audit Skill for Codex

## Install

Install the native export at `.agents/skills/nodejs-performance-audit/SKILL.md`.
Copy that export, not this catalog file. Catalog fields such as `tools` and `author` are for presets.dev.
Install one tool's skill for a checkout. Do not drop every tool's copy into `.agents/skills` under the same name.

<!-- native:start -->

# Node.js Performance Audit Skill for Codex

Codex skill `nodejs-performance-audit` for Node.js. Call it with `$nodejs-performance-audit` or `/skills`. Do not install the other tools' copies beside it.

## When to run

Run this audit when a Node.js service is slow, timing out, or leaking work after the client disconnects. Also run it for "check the event loop" or "this handler blocks".

## When to leave it

Stop for a browser-only React bug, or a repository that does not run on Node. Do not upgrade Node as part of the audit.

## Steps

1. Read `engines` and the start script. Note the LTS line. A recommendation to move to a v27 alpha is not a finding you file as work. Flag it only if the diff already targets that alpha.
2. Find the handler the user named. If they did not name one, ask. Search that path for `readFileSync`, `execSync`, large `JSON.parse`, and unbounded `Buffer.concat`.
3. Check outbound calls for a timeout and an `AbortSignal` tied to the request. A retry without a cap is a high finding on a hot path.
4. Check streams and body limits. An upload with no size cap is a high finding.
5. Look for a process-global cache keyed without the user or tenant when the value contains their data.
6. Run the project's benchmark or test only if one exists and the user asked. Otherwise write `not run`.

## Output

Findings with severity, file, line, the blocking or unbounded call, and a bounded alternative. Include the Node line you read.

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

## Stop

Stop when the user asks you to load-test production or to print environment secrets.

## Severity

`high` is a bug a caller can hit or a secret that leaks. `medium` is a broken contract that needs a specific input. `low` is a cleanup that does not change behaviour.
