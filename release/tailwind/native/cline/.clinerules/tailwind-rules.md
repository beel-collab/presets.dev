---
paths:
  - "**/*.css"
  - "**/*.tsx"
  - "**/*.html"
---

# Tailwind CSS Cline Rules: CSS-First Tokens and Accessible UI

Conditional Cline rule for Tailwind CSS. Install it under `.clinerules/` only. Use `tailwind-code-review` for a review.

## Updated for Tailwind CSS 4.3.5, Nov 2026

Tailwind CSS 4.3.5 is the npm `latest` release checked on 11 November 2026. v4 is CSS-first: theme tokens live in CSS, and the v3 `tailwind.config.js` plugin style is not the v4 setup. If the project is on v3, stay on v3. Do not paste a v3 config into a v4 app, and do not upgrade v3 to v4 unless the task asks.

## Project shape

Read the stylesheet entry and the package version before adding utilities. v4 projects use `@import "tailwindcss"` and `@theme` for tokens. v3 projects use the config file and `@tailwind` directives. Match the one that is installed.

Put design tokens in the theme the project already has. A one-off hex in a class is a last resort. Name the token after the role (`color-surface`), not the raw value.

## Class names

Write class names the compiler can see. `className="px-4 py-2"` is visible. `` className={`px-${n}`} `` is not, and it will not generate CSS. If you need a dynamic value, map a finite set of full class strings, or set a CSS variable.

Do not fight the cascade with a long string of conflicting utilities. Remove the one that lost. Use the project's component or `cva` helper if one exists, instead of copying a 40-class string between files.

## Layout and accessibility

Build responsive layouts with the breakpoints the project uses. Start from the small screen. Do not hide focus outlines. A control that is only an icon needs an accessible name.

Contrast comes from the theme tokens. Do not put gray text on a gray surface because it looks quiet. Respect `motion-reduce` when you add animation. Hit targets stay large enough to tap.

## Errors and states

Style the states the component can be in: empty, loading, error, disabled. Disabled is `disabled:` plus a real `disabled` attribute, not only a faded class. Error text is not color alone. Add the words.

## Performance

The production build scans source files. Do not safelist the entire color palette to make dynamic classes work. Fix the class so it is static. Do not import Tailwind into a file the bundler already processes twice.

## Tests

When you change a visible component, look at it at the project's mobile and desktop widths if a dev server is already how the repo is reviewed. A computed-style check belongs in the project's existing browser test, not a new harness. Record what you actually opened.

## Mistakes to avoid

- A v3 config dropped into a v4 project, or a v4 upgrade nobody requested.
- A class name built by string concatenation.
- Conflicting utilities left in the same class string.
- Focus rings removed, or meaning carried by color alone.
- A new palette that ignores the existing `@theme` tokens.
