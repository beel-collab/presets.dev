# Prisma sources

Checked 12 November 2026.

- Upgrade guide: https://www.prisma.io/docs/guides/upgrade-prisma-orm/v7
  Prisma 7 requires a driver adapter for every database. Postgres on Node uses `@prisma/adapter-pg`. The client is constructed as `new PrismaClient({ adapter })`. The generator is `prisma-client` with an `output` path. CLI configuration lives in `prisma.config.ts`.
- Accelerate retirement: https://www.prisma.io/docs/postgres/database/switch-from-accelerate
  Hosted Accelerate connections retire on 1 December 2026. Local `prisma+postgres://localhost` URLs are not included. Do not pass `prisma://` or hosted `prisma+postgres://` to `PrismaPg`.
- npm tags read earlier in this release: `latest` was 8.0.0-rc.33 and `prev` was 7.10.1. Stay on 7 unless the repository already chose the release candidate.
