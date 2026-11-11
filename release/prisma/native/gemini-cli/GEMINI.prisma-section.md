<!-- Append this section to GEMINI.md. Do not replace the existing file. Confirm with /memory show. -->

# Prisma Gemini CLI Rules: Schema, Migrations and Query Shape

Section to append to `GEMINI.md` for Prisma. Confirm with `/memory show`. The review skill waits for consent before it runs.

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
