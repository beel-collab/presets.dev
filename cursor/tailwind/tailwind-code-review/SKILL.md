---
id: "cursor-tailwind-code-review"
slug: "cursor/tailwind/tailwind-code-review/SKILL"
title: "Tailwind CSS Code Review Skill for Cursor"
description: "Cursor skill for a Tailwind CSS code review. Use when you want that code review on a Tailwind CSS change. Do not use it for a different stack."
type: "skill"
tools:
  - "cursor"
stack: "tailwind"
tags:
  - "tailwind"
  - "css"
  - "accessibility"
  - "code-review"
author:
  name: "presets.dev"
  github: "beel-collab"
license: "MIT"
origin: "original"
version: "1.0.0"
tested_with:
  - "Cursor docs 2026-11-11; app not executed"
created: "2026-11-11"
updated: "2026-11-11"
libs:
  - "tailwindcss@4.3.5"
updated_for: "Tailwind CSS 4.3.5, Nov 2026"
---

# Tailwind CSS Code Review Skill for Cursor

## Install

Install the native export at `.cursor/skills/tailwind-code-review/SKILL.md`.
Copy that export, not this catalog file. Catalog fields such as `tools` and `author` are for presets.dev.
Install one tool's skill for a checkout. Do not drop every tool's copy into `.agents/skills` under the same name.

<!-- native:start -->

# Tailwind CSS Code Review Skill for Cursor

Cursor skill `tailwind-code-review` for Tailwind CSS. Run it with `/tailwind-code-review`, or let Agent select it when the request matches. `paths` only limits automatic surfacing.

## When to run

Run this review for a Tailwind change: a new component, a theme edit, or "check the styles". Judge version fit, class detection, and accessibility.

## When to leave it

Stop when the project does not use Tailwind, or when the user asked for a v4 migration and you have not confirmed they want it. A v3 repo stays on v3.

## Steps

1. Read the installed `tailwindcss` major. Note v3 config versus v4 `@theme`. A mix of the two in one diff is a high finding.
2. Search the diff for class names built from variables or concatenated fragments. Each one that is not a complete static string is a finding.
3. Look for conflicting utilities on the same element, and for a one-off color that duplicates a token.
4. Check focus, labels on icon buttons, and error messages that are only a red class. Each gap is a finding.
5. Do not start a browser unless the user asked you to verify a screen. If you do, record the URL and the width.

## Output

Findings with severity, file, line, and the class or token to change. End with the Tailwind major and `no file edits` unless a fix was requested.

## Stop

Stop when the user asks you to upgrade v3 to v4 as part of an unrelated review.
