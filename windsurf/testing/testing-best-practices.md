---
trigger: glob
globs: "**/*.test.ts,**/*.spec.ts,**/*.test.tsx,**/*.spec.tsx"
title: "Testing Best Practices"
description: "Auto-applied when editing test files. Enforces consistent structure, naming, and patterns across unit and integration tests."
tags: ["testing"]
author:
  name: Community
  url: 'https://github.com/beel-collab/presets.dev'
---

# Testing Best Practices

## Structure
- Use `describe`/`it` blocks — not bare `test()` at the top level
- One logical assertion per test — multiple `expect` calls are fine if they test the same thing
- Group related tests under a `describe` block named after the unit under test

```ts
describe("UserService", () => {
  describe("createUser", () => {
    it("should return the created user with an id", async () => { ... });
    it("should throw if email already exists", async () => { ... });
  });
});
```

## Naming
- Format: `it("should [expected behavior] when [condition]")`
- Be specific — `"should return 404 when user not found"` not `"handles error"`
- Describe behavior, not implementation: `"should send a welcome email"` not `"should call sendEmail"`

## Arrange-Act-Assert
Always structure test bodies in three sections:
```ts
it("should apply 10% discount for premium users", () => {
  // Arrange
  const user = { tier: "premium" };
  const cart = { total: 100 };

  // Act
  const result = applyDiscount(user, cart);

  // Assert
  expect(result.total).toBe(90);
});
```

## Mocking
- Mock at the boundary — external APIs, databases, file system, clocks
- Never mock the code under test itself
- Reset mocks between tests: `beforeEach(() => { vi.clearAllMocks(); })`
- Prefer `vi.spyOn` over replacing implementations wholesale

```ts
// ✅ Mock the boundary, not the logic
vi.spyOn(emailService, "send").mockResolvedValue(undefined);
```

## Test Data
- Use factory functions over hardcoded objects — easy to override specific fields:
```ts
function makeUser(overrides: Partial<User> = {}): User {
  return { id: "1", email: "test@example.com", role: "user", ...overrides };
}
```
- Never share mutable state between tests

## Coverage
- Test the unhappy path as much as the happy path: null inputs, empty arrays, network errors
- Boundary conditions: 0, 1, max value, empty string
- Don't aim for 100% line coverage — aim for coverage of all meaningful behaviors

## Async Tests
```ts
// Always await or return promises
it("should resolve with user data", async () => {
  const user = await getUser("123");
  expect(user.id).toBe("123");
});

// Test rejections explicitly
it("should reject when id is invalid", async () => {
  await expect(getUser("")).rejects.toThrow("Invalid id");
});
```

## What NOT to Test
- Implementation details (private methods, internal state)
- Third-party library internals
- Trivial getters/setters with no logic
