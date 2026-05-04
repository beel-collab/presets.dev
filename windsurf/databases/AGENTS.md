---
title: "Database / Models"
description: "Place in your database/ or models/ directory. Auto-applies when Cascade works with schema files, migrations, or query code."
tags: ["databases"]
author:
  name: Community
  url: 'https://github.com/beel-collab/presets.dev'
---

# Database Conventions

## Schema Design
- Every table has a UUID primary key — never use business data as PK
- `NOT NULL` by default — nullable columns must be explicitly justified
- Use `timestamptz` for all timestamps (timezone-aware)
- Use `numeric`/`decimal` for money — never `float`
- Soft deletes with `deleted_at timestamptz NULL` — hard deletes only with explicit approval

## Naming
- Tables: `snake_case` plural nouns (`users`, `order_items`)
- Columns: `snake_case` (`created_at`, `user_id`)
- Foreign keys: `{referenced_table_singular}_id` (`user_id`, `product_id`)
- Indexes: `idx_{table}_{column(s)}` (`idx_orders_user_id`)
- Constraints: `{table}_{column}_fk`, `{table}_{column}_uq`

## Migrations
- Every schema change goes through a migration file — no manual ALTER in production
- Migrations must be reversible — always write the `down` migration
- Zero-downtime pattern for large tables: add nullable column → backfill in batches → add constraint → remove old column
- Never rename a column directly — add new column, migrate data, drop old

## Queries
- Specify columns explicitly — no `SELECT *`
- Use CTEs for complex queries — readability over cleverness
- Keyset pagination over `OFFSET` for large datasets
- Always `EXPLAIN ANALYZE` before declaring a query optimized

## Indexing
- Index every foreign key column
- Composite index: most selective column first
- Partial indexes for filtered queries: `WHERE status = 'active'`
- Review and drop unused indexes — they slow down writes

## What to Avoid
- N+1 queries — use `JOIN`, `include`, or `prefetch_related`
- Raw string interpolation in queries — always use parameterized statements
- Business logic inside stored procedures — keep it in the application layer
- Dropping columns without a deprecation period
