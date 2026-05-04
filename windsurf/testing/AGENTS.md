---
title: "Tests Directory"
description: "Place in your tests/ directory. Auto-applies when Cascade reads or edits any test file."
tags: ["testing"]
author:
  name: Community
  url: 'https://github.com/beel-collab/presets.dev'
---

# Test Conventions

## Structure
- `describe`/`it` blocks — not bare `test()` calls at the top level
- Group related tests: `describe("UserService", () => { describe("createUser", ...) })`
- One behavior per test — if the name has "and", split it

## Naming
Format: `it("should [behavior] when [condition]")`
```ts
it("should return 404 when user does not exist")
it("should send welcome email after successful registration")
it("should throw ValidationError when email is invalid")
```

## Arrange-Act-Assert
```ts
it("should apply discount for premium users", () => {
  // Arrange
  const user = makeUser({ tier: "premium" });
  const cart = makeCart({ total: 100 });
  // Act
  const result = applyDiscount(user, cart);
  // Assert
  expect(result.total).toBe(90);
});
```

## Test Data
- Factory functions over hardcoded objects
- `makeUser({ email: "custom@test.com" })` — override only what the test cares about
- Never share mutable state between tests

## Mocking
- Mock at the boundary: HTTP clients, DB drivers, clocks, file system
- Never mock the code under test
- `beforeEach(() => vi.clearAllMocks())` — reset between tests

## What to Test
- ✅ Business logic, edge cases, error paths
- ✅ Integration boundaries (real DB in integration tests)
- ❌ Third-party library internals
- ❌ Implementation details (private methods, internal state)
- ❌ Trivial getters with no logic
