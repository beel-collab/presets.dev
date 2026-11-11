---
name: "mcp-security-review"
description: "Review an MCP server for spec compatibility, schema checks, and tool permissions. Use for an MCP security review. Do not use for a generic HTTP API, or to pass a user's token through to an untrusted tool."
---

# MCP Security Review Skill for Copilot

Copilot skill `mcp-security-review` for MCP. The description decides when Copilot loads it. Keep this copy under `.github/skills`.

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
