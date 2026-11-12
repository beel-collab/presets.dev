---
id: "claude-kotlin-code-review"
slug: "claude/skills/kotlin/kotlin-code-review/SKILL"
title: "Kotlin Code Review Skill for Claude Code"
description: "Review a Kotlin change for coroutine cancellation, lifecycle-aware flows, and null assertions. Use for a Kotlin code review. Do not use for a non-Kotlin repository or to swallow CancellationException."
type: "skill"
tools:
  - "claude"
stack: "kotlin"
tags:
  - "kotlin"
  - "coroutines"
  - "android"
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
  - "kotlin@2.4"
updated_for: "Kotlin 2.4 stable line, Nov 2026"
---

# Kotlin Code Review Skill for Claude Code

## Install

Install the native export at `.claude/skills/kotlin-code-review/SKILL.md`.
Copy that export, not this catalog file. Catalog fields such as `tools` and `author` are for presets.dev.
Install one tool's skill for a checkout. Do not drop every tool's copy into `.agents/skills` under the same name.

<!-- native:start -->

# Kotlin Code Review Skill for Claude Code

Claude Code skill `kotlin-code-review` for Kotlin. The command is `/kotlin-code-review`. Leave the normal permission prompts on.

## When to run

Run this review for a Kotlin coroutine, a Flow, a Compose screen, or an Android lifecycle change.

## When to leave it

Stop for a non-Kotlin repository. Do not upgrade Kotlin or Compose unless the user asked.

## Steps

1. Read the Kotlin version in the version catalog or `build.gradle`. A 2.4-only API on an older compiler is a high finding.
2. Search for `GlobalScope`, `runBlocking`, and `catch (e: Exception)` that does not rethrow `CancellationException`. Each is a high finding on app code.
3. Check Flow collection. A collection that ignores the lifecycle is a finding.
4. Search for `!!`. Each one on external data is a finding.
5. Run the unit test task only if the user asked. Otherwise write `not run`. Do not claim a device run you did not do.

## Output

Findings with severity, file, line, the cancellation or null bug, and a fix.

## Stop

Stop when the user asks you to swallow cancellation so a job "always finishes".

## Severity

`high` is a bug a caller can hit or a secret that leaks. `medium` is a broken contract that needs a specific input. `low` is a cleanup that does not change behaviour.

## Output

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
