---
name: "mcp-security-review"
description: "Review an MCP server for spec compatibility, schema checks, and tool permissions. Use for an MCP security review. Do not use for a generic HTTP API, or to pass a user's token through to an untrusted tool."
---

# MCP Security Review Skill for Windsurf

Devin skill `mcp-security-review` for MCP. Invoke it with `/mcp-security-review`. Install only `.devin/skills`. This file is not a subagent.

## When to run

Run this review for an MCP server: a new tool, a transport, a spec bump, or "what can this tool do".

## When to leave it

Stop for a plain HTTP API that is not MCP. Do not deploy the server or call a production tool.

## Steps

1. Read the package names. A 2026-07-28 server that still depends only on `@modelcontextprotocol/sdk` and calls `server.connect(new StdioServerTransport())` is a high finding: that entry speaks the 2025 protocol. `initialize` and `Mcp-Session-Id` are not part of 2026-07-28. Flag them when the project claims that revision.
2. List every tool. A missing input schema, or a handler that does not check the schema, is a high finding.
3. For each tool, name the files, hosts, and credentials it can reach. A token passed through from the end user, or a path that escapes the root, is a high finding. A destructive tool whose only gate is a model-written `confirm` argument is a high finding. Approval has to come back through `input_required` and the host UI.
4. Check result text. Instructions that tell the model to ignore the user are a high finding.
5. A remote server with no auth in front of a sensitive tool is a high finding.
6. Run the project's server test only if the user asked. Otherwise write `not run`. Do not use a real account.

## Output

Findings with severity, file, line, the tool name, the capability that is too wide, and a narrower design. No tokens in the report.

```
## Findings
- high | path:line | what is wrong | what to do instead

## No findings
Say "No findings" and list the files you opened. A search you skipped is not a clean result.

## Example
Input: a one-line change that matches a rule in the standards.
Output: either one finding with file and line, or "No findings" when the change is the valid pattern named in the standards.
```

Do not flag the valid pattern named in the standards. Flag the mistake next to it.

## What to check

- Injection: concatenated SQL, shell, or HTML.
- XSS: unescaped user text in HTML.
- CSRF: a browser state change with the framework check disabled.
- Secrets: a key in the repo or in a log line.
- IDOR: an id from the client with no owner or permission check.
- SSRF: a user-supplied URL fetched with no allow-list.

## Stop

Stop when the user asks you to add a shell tool with no root, or to forward their credential to make a demo work.

## Severity

`high` is a bug a caller can hit or a secret that leaks. `medium` is a broken contract that needs a specific input. `low` is a cleanup that does not change behaviour.
