---
id: template-instruction
slug: templates/instruction
title: Instruction preset starter
description: Starter for an instruction preset that sets how the assistant behaves in a repository.
type: instruction
tools:
  - copilot
tags:
  - starter
author: Your Name
license: MIT
origin: original
version: 1.0.0
tested_with:
  - GitHub Copilot
created: 2026-11-11
updated: 2026-11-11
---

# Instruction preset starter

Copy this file to `copilot/<topic>/<name>.instructions.md`, or to `claude/instructions/<topic>/CLAUDE.md` for Claude Code. Update `slug` so it matches the new path with `.md` removed, and set `tools` to include that directory.

## Repository facts

List the commands, directories, and conventions the assistant needs. Write them from this repository, not from a generic guide.

## How to respond

- Read the files that the task touches before editing them.
- Keep a change limited to the request.
- Show the command you expect a person to run when a check exists.

## Stop and ask

Name the situations where the assistant should ask instead of guessing. Examples: a missing product decision, or a migration that deletes data.
