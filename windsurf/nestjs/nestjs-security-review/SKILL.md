---
id: "windsurf-nestjs-security-review"
slug: "windsurf/nestjs/nestjs-security-review/SKILL"
title: "NestJS Security Review Skill for Windsurf"
description: "Windsurf skill for a NestJS security review. Use when you want that security review on a NestJS change. Do not use it for a different stack."
type: "skill"
tools:
  - "windsurf"
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
  - "Devin and Cascade docs 2026-11-11; not run"
created: "2026-11-11"
updated: "2026-11-11"
libs:
  - "@nestjs/core@12.4.2"
updated_for: "NestJS 12.4.2, Nov 2026"
---

# NestJS Security Review Skill for Windsurf

## Install

Install the native export at `.devin/skills/nestjs-security-review/SKILL.md` and `.windsurf/skills/nestjs-security-review/SKILL.md`.
Copy that export, not this catalog file. Catalog fields such as `tools` and `author` are for presets.dev.
Install one tool's skill for a checkout. Do not drop every tool's copy into `.agents/skills` under the same name.

<!-- native:start -->

# NestJS Security Review Skill for Windsurf

Skill `nestjs-security-review` for Devin CLI and the legacy Windsurf skills folder. Invoke it with `/nestjs-security-review`. This file is not a subagent.

## When to run

Run this review for a NestJS controller, module, DTO, or guard.

## When to leave it

Stop for an Express app that does not use Nest. Do not upgrade Nest unless the user asked.

## Steps

1. Read the installed `@nestjs/core` version and the Node engine. A pattern from a newer major is a finding.
2. For each new provider, confirm it is registered and exported only if another module injects it. A missing registration is a high finding.
3. For each `@Body()`, confirm a class DTO with validation decorators. An interface is a high finding.
4. For each write, confirm a guard and that the service does not persist a client-supplied role or owner from a spread DTO.
5. Confirm the global validation pipe is still enabled.
6. Run the project's test script only if the user asked. Otherwise write `not run`.

## Output

Findings with severity, file, line, the missing provider or guard, and a fix.

## Stop

Stop when the user asks you to disable the validation pipe or to leave a route unguarded for a demo.
