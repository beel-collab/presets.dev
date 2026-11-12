---
id: "cursor-dotnet-code-review"
slug: "cursor/dotnet/dotnet-code-review/SKILL"
title: ".NET Code Review Skill for Cursor"
description: "Review a .NET change for async cancellation, endpoint authorization, and C# syntax the target framework does not have. Use for a .NET code review. Do not use for a non-.NET repository or to retarget the TFM unasked."
type: "skill"
tools:
  - "cursor"
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
  - "Cursor docs 2026-11-11; app not executed"
created: "2026-11-11"
updated: "2026-11-11"
libs:
  - "dotnet@10"
updated_for: ".NET 10 LTS and .NET 11, Nov 2026"
---

# .NET Code Review Skill for Cursor

## Install

Install the native export at `.cursor/skills/dotnet-code-review/SKILL.md`.
Copy that export, not this catalog file. Catalog fields such as `tools` and `author` are for presets.dev.
Install one tool's skill for a checkout. Do not drop every tool's copy into `.agents/skills` under the same name.

<!-- native:start -->

# .NET Code Review Skill for Cursor

Cursor skill `dotnet-code-review` for .NET. Run it with `/dotnet-code-review`, or let Agent select it when the request matches. `paths` only limits automatic surfacing.

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
Input: a one-line change that matches a rule in the standards.
Output: either one finding with file and line, or "No findings" when the change is the valid pattern named in the standards.
```

Do not flag the valid pattern named in the standards. Flag the mistake next to it.

## Stop

Stop when the user asks you to suppress nullable warnings project-wide or to block on async to "keep it simple".

## Severity

`high` is a bug a caller can hit or a secret that leaks. `medium` is a broken contract that needs a specific input. `low` is a cleanup that does not change behaviour.
