---
id: "gemini-cli-go-code-review"
slug: "gemini-cli/go/go-code-review/SKILL"
title: "Go Code Review Skill for Gemini CLI"
description: "Gemini CLI skill for a Go code review. Use when you want that code review on a Go change. Do not use it for a different stack."
type: "skill"
tools:
  - "gemini-cli"
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
  - "Gemini CLI docs 2026-11-11; CLI not run"
created: "2026-11-11"
updated: "2026-11-11"
libs:
  - "go@1.27.4"
updated_for: "Go 1.27.4, Nov 2026"
---

# Go Code Review Skill for Gemini CLI

## Install

Install the native export at `.gemini/skills/go-code-review/SKILL.md`.
Copy that export, not this catalog file. Catalog fields such as `tools` and `author` are for presets.dev.
Install one tool's skill for a checkout. Do not drop every tool's copy into `.agents/skills` under the same name.

<!-- native:start -->

# Go Code Review Skill for Gemini CLI

Gemini CLI skill `go-code-review` for Go. Activation calls `activate_skill` and waits for consent. Keep this copy under `.gemini/skills`.

## When to run

Run this review for a Go change: a handler, a worker, a package, or "check the error paths".

## When to leave it

Stop for a non-Go repository. Do not bump the `go` line in `go.mod` unless the user asked.

## Steps

1. Read the `go` version in `go.mod`. A new import of `json/v2` or an experimental SIMD flag on a module that is not on 1.27, or without a written reason, is a high finding.
2. Search the diff for `_ =` on a call that returns an error, and for `if err != nil { return nil }`. A discarded error is a high finding.
3. Search for `go func`. Each goroutine needs a cancel path and something that waits for it. A missing `ctx.Done()` in a loop is a high finding.
4. Check HTTP and SQL calls for a context and for parameters. String-built SQL is a high finding.
5. Run `go test` for the touched package if the user asked. Otherwise write `not run`.

## Output

Findings with severity, file, line, the ignored error or the leaked goroutine, and a fix. Include the Go version.

## Stop

Stop when the user asks you to silence an error with `_` so the build is quiet.
