---
description: "Kotlin standards for Coroutines, Null Safety and Compose. Use when editing this stack. Kotlin 2.4 stable line, Nov 2026."
trigger: "model_decision"
---

# Kotlin Windsurf Rules: Coroutines, Null Safety and Compose

Devin rule for Kotlin. Install the `.devin/rules` file. The trigger is model decision. Do not also copy it into `.windsurf/rules`.

## Updated for Kotlin 2.4, Nov 2026
Do not upgrade dependencies or the framework version unless the task asks.

Stay on the Kotlin version the Gradle build uses. The 2.4 line adds coroutine trace recovery and Swift-export improvements. Use them only when the compiler is already on 2.4. Do not upgrade Kotlin, Compose, or the Android Gradle Plugin unless the task asks. A multiplatform target is added only when the project is already multiplatform.

## Project shape

Match the source sets. Android UI uses the Compose compiler the project already applies. A ViewModel or the project's presenter owns screen state. A composable displays state and sends events up. Do not fetch the network directly inside a composable.

## Coroutines

Launch in a scope that is canceled with the owner: `viewModelScope`, `lifecycleScope`, or a scope the class cancels in `close`. `GlobalScope` is a bug. `runBlocking` does not belong inside a suspend function or on the main thread.

A coroutine checks cancellation. Do not catch `Exception` and ignore `CancellationException`. Rethrow it. A `Flow` is collected in `repeatOnLifecycle` or the project's equivalent so it stops when the screen stops. A hot flow shared with `shareIn` has a stopping policy.

## Null and errors

Prefer `?.` and a real branch over `!!`. `!!` is a crash you chose. A public function returns a sealed result or throws the project's exception. Do not return null for three different failures.

## Compose and Android

State that changes the UI is `mutableStateOf` or a `StateFlow` collected as state. Remember a callback that closes over a changing value, or pass the event up. Keys on a lazy list are stable ids.

A permission, a camera, or a location request follows the Activity result API the project uses. Do not call a deprecated start-activity-for-result snippet. Main-thread work stays tiny. Database and network use the dispatcher the app already injects.

## Tests

A coroutine test uses `runTest` and a test dispatcher. Advance time instead of sleeping. A Compose test sets content and asserts semantics. Run the project's unit test task. Record the output. Say when a device was not used.

## Mistakes to avoid

- `GlobalScope` or `runBlocking` on a suspend path.
- A `catch` that swallows `CancellationException`.
- `!!` on a value that can be null.
- A Flow collected without a lifecycle stop.
- A Kotlin upgrade bundled into a UI fix.

## What changed in this major

Kotlin 2.4 keeps `CancellationException` special. `GlobalScope` is still the wrong scope.

## Deprecated APIs to never generate

No API covered here was deprecated or removed.

## Commands

Run the Gradle unit test task.

## Example

```kotlin
viewModelScope.launch {
  try { repo.refresh() }
  catch (e: CancellationException) { throw e }
}
```
