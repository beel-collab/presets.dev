---
name: "go-code-review"
description: "Review a Go change for ignored errors, goroutine leaks, and context that is not canceled. Use for a Go code review. Do not use for a non-Go repository or to enable an experimental flag by default."
---

# Go Code Review Skill for Antigravity CLI

Antigravity CLI skill `go-code-review` for Go. The workspace path is `.agents/skills/go-code-review/SKILL.md`. Reload skills before you expect the new command.

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
