---
id: "claude-mcp-security-review"
slug: "claude/skills/mcp/mcp-security-review/SKILL"
title: "MCP Security Review Skill for Claude Code"
description: "Claude Code skill for a MCP security review. Use when you want that security review on a MCP change. Do not use it for a different stack."
type: "skill"
tools:
  - "claude"
stack: "mcp"
tags:
  - "mcp"
  - "tools"
  - "security"
author:
  name: "presets.dev"
  github: "beel-collab"
license: "MIT"
origin: "original"
version: "1.0.0"
tested_with:
  - "Claude Code docs 2026-11-11; CLI not run"
created: "2026-11-11"
updated: "2026-11-11"
libs:
  - "@modelcontextprotocol/sdk@1.32.2"
updated_for: "MCP spec 2026-07-28, SDK 1.32.2, Nov 2026"
---

# MCP Security Review Skill for Claude Code

## Install

Install the native export at `.claude/skills/mcp-security-review/SKILL.md`.
Copy that export, not this catalog file. Catalog fields such as `tools` and `author` are for presets.dev.
Install one tool's skill for a checkout. Do not drop every tool's copy into `.agents/skills` under the same name.

<!-- native:start -->

# MCP Security Review Skill for Claude Code

Claude Code skill `mcp-security-review` for MCP. The command is `/mcp-security-review`. Leave the normal permission prompts on.

## When to run

Run this review for an MCP server: a new tool, a transport, a spec bump, or "what can this tool do".

## When to leave it

Stop for a plain HTTP API that is not MCP. Do not deploy the server or call a production tool.

## Steps

1. Read the SDK version and any pinned protocol revision. A mix of legacy session fields and the 2026-07-28 handshake, with no negotiation, is a high finding.
2. List every tool. A missing input schema, or a handler that does not check the schema, is a high finding.
3. For each tool, name the files, hosts, and credentials it can reach. A token passed through from the end user, or a path that escapes the root, is a high finding.
4. Check result text. Instructions that tell the model to ignore the user are a high finding.
5. A remote server with no auth in front of a sensitive tool is a high finding.
6. Run the project's server test only if the user asked. Otherwise write `not run`. Do not use a real account.

## Output

Findings with severity, file, line, the tool name, the capability that is too wide, and a narrower design. No tokens in the report.

## Stop

Stop when the user asks you to add a shell tool with no root, or to forward their credential to make a demo work.
