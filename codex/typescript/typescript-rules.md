---
id: "codex-typescript-rules"
slug: "codex/typescript/typescript-rules"
title: "TypeScript Codex Instructions: Strict Types and Runtime Checks"
description: "Codex instructions for TypeScript: Strict Types and Runtime Checks. Append to AGENTS.md. Structure, security, and tests. TypeScript 7.0.2, Nov 2026."
type: "rule"
tools:
  - "codex"
stack: "typescript"
tags:
  - "typescript"
  - "strict"
  - "validation"
author:
  name: "presets.dev"
  github: "beel-collab"
license: "MIT"
origin: "original"
version: "1.0.0"
tested_with:
  - "Codex docs 2026-11-11; CLI not executed"
created: "2026-11-11"
updated: "2026-11-11"
libs:
  - "typescript@7.0.2"
updated_for: "TypeScript 7.0.2, Nov 2026"
---

# TypeScript Codex Instructions: Strict Types and Runtime Checks

## Install

Install the native export at `AGENTS.md` as an appended section, not a replacement and not a custom agent.
Copy that export, not this catalog file. Catalog fields such as `tools` and `author` are for presets.dev.
Install one tool's skill for a checkout. Do not drop every tool's copy into `.agents/skills` under the same name.

<!-- native:start -->

# TypeScript Codex Instructions: Strict Types and Runtime Checks

Section to append to `AGENTS.md` for TypeScript. This is project guidance, not a custom agent.

## Updated for TypeScript 7.0.2, Nov 2026

## Project shape

`tsconfig.json` is the source of truth. Preserve `strict` if it is on. Do not add a second config that weakens it for convenience. Path aliases, `module`, and `moduleResolution` stay as the project set them. Match the existing file layout.

A type-only import uses `import type` when the project is on `verbatimModuleSyntax` or already writes it that way. Do not import a type in a position that emits a runtime import the bundler will fail.

## Types that match the data

Model a finite set with a discriminated union and a `switch` that is exhaustive. Prefer `unknown` at a boundary and narrow it. `any` turns the checker off for everything it touches. A cast with `as` is a claim that you know more than the checker. Use it only after a runtime check, and keep the cast next to that check.

Optional fields and `null` are different. Do not paper over both with `!`. Handle the missing case.

Generics stay small. A function with three unconstrained type parameters is usually a `dict` in disguise. Name the constraint.

## Runtime checks

The checker disappears at build time. Parse JSON, form data, query strings, and environment variables with the validator the project already uses. The type of a parsed value is the validator's output, not a hand-written interface that can drift.

Do not validate by annotating a parameter. `function save(input: Note)` does not check `input` at runtime.

## Errors

Return a result or throw a typed error the caller catches. Do not `catch (e) {}`. If you catch `unknown`, narrow it before reading `message`. A public function documents the errors it raises by throwing types the project already defined.

## Performance and the compiler

Do not enable a slower project-wide flag to type one file. Fix the file. A giant union built from string concatenation is a compile-time cost. Prefer a map of known keys.

Do not port a `ts.createProgram` helper onto the `typescript` 7.0 package. That package has no stable compiler API. Keep the programmatic calls on `@typescript/typescript6` until the project adopts the 7.1 API on purpose. If the project has not upgraded, do not rewrite its lint or codegen pipeline.

## Tests

Type tests belong next to the function when the project uses `expectType` or `tsc` fixtures. A runtime test still asserts the parsed value, not only that the file typechecks. Run the project's `tsc --noEmit` or its documented check. Record the output.

## Mistakes to avoid

- `any` or `as` to silence an error at a trust boundary.
- A TypeScript interface treated as proof that JSON has that shape.
- Assuming TypeScript 7.0 exports the old compiler API, or a new one.
- A `strict` flag turned off to make a branch compile.
- A non-null assertion on a value that can be missing.

## What changed in this major

TypeScript 7.0 is the native `tsc` and ships no stable compiler API. Programmatic imports stay on `@typescript/typescript6` until 7.1.

## Deprecated APIs to never generate

Do not generate `enum` where a union is enough, or `import typescript` against the 7.0 package for the compiler API.

## Commands

Run `npx tsc --noEmit` with the project's compiler.

## Example

```ts
type Shape = { kind: "circle"; r: number } | { kind: "square"; s: number }
function area(shape: Shape): number {
  switch (shape.kind) {
    case "circle": return Math.PI * shape.r ** 2
    case "square": return shape.s ** 2
  }
}
```
