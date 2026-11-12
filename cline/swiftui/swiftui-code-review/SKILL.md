---
id: "cline-swiftui-code-review"
slug: "cline/swiftui/swiftui-code-review/SKILL"
title: "SwiftUI Code Review Skill for Cline"
description: "Review a SwiftUI change for actor isolation, observation, and main-actor UI updates. Use for a SwiftUI code review. Do not use for a non-Swift repository or to silence isolation with unchecked Sendable."
type: "skill"
tools:
  - "cline"
stack: "swiftui"
tags:
  - "swiftui"
  - "swift"
  - "ios"
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
  - "swift@6.4"
updated_for: "Swift 6.4, Nov 2026"
---

# SwiftUI Code Review Skill for Cline

## Install

Install the native export at `.cline/skills/swiftui-code-review/SKILL.md`.
Copy that export, not this catalog file. Catalog fields such as `tools` and `author` are for presets.dev.
Install one skill file per name. Cursor, GitHub Copilot, Codex, Antigravity CLI, and Devin can all read `.agents/skills`, so a second copy with the same name collides.

<!-- native:start -->

# SwiftUI Code Review Skill for Cline

Cline skill `swiftui-code-review` for SwiftUI. `/swiftui-code-review` forces it. A global skill of the same name overrides this project file.

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
Input: `ProfileView.body` starts `Task { await model.load() }`, so every redraw starts another load.
Output: high | ProfileView.swift:11 | the load is an unstructured task in `body` | use `.task { await model.load() }`. A `Task` inside a button action is not this finding.
```

Do not flag the valid pattern named in the standards. Flag the mistake next to it.

## Stop

Stop when the user asks you to disable strict concurrency to get a green build.

## Severity

`high` is a bug a caller can hit or a secret that leaks. `medium` is a broken contract that needs a specific input. `low` is a cleanup that does not change behaviour.
