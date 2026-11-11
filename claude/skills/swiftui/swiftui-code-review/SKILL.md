---
id: "claude-swiftui-code-review"
slug: "claude/skills/swiftui/swiftui-code-review/SKILL"
title: "SwiftUI Code Review Skill for Claude Code"
description: "Claude Code skill for a SwiftUI code review. Use when you want that code review on a SwiftUI change. Do not use it for a different stack."
type: "skill"
tools:
  - "claude"
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
  - "Claude Code docs 2026-11-11; CLI not run"
created: "2026-11-11"
updated: "2026-11-11"
libs:
  - "swift@6.4"
updated_for: "Swift 6.4, Nov 2026"
---

# SwiftUI Code Review Skill for Claude Code

## Install

Install the native export at `.claude/skills/swiftui-code-review/SKILL.md`.
Copy that export, not this catalog file. Catalog fields such as `tools` and `author` are for presets.dev.
Install one tool's skill for a checkout. Do not drop every tool's copy into `.agents/skills` under the same name.

<!-- native:start -->

# SwiftUI Code Review Skill for Claude Code

Claude Code skill `swiftui-code-review` for SwiftUI. The command is `/swiftui-code-review`. Leave the normal permission prompts on.

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
