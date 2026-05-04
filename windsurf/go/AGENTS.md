---
title: "Go Project"
description: "Place at project root. Always-on conventions for Go projects following standard layout and idiomatic patterns."
tags: ["go"]
author:
  name: Community
  url: 'https://github.com/beel-collab/presets.dev'
---

# Go Project Conventions

## Project Layout
```
cmd/
  server/
    main.go         # Entry point — wire dependencies, start server
internal/           # Private application code
  handler/          # HTTP handlers
  service/          # Business logic
  repository/       # Database access
  model/            # Domain types
pkg/                # Public reusable packages
migrations/         # SQL migration files
```

## Error Handling
```go
// Always wrap errors with context
if err != nil {
    return fmt.Errorf("createUser: %w", err)
}

// Check error types with errors.Is / errors.As
if errors.Is(err, ErrNotFound) {
    http.Error(w, "not found", http.StatusNotFound)
    return
}
```
- Never ignore errors — `_ = fn()` requires a comment explaining why
- Define sentinel errors: `var ErrNotFound = errors.New("not found")`
- Use `%w` to wrap, not `%v` — preserves the error chain

## Code Style
- `gofmt` and `goimports` enforced — no exceptions
- `golangci-lint` runs in CI
- Receiver names: short, consistent abbreviation of the type (`u` for `User`, not `self`)
- Interfaces defined in the consuming package, not the implementing package
- Accept interfaces, return concrete types

## Concurrency
- Share memory by communicating — prefer channels over mutexes for coordination
- Always document goroutine ownership: who starts it, who stops it, who reads the result
- Use `context.Context` for cancellation — pass as first parameter, never store in structs
- `sync.WaitGroup` to wait for goroutines; `errgroup` when errors matter

## Testing
- Table-driven tests as the standard pattern
- `t.Parallel()` in all tests that don't share state
- Integration tests behind `//go:build integration` tag
- `httptest.NewRecorder()` for handler tests — no live server needed
