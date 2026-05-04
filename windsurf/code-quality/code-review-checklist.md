---
trigger: model_decision
title: "Code Review Checklist"
description: "Comprehensive checklist for reviewing pull requests and code changes. Covers correctness, security, performance, and readability."
tags: ["code-quality"]
author:
  name: Community
  url: 'https://github.com/beel-collab/presets.dev'
---

# Code Review Checklist

## Correctness
- [ ] Logic matches the stated requirements exactly
- [ ] All edge cases handled: null/undefined, empty collections, boundary values, concurrent access
- [ ] Error paths are as well-tested as success paths
- [ ] No off-by-one errors in loops, slices, or pagination
- [ ] Async code properly awaited — no floating promises
- [ ] Race conditions considered for any shared state

## Security
- [ ] No secrets, API keys, or credentials in code or comments
- [ ] All user input validated and sanitized before use
- [ ] SQL queries use parameterized statements — never string interpolation
- [ ] File paths sanitized to prevent path traversal
- [ ] Auth checks happen server-side, not just client-side
- [ ] Sensitive data not logged (passwords, tokens, PII)
- [ ] Dependencies not introduced with known CVEs

## Performance
- [ ] No N+1 queries — use `include`/`select_related`/`JOIN` where needed
- [ ] Expensive operations not running in a loop
- [ ] Large datasets paginated or streamed, not loaded fully into memory
- [ ] Database queries have appropriate indexes for the WHERE/ORDER BY clauses
- [ ] Caching used appropriately — and cache invalidation is correct
- [ ] No unnecessary re-renders or recomputations on the frontend

## Readability
- [ ] Variable and function names are self-explanatory
- [ ] Functions do one thing and are under ~40 lines
- [ ] Nested conditionals flattened with early returns where possible
- [ ] Complex logic has a brief comment explaining *why*, not *what*
- [ ] Magic numbers/strings extracted to named constants
- [ ] Dead code removed — no commented-out blocks

## Architecture & Design
- [ ] Change is in the right layer (controller vs service vs repository)
- [ ] No circular dependencies introduced
- [ ] Follows existing patterns in the codebase — no surprise abstractions
- [ ] New abstractions justified — three similar cases, not one
- [ ] Public API surface is minimal — only expose what consumers need

## Testing
- [ ] New behavior has test coverage
- [ ] Tests cover failure cases, not just the happy path
- [ ] No tests deleted without justification
- [ ] Mocks don't mask real integration issues

## Operations
- [ ] New config/env vars documented and have sensible defaults
- [ ] Migrations are reversible or have a rollback plan
- [ ] Logging is meaningful — errors logged with context, not just swallowed
- [ ] Feature flags or gradual rollout considered for risky changes
