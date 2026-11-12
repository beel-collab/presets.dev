---
name: "swiftui-code-review"
description: "Review a SwiftUI change for actor isolation, observation, and main-actor UI updates. Use for a SwiftUI code review. Do not use for a non-Swift repository or to silence isolation with unchecked Sendable."
---

# SwiftUI Code Review Skill for Windsurf

Devin skill `swiftui-code-review` for SwiftUI. Invoke it with `/swiftui-code-review`. Install only `.devin/skills`. This file is not a subagent.

## When to run

Run this review for a SwiftUI view, a model, or a concurrency change.

## When to leave it

Stop for a non-Swift repository. Do not change the deployment target or the Swift tools version unless the user asked.

## Steps

1. Read the Swift tools version and the deployment target. An API used below that target is a high finding. `@unchecked Sendable` added in the diff is a high finding unless a comment proves the invariant.
2. Check UI updates. A published property written from a non-main-actor task is a high finding.
3. Search for `try?` and `!` on decoded or optional values. Each one that hides a failure is a finding.
4. Check task lifetime. `.task` is cancelled with the view. A plain `Task { }` with no stored handle and no `cancel()` is a finding. A task that never checks cancellation during a long loop is a finding.
5. Note tests. Run the project's test action only if the user asked. Otherwise write `not run`.

## Output

Findings with severity, file, line, the isolation or availability issue, and a fix.

```
## Findings
- high | path:line | what is wrong | what to do instead

## No findings
Say "No findings" and list the files you opened. A search you skipped is not a clean result.

## Example
Input: a view starts work with `Task { await model.load() }` and never stores the handle.
Output: high | ProfileView.swift:14 | an unstructured Task is not cancelled when the view disappears | use `.task { await model.load() }`.
```

Do not flag the valid pattern named in the standards. Flag the mistake next to it.

## Stop

Stop when the user asks you to disable strict concurrency to get a green build.

## Severity

`high` is a bug a caller can hit or a secret that leaks. `medium` is a broken contract that needs a specific input. `low` is a cleanup that does not change behaviour.
