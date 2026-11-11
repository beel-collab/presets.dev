---
name: "dotnet-code-review"
description: "Review a .NET change for async cancellation, endpoint authorization, and C# syntax the target framework does not have. Use for a .NET code review. Do not use for a non-.NET repository or to retarget the TFM unasked."
---

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
