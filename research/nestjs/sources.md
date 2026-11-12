# NestJS sources

Fetched 12 November 2026.

- Registry: https://registry.npmjs.org/@nestjs/core reports `latest` 12.4.2.
- https://docs.nestjs.com/application/validation documents `@Body({ schema })` with `StandardSchemaValidationPipe`, including Zod. The decorator alone does not validate. Class DTOs with `ValidationPipe` remain valid. A TypeScript interface is not a runtime schema.
- https://github.com/nestjs/nest/releases/tag/v12.0.0 is the Nest 12 release that introduced that schema option.
