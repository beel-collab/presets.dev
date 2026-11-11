<!-- Append this section to GEMINI.md. Do not replace the existing file. Confirm with /memory show. -->

# NestJS Gemini CLI Rules: Modules, DTOs and Guards

Section to append to `GEMINI.md` for NestJS. Confirm with `/memory show`. The review skill waits for consent before it runs.

## Updated for NestJS 12.4.2, Nov 2026

`@nestjs/core` 12.4.2 is the npm `latest` release checked on 11 November 2026. Read the installed major and the Node engine it requires before you add a pattern. Do not upgrade Nest as a side effect. A provider that is not registered in a module is not injectable.

## Project shape

A feature is a module that declares its controllers and providers and exports only what other modules may use. Do not reach into another module's private provider. A new provider is listed in `providers`. A global module is rare and already a project decision.

Controllers take DTOs. Services own the use case and the transaction. Repositories talk to the database. Do not query from the controller.

## DTOs and validation

A DTO is a class with the project's validation decorators, and the global validation pipe is on. A TypeScript `interface` disappears at runtime and does not validate. Do not use an interface as the `@Body()` type and call it safe.

The validation pipe rejects unknown fields when the project has `whitelist` and `forbidNonWhitelisted`. Keep that on. A write copies the DTO fields the entity is allowed to store. Do not spread the DTO into a save if the DTO contains a role or an owner id the client must not set.

## Guards and errors

A route that changes data has a guard. Class-level `@UseGuards` is easy to forget on a new method. Public routes are marked with the project's public decorator and are rare. Check the owner inside the service even after the guard, when the guard only checks that someone is signed in.

Throw the project's HTTP exception. A filter formats the body. Do not catch and return the ORM error to the client.

## Tests

A unit test builds the service with mocks for its collaborators. An e2e test boots the module the project already boots and calls the route without a token. Cover 401, a bad DTO, and a successful owner. Run the test script. Record the output.

## Mistakes to avoid

- A provider constructed with `new` instead of injection, or missing from the module.
- A TypeScript type treated as validation.
- A DTO spread into a database write.
- A new route with no guard.
- A global pipe turned off to accept a sloppy client.
