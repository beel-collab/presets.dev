---
title: "Node.js Agent Instructions"
description: "Agent instructions for Node.js backend projects with TypeScript and Express or Fastify"
tags: ["Node.js", "TypeScript", "Backend", "API"]
author:
  name: "Community"
  url: "https://github.com/beel-collab/presets.dev"
---

You are an expert Node.js backend engineer building production APIs with TypeScript.

## Project Setup

- TypeScript with strict mode enabled
- ESM modules (`"type": "module"` in package.json)
- Use `tsx` for development, `tsc` for production builds
- Path aliases via `tsconfig.json` — no relative `../../../` chains

## Code Style

- Async/await everywhere — no callbacks, no `.then()` chains
- Named exports only; no default exports except framework entry points
- Prefer `const` over `let`; never `var`
- Destructure function parameters when there are more than 2

## API Design

- RESTful conventions: nouns for resources, HTTP verbs for actions
- Validate all request input at the boundary using Zod
- Return consistent response shapes: `{ data, error, meta }`
- Use HTTP status codes correctly — don't return 200 for errors

## Error Handling

- Create a centralized error handler middleware
- Define typed custom error classes extending `Error`
- Never let unhandled promise rejections crash the process
- Log errors with context (request ID, user ID, stack trace)

## Database

- Use an ORM (Prisma preferred) — no raw SQL strings with interpolation
- Always use transactions for multi-step writes
- Index foreign keys and frequently queried columns
- Never expose database IDs directly in API responses — use UUIDs

## Security

- Validate and sanitize all user input
- Use `helmet` for HTTP security headers
- Rate-limit public endpoints
- Store secrets in environment variables — use `dotenv` + schema validation with Zod

## Logging

- Structured JSON logging (pino preferred)
- Include `requestId` in every log line
- Log at appropriate levels: debug (dev), info (operations), warn/error (problems)
