# MCP sources

Fetched 12 November 2026.

- Spec changelog: https://modelcontextprotocol.io/specification/2026-07-28/changelog
  The 2026-07-28 revision removes `initialize` / `notifications/initialized` and the `Mcp-Session-Id` header. Requests carry protocol version and capabilities in `_meta`. Servers implement `server/discover`. Subscriptions use `subscriptions/listen`. Results require `resultType`. Multi-round-trip requests use `input_required` instead of server-initiated elicitation, sampling, and roots calls. A model-written `confirm` argument is not that host UI.
- TypeScript SDK v2 upgrade: https://ts.sdk.modelcontextprotocol.io/v2/migration/upgrade-to-v2
  The guide rewrites `.tool()` to `registerTool` and shows `serveStdio(() => createServer())` from `@modelcontextprotocol/server`. `StdioServerTransport` is imported from `@modelcontextprotocol/server/stdio`. `@modelcontextprotocol/node` is for a handler that receives Node `IncomingMessage`, not for `node:http` `createServer`.
  Serving 2026-07-28 uses `serveStdio(() => createServer())` or `createMcpHandler(() => createServer())`. `server.connect(new StdioServerTransport())` from `@modelcontextprotocol/sdk` 1.32 does not speak this revision.
- Registry, read 12 November 2026: https://registry.npmjs.org/@modelcontextprotocol/sdk `latest` 1.32.2, https://registry.npmjs.org/@modelcontextprotocol/server `latest` 2.4.0, https://registry.npmjs.org/@modelcontextprotocol/client `latest` 2.4.0, https://registry.npmjs.org/@modelcontextprotocol/node `latest` 2.1.2.
