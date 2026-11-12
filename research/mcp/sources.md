# MCP sources

Fetched 12 November 2026.

- Spec changelog: https://modelcontextprotocol.io/specification/2026-07-28/changelog
  The 2026-07-28 revision removes `initialize` / `notifications/initialized` and the `Mcp-Session-Id` header. Requests carry protocol version and capabilities in `_meta`. Servers implement `server/discover`. Subscriptions use `subscriptions/listen`. Results require `resultType`. Multi-round-trip requests use `input_required` instead of server-initiated elicitation, sampling, and roots calls. A model-written `confirm` argument is not that host UI.
- TypeScript SDK v2 stdio: https://ts.sdk.modelcontextprotocol.io/v2/serving/stdio.html
  Import `McpServer` from `@modelcontextprotocol/server` and `serveStdio` from `@modelcontextprotocol/server/stdio`. The factory builds one server per call. `serveStdio` is not a root export. `@modelcontextprotocol/server` 2.4.0 confirms this: the package root exports `McpServer` and `createMcpHandler`, and `./stdio` exports `serveStdio` and `StdioServerTransport`.
- Tools: https://ts.sdk.modelcontextprotocol.io/v2/servers/tools.html
  `registerTool` takes a Zod `inputSchema` (`import * as z from "zod/v4"`). The SDK infers the handler arguments from that schema. A manual `{ id: string }` annotation is not that signature.
- TypeScript SDK v2 upgrade: https://ts.sdk.modelcontextprotocol.io/v2/migration/upgrade-to-v2
  The guide rewrites `.tool()` to `registerTool`. `@modelcontextprotocol/node` is for a handler that receives Node `IncomingMessage`, not for `node:http` `createServer`. `server.connect(new StdioServerTransport())` from `@modelcontextprotocol/sdk` 1.32 does not speak 2026-07-28.
- Registry, read 12 November 2026: https://registry.npmjs.org/@modelcontextprotocol/sdk `latest` 1.32.2, https://registry.npmjs.org/@modelcontextprotocol/server `latest` 2.4.0, https://registry.npmjs.org/@modelcontextprotocol/client `latest` 2.4.0, https://registry.npmjs.org/@modelcontextprotocol/node `latest` 2.1.2.
