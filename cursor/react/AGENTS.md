---
title: "React Agent Instructions"
description: "Agent instructions for React projects with TypeScript, hooks, and modern patterns"
tags: ["React", "TypeScript", "Hooks"]
author:
  name: "Community"
  url: "https://github.com/beel-collab/presets.dev"
---

You are an expert React engineer building modern component-based UIs with TypeScript.

## Component Principles

- Functional components only — no class components
- One component per file; filename matches component name
- Export components as named exports
- Keep components small and focused — split when a component exceeds ~150 lines

## TypeScript

- Define prop types with interfaces, not `type` aliases
- Never use `React.FC` — type props directly: `function Button({ label }: ButtonProps)`
- Prefer `unknown` over `any`; use type guards to narrow

## Hooks

- Custom hooks live in `hooks/` and are prefixed with `use`
- Never call hooks conditionally
- Derive state from existing state/props before reaching for `useState`
- Use `useReducer` for complex state with multiple sub-values
- Memoize expensive computations with `useMemo`; memoize callbacks passed to children with `useCallback`

## State Management

- Local state with `useState`/`useReducer` first
- Context for cross-cutting concerns (theme, auth) — not for frequently-updating values
- Use a dedicated library (Zustand, Jotai) for global application state

## Side Effects

- Keep `useEffect` minimal — don't use it for derived state or event handlers
- Always clean up subscriptions, timers, and listeners in the return function
- Fetch data with React Query or SWR — not raw `useEffect`

## Styling

- CSS Modules or Tailwind — keep styles co-located with components
- No inline styles except truly dynamic values (e.g. `style={{ width: value }}`)

## Testing

- Test behaviour, not implementation
- Use React Testing Library — no Enzyme
- Mock at the network level (MSW), not at the module level
