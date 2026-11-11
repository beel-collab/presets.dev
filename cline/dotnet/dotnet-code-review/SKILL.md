---
id: "cline-dotnet-code-review"
slug: "cline/dotnet/dotnet-code-review/SKILL"
title: ".NET Code Review Skill for Cline"
description: "Cline skill for a .NET code review. Use when you want that code review on a .NET change. Do not use it for a different stack."
type: "skill"
tools:
  - "cline"
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
  - "Cline docs 2026-11-11; app not executed"
created: "2026-11-11"
updated: "2026-11-11"
libs:
  - "dotnet@10"
updated_for: ".NET 10 LTS and .NET 11, Nov 2026"
---

# .NET Code Review Skill for Cline

## Install

Install the native export at `.cline/skills/dotnet-code-review/SKILL.md`.
Copy that export, not this catalog file. Catalog fields such as `tools` and `author` are for presets.dev.
Install one tool's skill for a checkout. Do not drop every tool's copy into `.agents/skills` under the same name.

<!-- native:start -->

# .NET Code Review Skill for Cline

Cline skill `dotnet-code-review` for .NET. `/dotnet-code-review` forces it. A global skill of the same name overrides this project file.

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

## Stop

Stop when the user asks you to suppress nullable warnings project-wide or to block on async to "keep it simple".
