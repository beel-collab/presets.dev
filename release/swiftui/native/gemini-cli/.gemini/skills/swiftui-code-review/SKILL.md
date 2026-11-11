---
name: "swiftui-code-review"
description: "Review a SwiftUI change for actor isolation, observation, and main-actor UI updates. Use for a SwiftUI code review. Do not use for a non-Swift repository or to silence isolation with unchecked Sendable."
---

# SwiftUI Code Review Skill for Gemini CLI

Gemini CLI skill `swiftui-code-review` for SwiftUI. Activation calls `activate_skill` and waits for consent. Keep this copy under `.gemini/skills`.

## When to run

Run this review for a SwiftUI view, a model, or a concurrency change.

## When to leave it

Stop for a non-Swift repository. Do not change the deployment target or the Swift tools version unless the user asked.

## Steps

1. Read the Swift tools version and the deployment target. An API used below that target is a high finding. `@unchecked Sendable` added in the diff is a high finding unless a comment proves the invariant.
2. Check UI updates. A published property written from a non-main-actor task is a high finding.
3. Search for `try?` and `!` on decoded or optional values. Each one that hides a failure is a finding.
4. Check `Task` lifetime. A task stored without cancellation when the view goes away is a finding.
5. Note tests. Run the project's test action only if the user asked. Otherwise write `not run`.

## Output

Findings with severity, file, line, the isolation or availability issue, and a fix.

## Stop

Stop when the user asks you to disable strict concurrency to get a green build.
