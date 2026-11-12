---
id: "windsurf-flutter-test-writer"
slug: "windsurf/flutter/flutter-test-writer/SKILL"
title: "Flutter Test Writer Skill for Windsurf"
description: "Write a Flutter widget or unit test for a behavior, including the mounted check after an await. Use when the user asks for Flutter tests. Do not use for a non-Flutter repository or to edit a generated file."
type: "skill"
tools:
  - "windsurf"
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
  - "Devin and Cascade docs 2026-11-11; not run"
created: "2026-11-11"
updated: "2026-11-11"
libs:
  - "flutter@3.50"
updated_for: "Flutter 3.50, Nov 2026"
---

# Flutter Test Writer Skill for Windsurf

## Install

Install the native export at `.devin/skills/flutter-test-writer/SKILL.md`.
Copy that export, not this catalog file. Catalog fields such as `tools` and `author` are for presets.dev.
Install one skill file per name. Cursor, GitHub Copilot, Codex, Antigravity CLI, and Devin can all read `.agents/skills`, so a second copy with the same name collides.

<!-- native:start -->

# Flutter Test Writer Skill for Windsurf

Devin skill `flutter-test-writer` for Flutter. Invoke it with `/flutter-test-writer`. Install only `.devin/skills`. This file is not a subagent.

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

```
## Files written
- test/profile_page_test.dart

## Covered
- After `lookup()` completes, the widget pops only if `context.mounted` is true.

## How to run
flutter test test/profile_page_test.dart

## Result
pass, fail, or not run. If the SDK is missing, say so. Do not report a pass you did not see.

## Gaps
- Devices and platforms this run did not exercise.
```

Example: `profile_page.dart` pops after `await lookup()` with no `mounted` check. The test pumps the widget, completes the future after unmount, and expects no `Navigator` use. Run `flutter test` on that file.

## Stop

Stop when the user asks you to mark the test passed without running it, or to change the Flutter SDK constraint to satisfy one import.
