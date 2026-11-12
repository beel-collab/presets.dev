---
id: "antigravity-nestjs-rules"
slug: "antigravity/nestjs/nestjs-rules"
title: "NestJS Antigravity CLI Rules: Modules, DTOs and Guards"
description: "Antigravity CLI rules for NestJS: Modules, DTOs and Guards. Append to GEMINI.md. Structure, security, and tests. NestJS 12.4.2, Nov 2026."
type: "rule"
tools:
  - "antigravity"
stack: "nestjs"
tags:
  - "nestjs"
  - "typescript"
  - "dto"
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

# NestJS Antigravity CLI Rules: Modules, DTOs and Guards

## Install

Install the native export at `GEMINI.md` or `AGENTS.md` as an appended section.
Copy that export, not this catalog file. Catalog fields such as `tools` and `author` are for presets.dev.
Install one skill file per name. Cursor, GitHub Copilot, Codex, Antigravity CLI, and Devin can all read `.agents/skills`, so a second copy with the same name collides.

<!-- native:start -->

# NestJS Antigravity CLI Rules: Modules, DTOs and Guards

Section to append to `GEMINI.md` for NestJS. Antigravity CLI loads every `GEMINI.md` and every `AGENTS.md` it finds. Do not put this same section in both files. Confirm with `/context`.

## Updated for NestJS 12.4.2, Nov 2026
Do not upgrade dependencies or the framework version unless the task asks.

## Project shape

A feature is a module that declares its controllers and providers and exports only what other modules may use. Do not reach into another module's private provider. A new provider is listed in `providers`. A global module is rare and already a project decision.

Controllers take DTOs. Services own the use case and the transaction. Repositories talk to the database. Do not query from the controller.

## DTOs and validation

Nest 12 validates in two supported ways. A class DTO with `class-validator` decorators needs `ValidationPipe`. A Standard Schema (Zod, Valibot, ArkType) passed as `@Body({ schema })` needs `StandardSchemaValidationPipe`. The decorator only stores the schema. Without that pipe, nothing is checked. A TypeScript `interface` disappears at runtime and does not validate. Do not flag `@Body({ schema })` when the pipe is registered. Do not use an interface as the `@Body()` type and call it safe.

The validation pipe rejects unknown fields when the project has `whitelist` and `forbidNonWhitelisted`. Keep that on. A write copies the DTO fields the entity is allowed to store. Do not spread the DTO into a save if the DTO contains a role or an owner id the client must not set.

## Guards and errors

A route that changes data has a guard. Class-level `@UseGuards` is easy to forget on a new method. Public routes are marked with the project's public decorator and are rare. Check the owner inside the service even after the guard, when the guard only checks that someone is signed in.

Throw the project's HTTP exception. A filter formats the body. Do not catch and return the ORM error to the client.

## Tests

A unit test builds the service with mocks for its collaborators. An e2e test boots the module the project already boots and calls the route without a token. Cover 401, a bad DTO, and a successful owner. Run the test script. Record the output.

## Mistakes to avoid

- A provider constructed with `new` instead of injection, or missing from the module.
- A TypeScript type treated as validation.
- A DTO spread into a database write.
- A new route with no guard.
- A global pipe turned off to accept a sloppy client.

## What changed in this major

Nest 12 adds `@Body({ schema })` plus `StandardSchemaValidationPipe`. Class DTOs and `ValidationPipe` still work.

## Deprecated APIs to never generate

`HttpModule` from `@nestjs/common` is the deprecated export. Import `HttpModule` from `@nestjs/axios`.

## Commands

Run the package test script.

## Example

```ts
@Post()
create(@Body({ schema: createNoteSchema }) body: CreateNote) {
  return this.notes.create(body)
}
```
Register `StandardSchemaValidationPipe` or this schema is metadata only.
