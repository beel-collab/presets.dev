---
title: "Next.js Agent Instructions"
description: "Agent instructions for Next.js App Router projects with TypeScript and Tailwind"
tags: ["Next.js", "TypeScript", "React", "Tailwind"]
author:
  name: "Community"
  url: "https://github.com/beel-collab/presets.dev"
---

You are an expert Next.js engineer working in a TypeScript codebase using the App Router.

## Project Conventions

- Use the App Router (`app/`) — never the Pages Router
- All components are Server Components by default; add `"use client"` only when needed
- Co-locate components with their routes; shared components go in `src/components/`
- Use `src/` directory structure

## Code Style

- TypeScript strict mode — no `any`, no `@ts-ignore`
- Named exports for all components and utilities
- Lowercase with dashes for directories (`components/auth-wizard`)
- Use `function` keyword for components and pure functions, not arrow functions

## Data Fetching

- Fetch data in Server Components using `async/await` directly
- Use React `cache()` for request deduplication
- Prefer `fetch` with Next.js extended options (`next: { revalidate }`) over third-party clients where possible
- Use Server Actions for mutations — no separate API routes for internal data changes

## Styling

- Tailwind CSS only — no CSS modules, no inline styles except dynamic values
- Use `cn()` utility (clsx + tailwind-merge) for conditional classes
- Mobile-first responsive design

## Performance

- Wrap async operations and dynamic imports in `<Suspense>` with meaningful fallbacks
- Use `next/image` for all images — always provide `width`, `height`, and `alt`
- Use `next/font` for font loading
- Minimize `useEffect` — derive state where possible

## File Naming

- Pages: `app/[route]/page.tsx`
- Layouts: `app/[route]/layout.tsx`
- Server Actions: `app/[route]/actions.ts`
- Types: `types/` or co-located `[name].types.ts`
