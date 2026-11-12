---
id: "cline-react-rules"
slug: "cline/react/react-rules"
title: "React Cline Rules: Components, State and Effects"
description: "Cline rules for React: Components, State and Effects. Structure, data, errors, security, performance, and tests. React 19.3.1, Nov 2026."
type: "rule"
tools:
  - "cline"
stack: "react"
tags:
  - "react"
  - "typescript"
  - "hooks"
  - "components"
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
  - "react@19.3.1"
updated_for: "React 19.3.1, Nov 2026"
---

# React Cline Rules: Components, State and Effects

## Install

Install the native export at `.clinerules/react-rules.md` (do not also copy it to `.cline/rules/`).
Copy that export, not this catalog file. Catalog fields such as `tools` and `author` are for presets.dev.
Install one tool's skill for a checkout. Do not drop every tool's copy into `.agents/skills` under the same name.

<!-- native:start -->

# React Cline Rules: Components, State and Effects

Conditional Cline rule for React. Install it under `.clinerules/` only.

## Updated for React 19.3.1, Nov 2026

## Project shape

Build the tree from function components. One component owns one job. Put shared UI in the folder the project already uses. Colocate a component's test next to it when that is the local pattern.

Props are the input. State is what this component owns. Derived values are computed while rendering. A parent owns state that two children must share.

## State and rendering

Set state in response to an event or a completed request. Compute `fullName` from `first` and `last` during render. An effect that copies props into state goes stale and renders twice.

Use a functional update when the next state depends on the previous one. Include every reactive value a hook callback reads, or restructure so the callback does not close over a changing value.

Lists need a stable id as `key`. Index keys break when the list is reordered, filtered, or inserted into.

## Effects

Effects synchronize with an external system: a subscription, a timer, a widget outside React. Return a cleanup that cancels the subscription or the timer. Do not fetch in an effect when the framework already loads data in a server component or a router loader. If the project does fetch in effects, abort on cleanup and ignore a response that arrives after unmount.

Strict Mode runs setup and cleanup an extra time in development. A cleanup that is missing will show up there. Do not "fix" that by disabling Strict Mode.

## React 19 patterns

Actions can submit a form and expose pending state. Keep the action's input validated at the boundary that talks to the server. A client action is not authorization.

Use a View Transition only when the project is on 19.3 or newer and the screen is a browser. Wrap the update that should animate. Provide a reduced-motion path. Fragment refs and `browser()` are the same kind of gate: check the version, and do not import them into a Native tree.

`ref` is a normal prop on function components in React 19. Do not add `forwardRef` to new components on a confirmed 19 codebase. Leave existing `forwardRef` calls alone unless you are already editing that component.

## Errors and accessibility

Throw from a render only for a broken invariant. Catch it with an error boundary the project already has. A form shows field errors next to the fields.

Every control has a label. Buttons are buttons, not clickable divs. Images that convey meaning have text alternatives. Do not silence a hydration mismatch with a suppress flag. Find the value that differed between server and client, usually a clock, a random id, or `window`.

## Security and performance

Do not pass unsanitized HTML to `dangerouslySetInnerHTML`. Escape by default. Do not store tokens in state that you then render into the DOM.

Memoize a child when a profile shows it re-rendering expensively, not by habit. Lift a subscription so one listener serves the tree. Virtualize a list that renders hundreds of rows. Code-split a heavy editor or chart behind the interaction that needs it.

## Tests

Test what the user sees. Query by role or label. Fire events through the testing library the repo uses. Assert the visible result, not a state variable. Cover the error text and the empty state when you change them.

## Mistakes to avoid

- An effect that copies props into state or derives a value the render could compute.
- A stale handler that reads state from the render where it was created.
- A suppressed hydration warning.
- A 19.3 DOM API used in React Native or in a React 18 app.
- `memo` and new context providers added without a measurement.

## What changed in this major

React 19.3 stabilizes View Transitions, Fragment refs, and `browser()`. Those are DOM APIs. `ref` is a normal prop, so new components skip `forwardRef`.

## Deprecated APIs to never generate

Do not generate `forwardRef` on a React 19 function component, or `componentWillMount`.

## Commands

Run the repo's test script and, when asked, the React profiler. Do not upgrade React.

## Example

```tsx
const fullName = first + " " + last
```
Compute `fullName` during render. Do not copy `first` into state from an effect.
