---
id: "codex-prisma-rules"
slug: "codex/prisma/prisma-rules"
title: "Prisma Codex Instructions: Schema, Migrations and Query Shape"
description: "Codex instructions for Prisma: Schema, Migrations and Query Shape. Append to AGENTS.md. Structure, security, and tests. Prisma 7.10.1 stable, Nov 2026."
type: "rule"
tools:
  - "codex"
stack: "prisma"
tags:
  - "prisma"
  - "postgresql"
  - "migrations"
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
  - "prisma@7.10.1"
updated_for: "Prisma 7.10.1 stable, Nov 2026"
---

# Prisma Codex Instructions: Schema, Migrations and Query Shape

## Install

Install the native export at `AGENTS.md` as an appended section, not a replacement and not a custom agent.
Copy that export, not this catalog file. Catalog fields such as `tools` and `author` are for presets.dev.
Install one tool's skill for a checkout. Do not drop every tool's copy into `.agents/skills` under the same name.

<!-- native:start -->

# Prisma Codex Instructions: Schema, Migrations and Query Shape

Section to append to `AGENTS.md` for Prisma. This is project guidance, not a custom agent. Use `$prisma-code-review` for a review.

## Updated for Prisma 7.10.1 stable, Nov 2026

On 11 November 2026 the npm `latest` tag for `prisma` was 8.0.0-rc.33, a release candidate. The `prev` tag was 7.10.1, the stable line. Stay on the major the repository installs. Do not bump a project to Prisma 8 because `latest` resolved to the RC. Postgres stays on the major the project runs. Do not assume a newer Postgres major is what this app uses.

## Project shape

`schema.prisma` is the model. Migrations in `prisma/migrations` are the history. Do not edit a migration that has already shipped. Add a new one. The client is generated. Do not hand-edit generated files.

The shadow database is a disposable database. Never point `shadowDatabaseUrl` at production. A migrate command against production is something a person runs on purpose. Do not run `migrate dev` or `migrate reset` against a shared database.

## Schema and migrations

Name relations on both sides. An optional field and a required field are different. A new required column on a table that has rows needs a default or a backfill in the same migration. Do not drop a column in the same change that still reads it.

Indexes follow the filters and the foreign keys you query. A unique constraint matches the real uniqueness rule, not a guess.

## Queries

`include` and `select` load what the screen needs. A loop that calls `findUnique` per row is an N+1. Lift it into one query or a relation include. Paginate lists with `take` and a cursor. Do not `findMany` an unbounded table into memory.

A transaction wraps a write that must succeed or fail together. Interactive transactions stay short. Do not hold one open across a network call to a third party.

`$queryRaw` uses parameters. Do not concatenate user input into SQL. `$executeRawUnsafe` is a review, not a shortcut.

## Errors and security

Catch a known request error, such as a unique conflict, and return the conflict the API already uses. Do not swallow `PrismaClientKnownRequestError`.

The Prisma client talks to the database from the server. The connection string is not in a client bundle and not in a committed `.env`. Row access still belongs to the application or to database policies. Prisma does not replace authorization.

## Tests

A migration test runs on a disposable database. Assert the column, the index, and the backfill. A query test asserts the number of queries when the project already counts them, or asserts the returned shape. Record the command. Do not claim you applied the migration to production.

## Mistakes to avoid

- Upgrading to the Prisma 8 RC because it was tagged `latest`.
- `migrate dev` or a shadow database pointed at production.
- Editing a shipped migration.
- An N+1 loop of `findUnique`.
- String-built raw SQL.
