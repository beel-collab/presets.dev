# Nuxt sources

Fetched 12 November 2026.

- Registry: https://registry.npmjs.org/nuxt reports `latest` 4.6.4.
- https://nuxt.com/docs/4.x/getting-started/upgrade is the Nuxt 4 upgrade guide. It describes `experimental.routeTypedFetch` as the switch that types `$fetch` and `useFetch` from generated route types. Leave it off unless the task asks.
- https://nuxt.com/docs/4.x/guide/going-further/runtime-config says keys outside `public` stay on the server, and keys under `public` are exposed to the client.
- https://nuxt.com/docs/4.x/migration/component-options says the Nuxt 2 `asyncData` and `fetch` hooks are replaced by `useAsyncData` and `useFetch`.
- https://nuxt.com/docs/4.x/getting-started/data-fetching documents `useFetch`. Pass a function, `() => `/api/notes/${route.params.id}``, so the request follows `useRoute()`. Copying the param into `ref()` once does not.
