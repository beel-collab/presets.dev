---
id: "antigravity-dotnet-code-review"
slug: "antigravity/dotnet/dotnet-code-review/SKILL"
title: ".NET Code Review Skill for Antigravity CLI"
description: "Review a .NET change for async cancellation, endpoint authorization, and C# syntax the target framework does not have. Use for a .NET code review. Do not use for a non-.NET repository or to retarget the TFM unasked."
type: "skill"
tools:
  - "antigravity"
stack: "dotnet"
tags:
  - "dotnet"
  - "csharp"
  - "async"
  - "code-review"
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

# .NET Code Review Skill for Antigravity CLI

## Install

Install the native export at `.agents/skills/dotnet-code-review/SKILL.md` (one file shared with Codex).
Copy that export, not this catalog file. Catalog fields such as `tools` and `author` are for presets.dev.
Install one skill file per name. Cursor, GitHub Copilot, Codex, Antigravity CLI, and Devin can all read `.agents/skills`, so a second copy with the same name collides.

<!-- native:start -->

# .NET Code Review

Shared skill `dotnet-code-review` for .NET. Codex and Antigravity CLI both read `.agents/skills/dotnet-code-review/SKILL.md`. Install this one file. Codex calls it with `$dotnet-code-review` or `/skills`. Cursor, GitHub Copilot, and Devin also read `.agents/skills`. A second copy with the same name collides. Do not install another tool's file there.

## When to run

Run this review for a .NET or C# change: an endpoint, an EF query, or an async method.

## When to leave it

Stop for a non-.NET repository. Do not change `TargetFramework` unless the user asked.

## Steps

1. Read `TargetFramework`. C# 15 unions or other new syntax on a .NET 10 or older TFM is a high finding.
2. Search the diff for `.Result`, `.Wait()`, and `async void`. Each on a request path is a high finding.
3. Confirm `CancellationToken` is accepted and passed into EF, HTTP, and delays. A token that is ignored is a finding.
4. Confirm writes call `RequireAuthorization` or the controller equivalent. A missing check is a high finding.
5. Review EF. `ToList` before a `Where`, or a loop of queries, is a finding.
6. Run `dotnet test` only if the user asked. Otherwise write `not run`.

## Output

Findings with severity, file, line, the TFM, and a fix that compiles on that TFM.

```
## Findings
- high | path:line | what is wrong | what to do instead

## No findings
Say "No findings" and list the files you opened. A search you skipped is not a clean result.

## Example
Input: a `net10.0` project adds a C# 15 union to a request DTO.
Output: high | NoteDto.cs:3 | C# 15 unions are not available on `net10.0` | keep the DTO as a record, or retarget only if the user asked.
```

Do not flag the valid pattern named in the standards. Flag the mistake next to it.

## Stop

Stop when the user asks you to suppress nullable warnings project-wide or to block on async to "keep it simple".

## Severity

`high` is a bug a caller can hit or a secret that leaks. `medium` is a broken contract that needs a specific input. `low` is a cleanup that does not change behaviour.
