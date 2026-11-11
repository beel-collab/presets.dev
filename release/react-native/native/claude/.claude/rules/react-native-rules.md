---
paths:
  - "**/*.tsx"
  - "app.json"
  - "app.config.ts"
---

# React Native Claude Code Rules: Expo, Navigation and Native Lifecycle

Path-scoped Claude Code rule for React Native. It loads when a matching file is read. It does not replace `CLAUDE.md`. Use `react-native-code-review` for a review.

## Updated for React Native 0.88.1, Nov 2026

React Native 0.88.1 is the npm `latest` release checked on 11 November 2026. Expo's current SDK that day was 58. Do not change the Expo SDK or the React Native version unless the task asks, and do not mix an SDK with a React Native version the SDK does not support. Web-only DOM APIs, including React 19.3 `browser()` and View Transitions, are not available here.

## Project shape

Read `app.json` or `app.config`, the navigation library, and whether the app is Expo or a bare workflow. Follow that. Screens live where the navigator already registers them. Platform files (`ios`, `android`, `.native`) stay the split the repo uses.

A new native module or config plugin is a product decision. Do not add one to solve a JavaScript problem.

## Components and state

The React rules still apply: derive values during render, clean up effects, and do not store props in state. A screen unmounts when the user navigates away. Cancel the request and the subscription in the cleanup.

Do not touch a navigation ref or a screen's state after the screen has blurred unless the API you call is documented to allow it. Check `mounted` or the navigation focus hook the project already uses before you set state after `await`.

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
