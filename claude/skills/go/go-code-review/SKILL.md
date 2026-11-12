---
id: "claude-go-code-review"
slug: "claude/skills/go/go-code-review/SKILL"
title: "Go Code Review Skill for Claude Code"
description: "Review a Go change for ignored errors, goroutine leaks, and context that is not canceled. Use for a Go code review. Do not use for a non-Go repository or to enable an experimental flag by default."
type: "skill"
tools:
  - "claude"
stack: "go"
tags:
  - "go"
  - "golang"
  - "context"
  - "code-review"
author:
  name: "presets.dev"
  github: "beel-collab"
license: "MIT"
origin: "original"
version: "1.0.0"
tested_with:
  - "Claude Code docs 2026-11-11; CLI not run"
created: "2026-11-11"
updated: "2026-11-11"
libs:
  - "go@1.27.4"
updated_for: "Go 1.27.4, Nov 2026"
---

# Go Code Review Skill for Claude Code

## Install

Install the native export at `.claude/skills/go-code-review/SKILL.md`.
Copy that export, not this catalog file. Catalog fields such as `tools` and `author` are for presets.dev.
Install one tool's skill for a checkout. Do not drop every tool's copy into `.agents/skills` under the same name.

<!-- native:start -->

# Go Code Review Skill for Claude Code

Claude Code skill `go-code-review` for Go. The command is `/go-code-review`. Leave the normal permission prompts on.

## When to run

Run this review for a Go change: a handler, a worker, a package, or "check the error paths".

## When to leave it

Stop for a non-Go repository. Do not bump the `go` line in `go.mod` unless the user asked.

## Steps

1. Read the `go` version in `go.mod`. `GOEXPERIMENT=simd` without a written reason is a high finding. An import of `encoding/json/v2` on a module older than 1.27 is a high finding. On 1.27, `encoding/json` is already the v2 implementation. Do not flag that import. Flag a switch to the `encoding/json/v2` package only when the diff does not account for the stricter defaults.
2. Search the diff for `_ =` on a call that returns an error, and for `if err != nil { return nil }`. A discarded error is a high finding.
3. Search for `go func`. Each goroutine needs a cancel path and something that waits for it. A missing `ctx.Done()` in a loop is a high finding.
4. Check HTTP and SQL calls for a context and for parameters. String-built SQL is a high finding.
5. Run `go test` for the touched package if the user asked. Otherwise write `not run`.

## Output

Findings with severity, file, line, the ignored error or the leaked goroutine, and a fix. Include the Go version.

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

Stop when the user asks you to silence an error with `_` so the build is quiet.

## Severity

`high` is a bug a caller can hit or a secret that leaks. `medium` is a broken contract that needs a specific input. `low` is a cleanup that does not change behaviour.
