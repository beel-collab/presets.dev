# Prisma sources

Fetched 12 November 2026.

- Registry: https://registry.npmjs.org/prisma reports `latest` 8.0.0-rc.33 and `prev` 7.10.1. Stay on 7.10.1 unless the repository already chose the release candidate.
- Upgrade guide: https://www.prisma.io/docs/guides/upgrade-prisma-orm/v7
  Prisma 7 requires a driver adapter for every database. Postgres on Node uses `@prisma/adapter-pg`. The client is constructed as `new PrismaClient({ adapter })`. The generator is `prisma-client` with an `output` path. CLI configuration lives in `prisma.config.ts`.
- Accelerate retirement: https://www.prisma.io/docs/postgres/database/switch-from-accelerate
  Hosted Accelerate connections retire on 1 December 2026. Local `prisma+postgres://localhost` URLs are not included. Do not pass `prisma://` or hosted `prisma+postgres://` to `PrismaPg`.
