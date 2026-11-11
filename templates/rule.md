---
id: template-rule
slug: templates/rule
title: Rule preset starter
description: Starter for a rule preset. Say which language or framework it covers and what the assistant should change.
type: rule
tools:
  - cursor
tags:
  - starter
author:
  name: Your Name
  github: your-name
license: MIT
origin: original
version: 1.0.0
tested_with:
  - Cursor 2.1
created: 2026-11-11
updated: 2026-11-11
---

# Rule preset starter

Copy this file to `<tool>/<topic>/<name>.md` (Cursor and Windsurf rules) or `<tool>/<topic>/<name>.mdc` (scoped Cursor rules). Then replace `id`, `slug`, `author`, `tools`, and the body. The `slug` is the path with `.md` or `.mdc` removed.

For a scoped Cursor rule, add `globs` and `alwaysApply` to the frontmatter.

## When this applies

Name the files or the task this rule is for.

## Write this way

- State the behavior you want in a sentence the assistant can follow.
- Give one small example you wrote yourself.
- Name the case the assistant should leave alone.

## Avoid

- Pasted excerpts from framework docs or from another rules file.
- A long list of preferences that you have not tried in the tool under `tested_with`.
