---
id: "claude-flutter-test-writer"
slug: "claude/skills/flutter/flutter-test-writer/SKILL"
title: "Flutter Test Writer Skill for Claude Code"
description: "Write a Flutter widget or unit test for a behavior, including the mounted check after an await. Use when the user asks for Flutter tests. Do not use for a non-Flutter repository or to edit a generated file."
type: "skill"
tools:
  - "claude"
stack: "flutter"
tags:
  - "flutter"
  - "dart"
  - "widgets"
  - "testing"
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
  - "flutter@3.50"
updated_for: "Flutter 3.50, Nov 2026"
---

# Flutter Test Writer Skill for Claude Code

## Install

Install the native export at `.claude/skills/flutter-test-writer/SKILL.md`.
Copy that export, not this catalog file. Catalog fields such as `tools` and `author` are for presets.dev.
Install one tool's skill for a checkout. Do not drop every tool's copy into `.agents/skills` under the same name.

<!-- native:start -->

# Flutter Test Writer Skill for Claude Code

Claude Code skill `flutter-test-writer` for Flutter. The command is `/flutter-test-writer`. Leave the normal permission prompts on.

## When to run

Run this when the user wants a Flutter test: a widget test, a unit test, or a regression for a UI bug.

## When to leave it

Stop for a non-Flutter repository. Do not add an integration driver the project does not have unless the user asked.

## Steps

1. Read `pubspec.yaml` and an existing test so the imports and `testWidgets` style match.
2. Name the behavior. Include the async case: after a future completes, the widget shows the result, and a disposed widget does not call `setState`.
3. Pump the widget. Find by text, key, or type. Tap or enter text. `pumpAndSettle` only when the animation is expected to finish. A fixed `Future.delayed` in a test is a smell.
4. Do not edit generated files to make the test compile. Fix the source.
5. Run `flutter test` on the new file. Record the output. If the SDK is missing, write `not run`.

## Output

The test path, the behavior, the command, and the result.

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

Stop when the user asks you to mark the test passed without running it, or to change the Flutter SDK constraint to satisfy one import.

## Severity

`high` is a bug a caller can hit or a secret that leaks. `medium` is a broken contract that needs a specific input. `low` is a cleanup that does not change behaviour.
