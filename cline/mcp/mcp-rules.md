---
id: "cline-mcp-rules"
slug: "cline/mcp/mcp-rules"
title: "MCP Cline Rules: Tools, Schemas and Permissions"
description: "Cline rules for MCP: Tools, Schemas and Permissions. Structure, data, errors, security, performance, and tests. MCP spec 2026-07-28, SDK 1.32.2, Nov 2026."
type: "rule"
tools:
  - "cline"
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
  - "Cline docs 2026-11-11; app not executed"
created: "2026-11-11"
updated: "2026-11-11"
libs:
  - "@modelcontextprotocol/sdk@1.32.2"
updated_for: "MCP spec 2026-07-28, SDK 1.32.2, Nov 2026"
---

# MCP Cline Rules: Tools, Schemas and Permissions

## Install

Install the native export at `.clinerules/mcp-rules.md` (do not also copy it to `.cline/rules/`).
Copy that export, not this catalog file. Catalog fields such as `tools` and `author` are for presets.dev.
Install one tool's skill for a checkout. Do not drop every tool's copy into `.agents/skills` under the same name.

<!-- native:start -->

# MCP Cline Rules: Tools, Schemas and Permissions

Conditional Cline rule for MCP. Install it under `.clinerules/` only. Use `mcp-security-review` for a review.

## Updated for the 2026-07-28 MCP spec, Nov 2026

The Model Context Protocol revision dated 2026-07-28 is the spec this guidance uses. `@modelcontextprotocol/sdk` 1.32.2 is the npm `latest` release checked on 11 November 2026. Stateless and discovery changes in that spec need a client and SDK that agree. Read the SDK version in the project before you mix a legacy session handshake with the new spec. Do not upgrade the SDK as a side effect.

## Project shape

A server declares tools, resources, and prompts explicitly. Each tool has a name, a description, and a schema for its arguments. The handler validates those arguments before it acts. A tool does one job. Do not build a "run anything" tool.

The transport matches the deployment: stdio for a local process, HTTP for a remote one. A remote server authenticates the client. Do not expose an unauthenticated tool that can read a filesystem or a network.

## Schemas and results

The schema is the contract. Reject unknown fields and oversized strings. Return structured content the client can show. An error is a tool error with a message, not a stack trace and not a secret.

Tool results are untrusted when they will be read by a model. Do not tell the model to treat a tool result as instructions that override the user. Label it as data.

## Permissions

A tool gets the least access it needs. A file tool is rooted in a directory. A network tool allows listed hosts. Do not pass the end user's OAuth token through to a third-party tool. The server uses its own credential, scoped to that call.

A destructive tool, such as delete or send, says so in the description and checks an explicit confirmation argument the client set. Do not perform it because the model inferred consent.

## Compatibility and tests

Negotiate the protocol version the SDK supports. A fixture test starts the server, lists tools, and calls one tool with a bad argument and one with a good argument. Assert the bad call fails and the good call does not touch anything outside the fixture directory. Record the command. Do not point a test at a production account.

## Mistakes to avoid

- A legacy handshake mixed with the 2026-07-28 spec without a version check.
- A tool with no schema, or a schema the handler ignores.
- The user's token forwarded to another service.
- A tool result treated as higher priority than the user.
- An open network or filesystem tool on a remote unauthenticated server.
