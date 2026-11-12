# Vue sources

Fetched 12 November 2026.

- Registry: https://registry.npmjs.org/vue reports `latest` 3.5.45.
- https://blog.vuejs.org/posts/vue-3-5 announces Vue 3.5, including the reactive props destructure.
- https://vuejs.org/guide/components/props.html says destructuring `defineProps()` in `<script setup>` stays reactive on 3.5 because the compiler tracks the props. On 3.4 and earlier the same destructure is a one-time copy. `reactive()` and a Pinia store still need `toRefs` or `storeToRefs`.
- Do not generate Vue 2 `new Vue()` or `Vue.filter` in a Vue 3 app.
