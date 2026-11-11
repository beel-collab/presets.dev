---
id: "windsurf-flutter-rules"
slug: "windsurf/flutter/flutter-rules"
title: "Flutter Windsurf Rules: Widgets, Async UI and Platform Builds"
description: "Windsurf rules for Flutter: Widgets, Async UI and Platform Builds. Structure, data, errors, security, performance, and tests. Flutter 3.47 stable line, Nov 2026."
type: "rule"
tools:
  - "windsurf"
stack: "flutter"
tags:
  - "flutter"
  - "dart"
  - "widgets"
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
  - "flutter@3.47"
updated_for: "Flutter 3.47 stable line, Nov 2026"
---

# Flutter Windsurf Rules: Widgets, Async UI and Platform Builds

## Install

Install the native export at `.devin/rules/flutter-rules.md` and, for legacy Cascade, `.windsurf/rules/flutter-rules.md`.
Copy that export, not this catalog file. Catalog fields such as `tools` and `author` are for presets.dev.
Install one tool's skill for a checkout. Do not drop every tool's copy into `.agents/skills` under the same name.

<!-- native:start -->

# Flutter Windsurf Rules: Widgets, Async UI and Platform Builds

Rule for Flutter on current Devin (`.devin/rules`) and legacy Cascade (`.windsurf/rules`). The trigger is model decision. Use `flutter-test-writer` for a review.

## Updated for Flutter 3.47, Nov 2026

Write for the Flutter version in `pubspec.yaml` and the SDK constraint. The 3.47 stable line is the series to follow when the project is already on it, including its split of Material and Cupertino packages and the Kotlin migration for Android. Do not bump Flutter or change the Android embedding unless the task asks. Do not edit generated files under `.dart_tool` or plugin registries.

## Project shape

Widgets are small. A screen composes widgets. State that outlives a screen lives in the project's state solution, not in a global mutable singleton you add today. Follow the existing folder split: `ui`, `data`, and `domain`, or whatever the repo already has.

`BuildContext` is only valid while the element is mounted. After `await`, check `context.mounted` before you use `context` for navigation, a theme, or `setState`.

## Async UI

A future or a stream the widget owns is disposed. A `StreamSubscription` is canceled in `dispose`. Do not call `setState` after dispose. Show loading, empty, and error states. An error that only prints to the console looks like a frozen spinner.

## Platform builds

Android and iOS configuration stay in the files the project already owns. A Kotlin migration is a named task, not a side effect of a Dart change. Read the current Gradle and Kotlin versions before you touch them. Platform channels have a typed contract. Do not pass an untyped map when the project has a pigeon or a freezed model for it.

Assets are declared. A missing asset is a test failure, not a runtime surprise you ignore.

## Errors, accessibility, and tests

Catch a failed load and render the message. Do not `catch (_)` and continue with null data that the UI treats as empty success.

Buttons have semantics. Contrast and tap targets follow the Material or Cupertino widget you used, not a custom gesture detector with no label.

Widget tests pump the widget, find by text or key, and tap. A unit test covers a notifier or a parser without a device. An integration test is how you prove a flow. Run `flutter test` for the file you added. Record the output. Say when you did not run a device.

## Mistakes to avoid

- `BuildContext` used after `await` without `context.mounted`.
- A subscription that is never canceled.
- A generated plugin file edited by hand.
- An Android build change copied from an old embedding.
- A test that never pumps a frame and still claims the widget works.
