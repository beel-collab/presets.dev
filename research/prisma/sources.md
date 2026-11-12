# Prisma sources

Fetched 12 November 2026.

- Registry: https://registry.npmjs.org/prisma reports `latest` 8.0.0-rc.33 and `prev` 7.10.1. Stay on 7.10.1 unless the repository already chose the release candidate.
- CLI reference: https://www.prisma.io/docs/orm/reference/prisma-cli-reference shows `prisma validate` loading `schema.prisma` and reporting whether the schema is valid. The sample output does not connect to a database.
- Upgrade guide: https://www.prisma.io/docs/guides/upgrade-prisma-orm/v7
  Prisma 7 requires a driver adapter for every database. The guide's Postgres example imports `PrismaClient` from `./generated/prisma/client` and `PrismaPg` from `@prisma/adapter-pg`, then calls `new PrismaClient({ adapter: new PrismaPg({ connectionString: process.env.DATABASE_URL }) })`. The generator is `prisma-client` with a required `output`. CLI configuration lives in `prisma.config.ts`. The instantiate page uses the placeholder `./path/to/generated/prisma`; the upgrade example is the concrete path.
- Accelerate retirement: https://www.prisma.io/docs/postgres/database/switch-from-accelerate
  Hosted Accelerate connections retire on 1 December 2026. Local `prisma+postgres://localhost` URLs are not included. Do not pass `prisma://` or hosted `prisma+postgres://` to `PrismaPg`.
