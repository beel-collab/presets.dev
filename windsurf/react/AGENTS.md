---
title: "React Components"
description: "Place in your components/ directory. Cascade auto-applies these conventions whenever it reads or edits files in that folder."
tags: ["react"]
author:
  name: Community
  url: 'https://github.com/beel-collab/presets.dev'
---

# React Component Conventions

## Component Structure
- Functional components only — no class components
- One component per file, filename matches component name: `UserCard.tsx`
- Named exports only — no default exports
- Props interface defined directly above the component

```tsx
interface UserCardProps {
  user: User;
  onSelect?: (id: string) => void;
}

export function UserCard({ user, onSelect }: UserCardProps) {
  ...
}
```

## File Organization
Each component folder should contain:
- `ComponentName.tsx` — the component
- `ComponentName.test.tsx` — tests
- `ComponentName.module.css` — styles (if needed)
- `index.ts` — re-export: `export { ComponentName } from "./ComponentName"`

## Hooks
- Extract stateful logic into custom hooks: `useCart`, `useAuth`
- Hook files named `useHookName.ts`, live alongside the component that owns them
- Hooks shared across components go in `src/hooks/`

## Styling
- CSS Modules for component-scoped styles
- No inline styles except for dynamic values (e.g., widths from JS)
- Tailwind utility classes are fine for layout; CSS Modules for component-specific design

## State
- Keep state as local as possible — lift only when two sibling components need it
- Server state (API data) managed with TanStack Query — not `useState`
- No prop drilling beyond 2 levels — use context or a store

## Performance
- Wrap components in `React.memo` only after profiling shows unnecessary re-renders
- Avoid creating functions/objects in JSX props — define outside or use `useCallback`
- Lazy-load heavy components: `const Modal = lazy(() => import("./Modal"))`
