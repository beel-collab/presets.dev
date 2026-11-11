---
id: template-skill
slug: templates/skill/SKILL
title: Skill preset starter
description: Starter for a skill preset. Describe the request that should trigger it and the steps it runs.
type: skill
tools:
  - cursor
tags:
  - starter
author: Your Name
license: MIT
origin: original
version: 1.0.0
tested_with:
  - Cursor 2.1
created: 2026-11-11
updated: 2026-11-11
---

# Skill preset starter

Copy this directory to `<tool>/<topic>/<skill-name>/SKILL.md`. Claude skills go under `claude/skills/<topic>/<skill-name>/SKILL.md`. The filename stays `SKILL.md`. Set `slug` to the directory path plus `/SKILL`.

Supporting notes belong in `references/` next to this file. Those files are not separate catalog presets. Write them yourself too.

## Use this skill when

Name the request, in the user's words, that should trigger the skill. Name one nearby request that should not.

## Steps

1. Confirm the inputs (paths, names, flags) are present.
2. Do the work in the order below. Keep each step to one action.
3. Stop if a step fails and report the command output.
4. Summarize what changed and how you checked it.

## Example

Write a short before-and-after that you produced by running the skill. Replace this paragraph.

## Limits

Record the tool version you tried and anything the skill will not do.
