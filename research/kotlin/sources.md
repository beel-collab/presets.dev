# Kotlin sources

- https://blog.jetbrains.com/kotlin/2026/09/kotlin-2-4-20-released/ is the 2.4.20 post cited for coroutine trace recovery. This session did not re-download that page. The standards stay on the Kotlin version in the Gradle build.
- `CancellationException` must be rethrown. That is kotlinx.coroutines behaviour: https://kotlinlang.org/api/kotlinx.coroutines/kotlinx-coroutines-core/kotlinx.coroutines/-cancellation-exception/
