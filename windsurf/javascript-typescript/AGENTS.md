---
title: "TypeScript Project"
description: "Place at project root. Always-on conventions for TypeScript projects with strict mode."
tags: ["javascript-typescript"]
author:
  name: Community
  url: 'https://github.com/beel-collab/presets.dev'
---

# TypeScript Project Conventions

## TypeScript Config
- `strict: true` always enabled
- `noUncheckedIndexedAccess: true` — array access returns `T | undefined`
- `exactOptionalPropertyTypes: true` — `undefined` is not a valid value for optional props
- `moduleResolution: "bundler"` for Vite/Next.js projects

## Type Safety Rules
- No `any` — use `unknown` and narrow with guards, or use specific union types
- No non-null assertions (`!`) — use optional chaining (`?.`) or explicit guards
- No `@ts-ignore` — `@ts-expect-error` with a comment is acceptable when truly needed
- Import types explicitly: `import type { User } from "./types"`

```ts
// ✅ Type narrowing over casting
function processId(id: unknown): string {
  if (typeof id !== "string") throw new TypeError("id must be a string");
  return id.toUpperCase();
}
```

## Naming
- `PascalCase` — types, interfaces, classes, enums, React components
- `camelCase` — variables, functions, methods, props
- `UPPER_SNAKE_CASE` — module-level constants
- `kebab-case` — filenames

## Patterns
- `interface` for object shapes that may be extended; `type` for unions/intersections
- `const` objects with `as const` over TypeScript enums
- Barrel files (`index.ts`) only at module boundaries — not inside feature folders
- Prefer `unknown` over `any` for external data (API responses, JSON.parse results)

## Common Mistakes to Avoid
- Widening types unnecessarily: `const x: string = "hello"` — let TypeScript infer
- Using `Object`, `String`, `Number` (boxed types) — use `object`, `string`, `number`
- Mutating function parameters — treat inputs as readonly
- Storing derived state — compute it from the source of truth
