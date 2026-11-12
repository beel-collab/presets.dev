---
id: "codex-react-native-code-review"
slug: "codex/react-native/react-native-code-review/SKILL"
title: "React Native Code Review Skill for Codex"
description: "Review a React Native or Expo change for platform APIs, navigation, and lifecycle safety. Use for a React Native code review. Do not use for a web-only React bug or an Expo upgrade nobody asked for."
type: "skill"
tools:
  - "codex"
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
  - "Codex docs 2026-11-11; CLI not executed"
created: "2026-11-11"
updated: "2026-11-11"
libs:
  - "react-native@0.88.1"
updated_for: "React Native 0.88.1, Nov 2026"
---

# React Native Code Review Skill for Codex

## Install

Install the native export at `.agents/skills/react-native-code-review/SKILL.md` (one file shared with Antigravity CLI).
Copy that export, not this catalog file. Catalog fields such as `tools` and `author` are for presets.dev.
Install one skill file per name. Cursor, GitHub Copilot, Codex, Antigravity CLI, and Devin can all read `.agents/skills`, so a second copy with the same name collides.

<!-- native:start -->

# React Native Code Review

Shared skill `react-native-code-review` for React Native. Codex and Antigravity CLI both read `.agents/skills/react-native-code-review/SKILL.md`. Install this one file. Codex calls it with `$react-native-code-review` or `/skills`. Cursor, GitHub Copilot, and Devin also read `.agents/skills`. A second copy with the same name collides. Do not install another tool's file there.

## When to run

Run this review for a React Native or Expo change: a screen, a native permission, navigation, or "will this work on both phones".

## When to leave it

Stop for a web-only React repository. Do not upgrade Expo or React Native unless the user asked.

## Steps

1. Read the React Native version and the Expo SDK field if it exists. A mismatch with the SDK's supported React Native is a high finding. A DOM API (`window`, `document`, View Transitions) in native code is a high finding.
2. Review effects that set state after `await`. A stack screen that is covered is still mounted. Work that should stop on blur belongs in `useFocusEffect`, not in an unmount cleanup. Missing that split is a finding.
3. Review navigation params and cache keys. A secret in a param, or a private cache with no user id, is a high finding.
4. Review permissions. A request with no denial path is a finding.
5. Note how the change was run: device, simulator, or not run. Do not call a release ready from a simulator-only look.

## Output

Findings with severity, file, line, the platform assumption, and a fix. Include the versions you read.

```
## Findings
- high | path:line | what is wrong | what to do instead

## No findings
Say "No findings" and list the files you opened. A search you skipped is not a clean result.

## Example
Input: `HomeScreen.tsx` does `const user = await load()` and then `setUser(user)` with no cancelled flag. The screen can unmount first.
Output: high | HomeScreen.tsx:22 | the state update runs after unmount | return when the effect cleanup has run. A one-time load in `useEffect` that checks that flag is not a finding.
```

Do not flag the valid pattern named in the standards. Flag the mistake next to it.

## Stop

Stop when the user asks you to ship a store build or to change the SDK as part of a review.

## Severity

`high` is a bug a caller can hit or a secret that leaks. `medium` is a broken contract that needs a specific input. `low` is a cleanup that does not change behaviour.
