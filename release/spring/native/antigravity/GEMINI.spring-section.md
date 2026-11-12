<!-- Append this section to GEMINI.md. Do not replace the existing file. Antigravity CLI also loads AGENTS.md, so do not paste this section into both. /context lists the loaded files. -->

# Spring Boot Antigravity CLI Rules: Injection, Transactions and Validation

Section to append to `GEMINI.md` for Spring Boot. Antigravity CLI loads every `GEMINI.md` and every `AGENTS.md` it finds. Do not put this same section in both files. Confirm with `/context`.

## Updated for Spring Boot 4.1, Nov 2026
Do not upgrade dependencies or the framework version unless the task asks.

Stay on the Spring Boot and JDK the build already uses. For a new service, Boot 4.1 is the stable line to write for. Do not add an M, RC, or SNAPSHOT version because a blog shows it. A lazy DataSource connection is an option you turn on for a reason, not a default you copy into every app. Read `pom.xml` or `build.gradle` before you add a starter.

## Project shape

A web app splits controller, application service, and persistence. The controller maps HTTP. The service owns the use case and the transaction. The repository talks to the database. Do not put business rules in the controller.

Constructor injection is the default. Do not use field injection. A new bean is a constructor argument, not a static lookup.

## Validation and HTTP

Validate input with the project's Bean Validation annotations on the request DTO. A controller checks the binding result the way neighbors do. Do not trust a path id as proof the caller owns the row. Load the row and authorize.

Return the status the API already uses. A not-found and a forbidden are different. Do not catch every exception and return 200.

## Transactions and data

`@Transactional` sits on the service method that must commit or roll back together. Spring applies it with a proxy. A call from another method in the same class, `this.save()`, does not pass through that proxy, so `@Transactional` and `@Async` on the callee do not run. The same is true for a private method. Call through an injected bean, or move the boundary to the method that is actually invoked from outside. Do not call a remote HTTP API inside the transaction. Keep the transaction short.

A JPA query fetches what it needs. An open session that lazy-loads a collection in a loop is an N+1. Use a fetch join or a projection the project already prefers. Pagination has a page size cap.

## Security

Method security or security filter rules protect every state-changing endpoint. A new route copies the matcher style the app uses. CSRF, sessions, and stateless JWT follow the existing configuration. Do not permit all on a new matcher to make a test pass.

Do not log the Authorization header or the request body of a login. Secrets stay in the environment or the secret store the app already uses.

## Tests

A slice test covers a controller or a repository when the project uses slices. A full integration test uses the project's Testcontainers or embedded setup, not production. Assert the status, the body, and that an unauthorized caller is rejected. Run the test task. Record the output.

## Mistakes to avoid

- Field injection.
- A controller that contains the business transaction.
- `@Transactional` on a private self-invoked method.
- An N+1 lazy load in a loop.
- `permitAll` added to hide a failing test.
- An M, RC, or SNAPSHOT Boot version added to the build.

## What changed in this major

Boot 4.1 is the stable line. Do not add an M, RC, or SNAPSHOT version. `@Transactional` still needs a proxy.

## Deprecated APIs to never generate

`@MockBean` and `@SpyBean` were removed in Spring Boot 4. Use `@MockitoBean` and `@MockitoSpyBean`. `WebSecurityConfigurerAdapter` is deprecated. Declare a `SecurityFilterChain` bean and match paths with `requestMatchers`, not `antMatchers`.

## Commands

Run the Gradle or Maven test task.

## Example

```java
import org.springframework.stereotype.Service;
import org.springframework.transaction.annotation.Transactional;

record CreateNote(String body) {}

record Note(String body) {}

interface NoteRepository {
    Note save(Note note);
}

@Service
class NoteService {
    private final NoteRepository notes;

    NoteService(NoteRepository notes) {
        this.notes = notes;
    }

    @Transactional
    public Note create(CreateNote req) {
        return notes.save(new Note(req.body()));
    }
}
```

Call `create` from another bean. `this.create()` inside `NoteService` skips `@Transactional`.
