## When to run

Run this review for a Kotlin coroutine, a Flow, a Compose screen, or an Android lifecycle change.

## When to leave it

Stop for a non-Kotlin repository. Do not upgrade Kotlin or Compose unless the user asked.

## Steps

1. Read the Kotlin version in the version catalog or `build.gradle`. A 2.4-only API on an older compiler is a high finding.
2. Search for `GlobalScope`, `runBlocking`, and `catch (e: Exception)` that does not rethrow `CancellationException`. Each is a high finding on app code.
3. Check Flow collection. A collection that ignores the lifecycle is a finding.
4. Search for `!!`. Each one on external data is a finding.
5. Run the unit test task only if the user asked. Otherwise write `not run`. Do not claim a device run you did not do.

## Output

Findings with severity, file, line, the cancellation or null bug, and a fix.

## Stop

Stop when the user asks you to swallow cancellation so a job "always finishes".
