---
id: "cursor-nestjs-security-review"
slug: "cursor/nestjs/nestjs-security-review/SKILL"
title: "NestJS Security Review Skill for Cursor"
description: "Review a NestJS change for unregistered providers, DTO validation, and unguarded routes. Use for a NestJS security review. Do not use for a non-NestJS TypeScript API or to treat a TypeScript interface as runtime validation."
type: "skill"
tools:
  - "cursor"
stack: "nestjs"
tags:
  - "nestjs"
  - "typescript"
  - "dto"
  - "security"
author:
  name: "presets.dev"
  github: "beel-collab"
license: "MIT"
origin: "original"
version: "1.0.0"
tested_with:
  - "Cursor docs 2026-11-11; app not executed"
created: "2026-11-11"
updated: "2026-11-11"
libs:
  - "@nestjs/core@12.4.2"
updated_for: "NestJS 12.4.2, Nov 2026"
---

# NestJS Security Review Skill for Cursor

## Install

Install the native export at `.cursor/skills/nestjs-security-review/SKILL.md`.
Copy that export, not this catalog file. Catalog fields such as `tools` and `author` are for presets.dev.
Install one skill file per name. Cursor, GitHub Copilot, Codex, Antigravity CLI, and Devin can all read `.agents/skills`, so a second copy with the same name collides.

<!-- native:start -->

# NestJS Security Review Skill for Cursor

Cursor skill `nestjs-security-review` for NestJS. Run it with `/nestjs-security-review`, or let Agent select it when the request matches. `paths` only limits automatic surfacing.

## When to run

Run this review for a NestJS controller, module, DTO, or guard.

## When to leave it

Stop for an Express app that does not use Nest. Do not upgrade Nest unless the user asked.

## Steps

1. Read the installed `@nestjs/core` version and the Node engine. A pattern from a newer major is a finding.
2. For each new provider, confirm it is registered and exported only if another module injects it. A missing registration is a high finding.
3. For each `@Body()`, confirm a real check. A class DTO with `ValidationPipe`, or `@Body({ schema })` with `StandardSchemaValidationPipe` registered, is valid. Do not flag the schema form. An interface, or a `schema` option with no pipe, is a high finding.
4. For each write, confirm a guard and that the service does not persist a client-supplied role or owner from a spread DTO.
5. Confirm the global validation pipe is still enabled.
6. Run the project's test script only if the user asked. Otherwise write `not run`.

## Output

Findings with severity, file, line, the missing provider or guard, and a fix.

```
## Findings
- high | path:line | what is wrong | what to do instead

## No findings
Say "No findings" and list the files you opened. A search you skipped is not a clean result.

## Example
Input: `@Post() create(@Body() body: CreateNote)` where `CreateNote` is only an interface.
Output: high | notes.controller.ts:14 | an interface is erased and does not validate | use a class with `ValidationPipe`, or `@Body({ schema })` plus `StandardSchemaValidationPipe`.
```

Do not flag the valid pattern named in the standards. Flag the mistake next to it.

## What to check

- Injection: a query built by concatenating a body field.
- XSS: a controller returns user HTML with no escape.
- CSRF: a cookie-session write with no CSRF guard.
- Secrets: a config value or service key logged from an exception filter.
- IDOR: a param id used with no guard after authentication.
- SSRF: an HTTP call to a URL taken from the body with no allow-list.

## Stop

Stop when the user asks you to disable the validation pipe or to leave a route unguarded for a demo.

## Severity

`high` is a bug a caller can hit or a secret that leaks. `medium` is a broken contract that needs a specific input. `low` is a cleanup that does not change behaviour.
