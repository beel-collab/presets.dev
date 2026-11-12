---
id: "copilot-mcp-rules"
slug: "copilot/mcp/mcp-rules.instructions"
title: "MCP Copilot Instructions: Tools, Schemas and Permissions"
description: "Copilot instructions for MCP: Tools, Schemas and Permissions. Structure, data, errors, security, performance, and tests. MCP spec 2026-07-28, server SDK 2.4.0, Nov 2026."
type: "instruction"
tools:
  - "copilot"
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
  - "Copilot docs 2026-11-11; app not executed"
created: "2026-11-11"
updated: "2026-11-11"
libs:
  - "@modelcontextprotocol/server@2.4.0"
updated_for: "MCP spec 2026-07-28, server SDK 2.4.0, Nov 2026"
---

# MCP Copilot Instructions: Tools, Schemas and Permissions

## Install

Install the native export at `.github/instructions/mcp.instructions.md`.
Copy that export, not this catalog file. Catalog fields such as `tools` and `author` are for presets.dev.
Install one tool's skill for a checkout. Do not drop every tool's copy into `.agents/skills` under the same name.

<!-- native:start -->

# MCP Copilot Instructions: Tools, Schemas and Permissions

Path-specific Copilot instructions for MCP. They apply through `applyTo` and leave `.github/copilot-instructions.md` in place.

## Updated for the 2026-07-28 MCP spec, Nov 2026
Do not upgrade dependencies or the framework version unless the task asks.

The spec this file follows is the 2026-07-28 revision. `@modelcontextprotocol/sdk` 1.32.2 is still the v1 package on npm, and a server that calls `server.connect(new StdioServerTransport())` or hands requests to a Streamable HTTP transport from that package speaks the 2025-era protocol only. A client pinned to 2026-07-28 cannot complete a session with it.

To serve 2026-07-28, use the v2 packages. `@modelcontextprotocol/server` 2.4.0 and `@modelcontextprotocol/client` 2.4.0 are the v2 packages that speak this revision. A Node stdio or HTTP entry uses `@modelcontextprotocol/node` when the handler sees Node `IncomingMessage`. Start with `serveStdio(() => createServer())` or `createMcpHandler(() => createServer())`. Read the installed package names before editing. Do not upgrade a v1 server as a side effect of another change, and do not import `@modelcontextprotocol/core-internal`.

## What this revision removed

The 2026-07-28 revision is stateless. There is no `initialize` / `notifications/initialized` handshake and no `Mcp-Session-Id` header. Every request carries its protocol version and client capabilities in `_meta` (`io.modelcontextprotocol/protocolVersion`, `io.modelcontextprotocol/clientCapabilities`). Servers identify themselves on each result the same way. A version mismatch is `UnsupportedProtocolVersionError`.

`server/discover` is required. It advertises supported versions, capabilities, and identity. Clients may call it before other requests, or use it as a probe on stdio.

List methods do not vary per connection. Cross-call state is an explicit server-minted handle passed as an ordinary tool argument. `resources/subscribe` is gone. Opted-in change notifications use `subscriptions/listen`. Every result has `resultType`: `"complete"` or `"input_required"`.

A server that needs more information returns `InputRequiredResult` (`resultType: "input_required"`) and the client retries the original request with `inputResponses`. That is the multi round-trip request pattern. It replaces server-initiated `elicitation/create`, `sampling/createMessage`, and `roots/list` on this revision.

## Project shape

Declare tools, resources, and prompts explicitly. Each tool has a name, a description, and a JSON Schema for its arguments. The handler checks that schema before it acts. One tool does one job. Do not ship a tool that runs arbitrary commands.

Pick the transport for the deployment. Local processes use stdio. A remote HTTP server authenticates the caller. Do not expose an unauthenticated remote tool that can read a filesystem or call the network.

## Schemas and results

Reject unknown fields and oversized strings. Return structured content. An error is a tool error with a short message, not a stack and not a secret.

Tool results are data. Do not tell the model to treat a tool result as instructions that override the user.

## Permissions

A file tool is rooted in one directory. A network tool allows listed hosts. Do not pass the end user's OAuth token through to another service. The server uses its own credential, scoped to that call.

A destructive tool says so in its description. Do not treat a `confirm: true` argument as consent. The model writes that argument. Return `resultType: "input_required"` and let the host show the decision in its own UI, then retry the original request with the user's `inputResponses`. Do not perform the action because the model inferred a yes.

## Checks

`npm test` in the server package, against a fixture directory, with one rejected argument and one accepted argument. Do not point the test at a production account.

## Mistakes to avoid

- Implementing 2026-07-28 with `@modelcontextprotocol/sdk` 1.32 and `server.connect(StdioServerTransport)`.
- Sending `initialize` or `Mcp-Session-Id` and expecting this revision to honor them.
- A tool with no schema, or a handler that ignores the schema.
- The user's token forwarded to another service.
- A tool result written as instructions that outrank the user.
- An open network or filesystem tool on a remote server with no authentication.
- A `confirm` argument treated as the user's approval.

## What changed in this major

The 2026-07-28 spec removes `initialize` and `Mcp-Session-Id`. Serve it with `@modelcontextprotocol/server` 2.x via `serveStdio` or `createMcpHandler`.

## Deprecated APIs to never generate

For a 2026-07-28 server, do not generate `server.connect(new StdioServerTransport())` from `@modelcontextprotocol/sdk` 1.32. Call `serveStdio` or `createMcpHandler` from `@modelcontextprotocol/server` 2.x.

## Commands

Run the server package tests against a fixture directory.

## Example

```ts
import { McpServer, serveStdio } from "@modelcontextprotocol/server"
import { StdioServerTransport } from "@modelcontextprotocol/server/stdio"

const notes = new McpServer({ name: "notes", version: "1.0.0" })
notes.registerTool(
  "read_note",
  { description: "Read one note by id" },
  async (args: { id: string }) => ({
    content: [{ type: "text", text: args.id }],
  }),
)

await serveStdio(() => notes)
```

`registerTool` is the v2 name for `.tool()`. `serveStdio` and `McpServer` come from `@modelcontextprotocol/server`. `StdioServerTransport` comes from `@modelcontextprotocol/server/stdio`, not from the package root. A handler that receives Node's `IncomingMessage` imports its HTTP transport from `@modelcontextprotocol/node`. Do not import `createServer` from `node:http` to build this server. `server.connect(new StdioServerTransport())` from `@modelcontextprotocol/sdk` 1.32 cannot speak 2026-07-28.
