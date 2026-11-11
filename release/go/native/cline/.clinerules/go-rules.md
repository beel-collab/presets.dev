---
paths:
  - "**/*.go"
  - "go.mod"
---

# Go Cline Rules: Errors, Context and Goroutines

Conditional Cline rule for Go. Install it under `.clinerules/` only. Use `go-code-review` for a review.

## Updated for Go 1.27.4, Nov 2026

Go 1.27.4 was the current stable release reported by `go.dev/dl` on 11 November 2026. Go 1.26.11 was also listed as stable. Stay on the version in `go.mod`. Go 1.27 adds generic methods and `json/v2`. SIMD stays experimental. Do not flip an experimental flag on because it exists, and do not switch a module to `json/v2` unless the task asks and the module is already on 1.27.

## Project shape

`go.mod` names the module. Packages are small and named for what they provide. `internal/` is for code other modules must not import. Match the existing layout. Commands live in `cmd/` when the repo already does that.

Format with `gofmt`. Vet and the project's linters are part of the check, not optional decoration.

## Errors

Check every error. `_ = do()` is a bug unless the comment says why the error cannot matter. Wrap with `%w` when the caller should use `errors.Is` or `errors.As`. A sentinel or a typed error is the project's existing style. Do not panic for a request failure. `panic` is for a broken invariant during startup, and even then `main` should fail with an error when it can.

## Context and goroutines

The first argument of a request-scoped function is `context.Context`. Pass `ctx`. Do not store a context in a struct. When the caller cancels, the work stops: a select on `ctx.Done()`, a query that takes `ctx`, an HTTP request built with `NewRequestWithContext`.

A goroutine has an owner and an end. A `go` with no way to finish is a leak. Use `errgroup` or the project's worker helper when you start more than one. Send results on a channel that is closed by the sender. Do not copy a `WaitGroup` by value.

## HTTP, JSON, and data

Handlers set a timeout on the server and on outbound calls. Decode JSON into a struct with a size limit. Unknown fields follow the project's decoder. `json/v2` is a deliberate switch on Go 1.27, not a drop-in rename of every `encoding/json` call. Read the behavior before you change a marshal.

SQL uses parameters. A transaction commits or rolls back on every path, including the error path.

## Tests

Table tests cover the success and the error. Use `t.Helper` in a helper. A test that starts a goroutine fails the test on `ctx` cancel instead of sleeping. Run `go test` for the package you changed. Record the output.

## Mistakes to avoid

- An ignored error.
- A goroutine with no cancellation and no join.
- `context.Background()` inside a request instead of the request context.
- Experimental SIMD or `json/v2` enabled by default.
- A retry that ignores `ctx.Done()`.
