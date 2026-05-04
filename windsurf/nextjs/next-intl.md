---
trigger: manual
title: "Next Intl"
tags: ["nextjs"]
author:
  name: Community
  url: 'https://github.com/beel-collab/presets.dev'
---

# Key Rules for Setting Up i18n Routing with next-intl

## i18n Routing Options:
- Use prefix-based (`/en/about`) routing.
- Use a `[locale]` dynamic segment in the App Router to serve localized content.

## Basic Setup:
- Install `next-intl` using `npm install next-intl`.
- Organize the project structure to include a `messages` folder for translations and necessary configuration files like `routing.ts`, `middleware.ts`, and `request.ts`.

## Translations:
- Store translations in JSON files (e.g., `messages/en.json`).
- Load translations dynamically based on the user’s locale.

## Configuration:
- Use `next.config.mjs` to set up a `next-intl` plugin for request-specific i18n configurations.
- Define supported locales and a default locale in `routing.ts`.

## Middleware Integration:
- Use middleware (`middleware.ts`) to handle locale negotiation and path matching (e.g., `/` → `/en`).

## Dynamic Locale Handling:
- Implement a centralized configuration in `request.ts` to manage locale-specific settings and translations for Server Components.

## Component Integration:
- Use `NextIntlClientProvider` in `layout.tsx` to pass translations and locale data to Client Components.
- Use hooks like `useTranslations` and `Link` in pages (e.g., `page.tsx`) for localized content and navigation.

## Static Rendering:
- Add `generateStaticParams` to layouts or pages to enable static rendering for localized routes.
- Call `setRequestLocale` in each layout and page to validate the locale and enable static rendering before using `next-intl` APIs.

## Metadata Localization:
- Use the `locale` param in metadata generation (`generateMetadata`) to provide localized titles or other metadata.

## Best Practices:
- Always validate the incoming locale.
- Ensure that `setRequestLocale` is called before invoking any `next-intl` functionality.
- Customize routing and navigation APIs as needed while leveraging `next-intl` wrappers.
