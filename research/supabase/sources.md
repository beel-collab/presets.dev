# Supabase sources

Fetched 12 November 2026.

- Registry: https://registry.npmjs.org/@supabase/supabase-js reports `latest` 2.119.0.
- https://supabase.com/docs/guides/getting-started/migrating-to-new-api-keys says `anon` and `service_role` are legacy keys. New keys use the `sb_publishable_` and `sb_secret_` forms. Both systems work until the legacy keys are disabled. A secret or `service_role` key bypasses RLS and must not ship in the browser.
- https://supabase.com/docs/guides/database/postgres/row-level-security is the Supabase RLS guide. A publishable or `anon` key in the browser is not a finding when RLS is on.
- https://www.postgresql.org/docs/current/sql-createpolicy.html says a `DELETE` policy cannot have `WITH CHECK`. `UPDATE` policies accept both `USING` and `WITH CHECK`. If no `WITH CHECK` expression is defined, `USING` is also used for the new row.
- https://supabase.com/docs/guides/realtime/authorization is Realtime authorization. A client-side Realtime filter is not that boundary.
