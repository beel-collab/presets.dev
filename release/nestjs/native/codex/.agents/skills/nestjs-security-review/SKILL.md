---
name: "nestjs-security-review"
description: "Review a NestJS change for unregistered providers, DTO validation, and unguarded routes. Use for a NestJS security review. Do not use for a non-NestJS TypeScript API or to treat a TypeScript interface as runtime validation."
---

# NestJS Security Review Skill for Codex

Codex skill `nestjs-security-review` for NestJS. Call it with `$nestjs-security-review` or `/skills`. Do not install the other tools' copies beside it.

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
