---
id: "gemini-cli-react-performance-audit"
slug: "gemini-cli/react/react-performance-audit/SKILL"
title: "React Performance Audit Skill for Gemini CLI"
description: "Gemini CLI skill for a React performance audit. Use when you want that performance audit on a React change. Do not use it for a different stack."
type: "skill"
tools:
  - "gemini-cli"
stack: "react"
tags:
  - "react"
  - "typescript"
  - "hooks"
  - "components"
  - "performance"
author:
  name: "presets.dev"
  github: "beel-collab"
license: "MIT"
origin: "original"
version: "1.0.0"
tested_with:
  - "Gemini CLI docs 2026-11-11; CLI not run"
created: "2026-11-11"
updated: "2026-11-11"
libs:
  - "react@19.3.1"
updated_for: "React 19.3.1, Nov 2026"
---

# React Performance Audit Skill for Gemini CLI

## Install

Install the native export at `.gemini/skills/react-performance-audit/SKILL.md`.
Copy that export, not this catalog file. Catalog fields such as `tools` and `author` are for presets.dev.
Install one tool's skill for a checkout. Do not drop every tool's copy into `.agents/skills` under the same name.

<!-- native:start -->

# React Performance Audit Skill for Gemini CLI

Gemini CLI skill `react-performance-audit` for React. Activation calls `activate_skill` and waits for consent. Keep this copy under `.gemini/skills`.

## When to run

Run this audit when a React screen is slow, janky, or re-rendering more than the interaction needs. Also run it for "why is this page heavy" or "check the render cost".

## When to leave it

Stop for a non-React repository, a copy change, or a request that only asks for a new color. Do not upgrade React as part of the audit.

## Steps

1. Read the installed `react` version. Note 19 versus 18. Do not recommend 19.3 APIs on 18.
2. Find the interaction the user says is slow. If they did not name one, ask. Do not audit the whole repository blindly.
3. Look for effects that set state on every render, missing cleanups, and derived state stored in `useState`. Each one is a finding when it causes an extra render or a loop.
4. Look for client-only work that could stay out of the first render: a heavy chart, a markdown parser, a date library imported by a leaf that every page loads. Record the import path.
5. Look for lists rendered in full when the row count is unbounded, and for context providers whose value is a fresh object every render and whose consumers are expensive.
6. Check hydration. A `window` or `Date.now()` read during render is a finding. A suppressed mismatch warning is a finding.
7. If the project has a profiler script or a bundle report, run it when the user asked for measurements. Otherwise say what you would measure and write `not run`.

## Output

Each finding has severity, file, line, the render or network cost you can point at, and a smaller fix. End with the React version and `no file edits` unless the user asked for a change.

## Stop

Stop when the project is not React, or when the user asks you to rewrite the UI without a measured hotspot.
