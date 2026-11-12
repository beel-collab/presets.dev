---
id: "antigravity-nestjs-security-review"
slug: "antigravity/nestjs/nestjs-security-review/SKILL"
title: "NestJS Security Review Skill for Antigravity CLI"
description: "Review a NestJS change for unregistered providers, DTO validation, and unguarded routes. Use for a NestJS security review. Do not use for a non-NestJS TypeScript API or to treat a TypeScript interface as runtime validation."
type: "skill"
tools:
  - "antigravity"
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
  - "Antigravity CLI docs 2026-11-12; CLI not run"
created: "2026-11-11"
updated: "2026-11-11"
libs:
  - "@nestjs/core@12.4.2"
updated_for: "NestJS 12.4.2, Nov 2026"
---

# NestJS Security Review Skill for Antigravity CLI

## Install

Install the native export at `.agents/skills/nestjs-security-review/SKILL.md`.
Copy that export, not this catalog file. Catalog fields such as `tools` and `author` are for presets.dev.
Install one tool's skill for a checkout. Do not drop every tool's copy into `.agents/skills` under the same name.

<!-- native:start -->

# NestJS Security Review Skill for Antigravity CLI

Antigravity CLI skill `nestjs-security-review` for NestJS. The workspace path is `.agents/skills/nestjs-security-review/SKILL.md`. Reload skills before you expect the new command.

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

## Stop

Stop when the user asks you to disable the validation pipe or to leave a route unguarded for a demo.

## Severity

`high` is a bug a caller can hit or a secret that leaks. `medium` is a broken contract that needs a specific input. `low` is a cleanup that does not change behaviour.

## Output

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

## What to check

- Injection: concatenated SQL, shell, or HTML.
- XSS: unescaped user text in HTML.
- CSRF: a browser state change with the framework check disabled.
- Secrets: a key in the repo or in a log line.
- IDOR: an id from the client with no owner or permission check.
- SSRF: a user-supplied URL fetched with no allow-list.
