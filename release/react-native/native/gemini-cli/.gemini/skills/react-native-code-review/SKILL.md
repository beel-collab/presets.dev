---
name: "react-native-code-review"
description: "Review a React Native or Expo change for platform APIs, navigation, and lifecycle safety. Use for a React Native code review. Do not use for a web-only React bug or an Expo upgrade nobody asked for."
---

# React Native Code Review Skill for Gemini CLI

Gemini CLI skill `react-native-code-review` for React Native. Activation calls `activate_skill` and waits for consent. Keep this copy under `.gemini/skills`.

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
