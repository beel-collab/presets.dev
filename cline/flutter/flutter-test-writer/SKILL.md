---
id: "cline-flutter-test-writer"
slug: "cline/flutter/flutter-test-writer/SKILL"
title: "Flutter Test Writer Skill for Cline"
description: "Cline skill for a Flutter test writer. Use when you want that test writer on a Flutter change. Do not use it for a different stack."
type: "skill"
tools:
  - "cline"
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
  - "Cline docs 2026-11-11; app not executed"
created: "2026-11-11"
updated: "2026-11-11"
libs:
  - "flutter@3.47"
updated_for: "Flutter 3.47 stable line, Nov 2026"
---

# Flutter Test Writer Skill for Cline

## Install

Install the native export at `.cline/skills/flutter-test-writer/SKILL.md`.
Copy that export, not this catalog file. Catalog fields such as `tools` and `author` are for presets.dev.
Install one tool's skill for a checkout. Do not drop every tool's copy into `.agents/skills` under the same name.

<!-- native:start -->

# Flutter Test Writer Skill for Cline

Cline skill `flutter-test-writer` for Flutter. `/flutter-test-writer` forces it. A global skill of the same name overrides this project file.

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

## Stop

Stop when the user asks you to mark the test passed without running it, or to change the Flutter SDK constraint to satisfy one import.
