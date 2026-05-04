---
trigger: always_on
title: "TypeScript Strict Mode"
description: "Always-on TypeScript conventions for strict, type-safe codebases."
tags: ["javascript-typescript"]
author:
  name: Community
  url: 'https://github.com/beel-collab/presets.dev'
---

# TypeScript Strict Mode

## tsconfig Requirements
- `strict: true` must be enabled — this enables `strictNullChecks`, `noImplicitAny`, `strictFunctionTypes`, and more
- Also enable `noUncheckedIndexedAccess`, `exactOptionalPropertyTypes`, `noImplicitReturns`
- Use `"moduleResolution": "bundler"` for modern tooling (Vite, Next.js, Bun)

## Type Safety Rules

**Never use `any` — always prefer:**
- `unknown` for values of unknown type (then narrow with typeof / instanceof)
- `never` for exhaustive checks
- Specific union types for constrained values

```ts
// ❌ Bad
function process(data: any) { return data.value; }

// ✅ Good
function process(data: unknown) {
  if (typeof data === "object" && data !== null && "value" in data) {
    return (data as { value: string }).value;
  }
}
```

**Avoid non-null assertions (`!`) — use guards instead:**
```ts
// ❌ Bad
const el = document.getElementById("app")!;

// ✅ Good
const el = document.getElementById("app");
if (!el) throw new Error("Missing #app element");
```

**Use `satisfies` for type checking without widening:**
```ts
const config = {
  port: 3000,
  host: "localhost",
} satisfies Config;
```

## Naming & Structure
- `PascalCase` for types, interfaces, enums, classes
- `camelCase` for variables, functions, methods
- `UPPER_SNAKE_CASE` for constants
- Prefix interfaces with nothing — not `IUser`, just `User`
- Use `type` for unions/intersections; `interface` for object shapes that may be extended

## Functions
- All parameters and return types must be explicitly typed
- Prefer function declarations over `const fn = () =>` for top-level functions
- Use overloads for functions with meaningfully different signatures

## Imports
- Use type-only imports for types: `import type { User } from "./types"`
- Barrel files (`index.ts`) only at module boundaries — not inside feature folders
- Absolute imports via path aliases (`@/`) over deep relative paths

## Enums
- Prefer `const` objects + `as const` over TypeScript enums:
```ts
// ✅ Preferred
const Status = { Active: "active", Inactive: "inactive" } as const;
type Status = typeof Status[keyof typeof Status];
```
