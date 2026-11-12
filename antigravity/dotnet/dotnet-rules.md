---
id: "antigravity-dotnet-rules"
slug: "antigravity/dotnet/dotnet-rules"
title: ".NET Antigravity CLI Rules: Nullable Contracts, Async and Endpoints"
description: "Antigravity CLI rules for .NET: Nullable Contracts, Async and Endpoints. Append to GEMINI.md. Structure, security, and tests. .NET 10 LTS and .NET 11, Nov 2026."
type: "rule"
tools:
  - "antigravity"
stack: "dotnet"
tags:
  - "dotnet"
  - "csharp"
  - "async"
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
  - "dotnet@10"
updated_for: ".NET 10 LTS and .NET 11, Nov 2026"
---

# .NET Antigravity CLI Rules: Nullable Contracts, Async and Endpoints

## Install

Install the native export at `GEMINI.md` or `AGENTS.md` as an appended section.
Copy that export, not this catalog file. Catalog fields such as `tools` and `author` are for presets.dev.
Install one tool's skill for a checkout. Do not drop every tool's copy into `.agents/skills` under the same name.

<!-- native:start -->

# .NET Antigravity CLI Rules: Nullable Contracts, Async and Endpoints

Section to append to `GEMINI.md` for .NET. Antigravity CLI also reads `AGENTS.md`. Confirm the loaded rules before you rely on them.

## Updated for .NET 10 LTS and .NET 11, Nov 2026

.NET 11 shipped in November 2026, with C# 15 unions and closed hierarchies. A project that still targets .NET 10 LTS does not get that syntax. Read the `TargetFramework` before you write a language feature. Do not retarget the project unless the task asks. Nullable reference types stay enabled when the project has them on.

## Project shape

Match the existing minimal API or controller style. A handler is small. Domain rules live in a type the handler calls. Do not grow a static `Program.cs` into the place every rule lives.

Projects, not random folders, are the compilation boundary. Internal types stay internal.

## Contracts

Public methods say whether a value can be null. Do not silence the nullable warning with `!` unless you just checked. A union or a closed hierarchy is appropriate on a TFM that has C# 15. On an older TFM, use the pattern the codebase already uses. Do not paste preview syntax into a .NET 10 build.

Validate input at the endpoint with the project's validator. The validated type is what the handler accepts.

## Async

Async methods take a `CancellationToken` and pass it on. Do not use `async void` except for an event handler the platform requires. Do not block on a task with `.Result` or `.Wait()`. A timeout is a `CancellationTokenSource` linked to the caller's token, not a discarded task.

EF Core queries stay `IQueryable` until the filter is applied, then `ToListAsync(ct)`. A loop of `await` per row is an N+1. Add `Include` or a projection.

## Endpoints and security

Every endpoint that changes data has an authorization policy. A new minimal API calls `RequireAuthorization` the way its neighbors do. Do not map an anonymous write.

Return the status the API uses. A problem-details body is for the error, not a stack trace. Do not log tokens.

## Tests

Use the project's `WebApplicationFactory` or unit style. Cover a canceled token, a forbidden caller, and a query filter. Run `dotnet test` for the project you changed. Record the output.

## Mistakes to avoid

- C# 15 syntax in a TFM that does not have it.
- `async void`, or `.Result` on a hot path.
- A `CancellationToken` that stops at the first method.
- An endpoint with no authorization on a write.
- An EF query that loads the table and filters in memory.

## What changed in this major

.NET 11 can use C# 15 unions. A `net10.0` project cannot. Pass `CancellationToken` through.

## Deprecated APIs to never generate

No API covered here was deprecated or removed.

## Commands

Run `dotnet test` for the touched project.

## Example

```csharp
app.MapPost("/notes", async (Note body, ClaimsPrincipal user, CancellationToken ct) =>
{
    return Results.Ok(await store.AddAsync(body, user, ct));
}).RequireAuthorization();
```
