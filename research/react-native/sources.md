# React Native sources

Fetched 12 November 2026.

- Registry: https://registry.npmjs.org/react-native reports `latest` 0.88.1. https://registry.npmjs.org/expo reports `latest` 58.0.24. Keep the SDK and React Native pair the app already has.
- https://reactnative.dev/blog is the React Native release blog.
- https://reactnavigation.org/docs/navigation-lifecycle/ says that navigating from Home to Profile mounts Profile and leaves Home mounted. Focus and blur are how you see a screen come and go. `useFocusEffect` is the hook for focus-owned work. Effect cleanup is for a real unmount.
- React 19.3 DOM APIs are not native APIs. See https://react.dev/blog/2026/09/09/react-19-3.
