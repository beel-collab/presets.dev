# Kotlin sources

Fetched 12 November 2026.

- https://kotlinlang.org/docs/whatsnew2420.html documents Kotlin 2.4.20, released 7 September 2026. Coroutine stack-trace recovery is stable and on by default. The blog post is https://blog.jetbrains.com/kotlin/2026/09/kotlin-2-4-20-released/.
- https://kotlinlang.org/api/kotlinx.coroutines/kotlinx-coroutines-core/kotlinx.coroutines/-cancellation-exception/ is why a caught `CancellationException` must be rethrown. `GlobalScope` is still the wrong scope for UI work.
- A build stays on the Kotlin version in its Gradle script.
