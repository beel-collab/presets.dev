---
id: "cline-react-native-rules"
slug: "cline/react-native/react-native-rules"
title: "React Native Cline Rules: Expo, Navigation and Native Lifecycle"
description: "Cline rules for React Native: Expo, Navigation and Native Lifecycle. Structure, data, errors, security, performance, and tests. React Native 0.88.1, Nov 2026."
type: "rule"
tools:
  - "cline"
stack: "react-native"
tags:
  - "react-native"
  - "expo"
  - "mobile"
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

# React Native Cline Rules: Expo, Navigation and Native Lifecycle

## Install

Install the native export at `.clinerules/react-native-rules.md` (do not also copy it to `.cline/rules/`).
Copy that export, not this catalog file. Catalog fields such as `tools` and `author` are for presets.dev.
Install one skill file per name. Cursor, GitHub Copilot, Codex, Antigravity CLI, and Devin can all read `.agents/skills`, so a second copy with the same name collides.

<!-- native:start -->

# React Native Cline Rules: Expo, Navigation and Native Lifecycle

Conditional Cline rule for React Native. Install it under `.clinerules/` only.

## Updated for React Native 0.88.1, Nov 2026
Do not upgrade dependencies or the framework version unless the task asks.

## Project shape

Read `app.json` or `app.config`, the navigation library, and whether the app is Expo or a bare workflow. Follow that. Screens live where the navigator already registers them. Platform files (`ios`, `android`, `.native`) stay the split the repo uses.

A new native module or config plugin is a product decision. Do not add one to solve a JavaScript problem.

## Components and state

The React rules still apply: derive values during render, clean up effects, and do not store props in state. In a native stack, pushing another screen does not unmount the one underneath. Focus-owned work uses `useFocusEffect` and returns a cleanup that runs on blur. Effect cleanup runs when the screen actually unmounts, which is later, often after it is popped. Do not treat blur as unmount.

After `await`, check that the screen is still focused before you set state or navigate. A request started on focus is cancelled in the focus cleanup.

## Platform behavior

Branch on `Platform.OS` for a real platform difference, not for a style you can share. A web preview in Expo is not a phone. Do not call `window`, `document`, or a DOM layout API.

Permissions are requested at the moment of use, with a reason the platform stores already show. Handle the denial. Do not assume a permission granted in the simulator is granted on a device.

Safe area, keyboard, and back behavior come from the libraries the app already uses. A fixed padding that ignores the inset will collide with the notch or the gesture bar.

## Navigation and data

Register screens in the existing navigator. Pass serializable params. Do not pass functions or class instances through route params.

Fetch with the client's existing data library. Cache keys include the signed-in user when the payload is private. Sign out clears that cache.

## Errors, security, and tests

An error boundary around a navigator section beats a red box in production. Log to the project's crash reporter. Do not `console.log` tokens.

Tokens live in the secure store the app already uses, not in AsyncStorage when that store is the project's choice for secrets. Deep links validate the host and the path before they navigate.

Run the project's Jest or Maestro target for the logic you changed. A device check is required before you call a release ready. Say so when you only ran a simulator, or when you ran nothing.

## Mistakes to avoid

- A web DOM API in a native screen.
- `setState` after an `await` on a screen that may have unmounted.
- An Expo SDK bump that does not match the React Native version.
- A route param that contains a secret or a function.
- Calling the work done without a device or a clearly labeled simulator run.

## What changed in this major

React Native 0.88 is the current line. Expo SDK 58 is current npm latest. Do not mix an SDK with an unsupported React Native.

## Deprecated APIs to never generate

`componentWillMount` is a legacy lifecycle. Do not generate it.

## Commands

Run the unit test script. Say when no device was used.

## Example

```tsx
useFocusEffect(useCallback(() => {
  const ac = new AbortController()
  load(ac.signal)
  return () => ac.abort()
}, []))
```
