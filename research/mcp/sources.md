# MCP sources

Checked 12 November 2026.

- Spec changelog: https://modelcontextprotocol.io/specification/2026-07-28/changelog
  The 2026-07-28 revision removes `initialize` / `notifications/initialized` and the `Mcp-Session-Id` header. Requests carry protocol version and capabilities in `_meta`. Servers implement `server/discover`. Subscriptions use `subscriptions/listen`. Results require `resultType`. Multi round-trip requests use `input_required` instead of server-initiated elicitation, sampling, and roots calls.
- TypeScript SDK v2 upgrade: https://ts.sdk.modelcontextprotocol.io/v2/migration/upgrade-to-v2
  `@modelcontextprotocol/sdk` 1.32 serves 2025-era clients. Serving 2026-07-28 uses `serveStdio(() => createServer())` or `createMcpHandler(() => createServer())` from the v2 packages.
- npm `latest` on 12 November 2026: `@modelcontextprotocol/sdk` 1.32.2, `@modelcontextprotocol/server` 2.4.0, `@modelcontextprotocol/client` 2.4.0, `@modelcontextprotocol/node` 2.1.2.
