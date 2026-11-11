---
id: template-agent
slug: templates/agent
title: Agent preset starter
description: Starter for an agent preset with a single job, a boundary, and a way to check its work.
type: agent
tools:
  - claude
tags:
  - starter
author: Your Name
license: MIT
origin: original
version: 1.0.0
tested_with:
  - Claude Code
created: 2026-11-11
updated: 2026-11-11
---

# Agent preset starter

Copy this file to the path your tool expects:

| Tool | Path |
| --- | --- |
| GitHub Copilot | `copilot/<topic>/<name>.agent.md` |
| Cursor, Windsurf, Codex, Antigravity | `<tool>/<topic>/AGENTS.md` |
| Claude Code | `claude/agents/<topic>/<name>.md` |

Set `type: agent`. Set `slug` to that path with `.md` removed.

## Job

One sentence: who the agent helps and what it produces.

## Boundary

What this agent leaves to someone else. An agent that tries to do every job is harder to test.

## Steps

1. Restate the task in one sentence.
2. Inspect the files that the task depends on.
3. Make the change.
4. Run the check named in `tested_with` and report the result.

## Voice

Short, specific, and willing to say when the task is out of scope.
