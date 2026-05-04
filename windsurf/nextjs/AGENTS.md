---
title: "Next.js Project"
description: "Place at project root. Always-on conventions for Next.js App Router projects with TypeScript and Tailwind."
tags: ["nextjs"]
author:
  name: Community
  url: 'https://github.com/beel-collab/presets.dev'
---

# Next.js Project Conventions

## Stack
- Next.js 14+ with App Router
- TypeScript strict mode
- Tailwind CSS for styling
- Prisma for database access
- next-auth for authentication

## Routing & Pages
- Pages in `app/` using App Router file conventions (`page.tsx`, `layout.tsx`, `loading.tsx`, `error.tsx`)
- Route groups with `(group-name)/` for organization without URL segments
- Dynamic routes: `[id]` for single param, `[...slug]` for catch-all
- Parallel routes `@slot` only when genuinely needed — prefer simpler patterns

## Server vs Client Components
- Default to React Server Components (RSC) — no `"use client"` unless needed
- Add `"use client"` only for: event handlers, browser APIs, hooks, interactive state
- Never import server-only modules (db, fs) in client components
- Shared types between server/client are fine — shared logic must be split

## Data Fetching
- Fetch directly in Server Components — no useEffect for initial data
- Use `cache()` to deduplicate requests within a render
- Mutations via Server Actions (`"use server"`) — not API routes for form submissions
- API routes (`app/api/`) only for external consumers or webhooks

## File Conventions
```
app/
  (auth)/           # Auth route group
  api/              # API routes
  [locale]/         # i18n if needed
components/
  ui/               # Primitive components
server/             # Server-only: db.ts, auth.ts
lib/                # Shared utilities (safe for both server/client)
```

## Performance
- Images: always use `next/image` — never `<img>`
- Fonts: `next/font` to avoid layout shift
- Links: `next/link` for all internal navigation
- Dynamic imports for heavy client components: `dynamic(() => import("./HeavyChart"))`
