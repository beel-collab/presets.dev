---
id: "cline-react-native-code-review"
slug: "cline/react-native/react-native-code-review/SKILL"
title: "React Native Code Review Skill for Cline"
description: "Cline skill for a React Native code review. Use when you want that code review on a React Native change. Do not use it for a different stack."
type: "skill"
tools:
  - "cline"
stack: "react-native"
tags:
  - "react-native"
  - "expo"
  - "mobile"
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
  - "react-native@0.88.1"
updated_for: "React Native 0.88.1, Nov 2026"
---

# React Native Code Review Skill for Cline

## Install

Install the native export at `.cline/skills/react-native-code-review/SKILL.md`.
Copy that export, not this catalog file. Catalog fields such as `tools` and `author` are for presets.dev.
Install one tool's skill for a checkout. Do not drop every tool's copy into `.agents/skills` under the same name.

<!-- native:start -->

# React Native Code Review Skill for Cline

Cline skill `react-native-code-review` for React Native. `/react-native-code-review` forces it. A global skill of the same name overrides this project file.

## When to run

Run this review for a React Native or Expo change: a screen, a native permission, navigation, or "will this work on both phones".

## When to leave it

Stop for a web-only React repository. Do not upgrade Expo or React Native unless the user asked.

## Steps

1. Read the React Native version and the Expo SDK field if it exists. A mismatch with the SDK's supported React Native is a high finding. A DOM API (`window`, `document`, View Transitions) in native code is a high finding.
2. Review effects that set state after `await`. A missing focus or mounted check is a finding.
3. Review navigation params and cache keys. A secret in a param, or a private cache with no user id, is a high finding.
4. Review permissions. A request with no denial path is a finding.
5. Note how the change was run: device, simulator, or not run. Do not call a release ready from a simulator-only look.

## Output

Findings with severity, file, line, the platform assumption, and a fix. Include the versions you read.

## Stop

Stop when the user asks you to ship a store build or to change the SDK as part of a review.
