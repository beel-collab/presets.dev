---
applyTo: "**/*supabase*,**/*.sql"
---

# Supabase Copilot Instructions: Auth, RLS and Typed Queries

Path-specific Copilot instructions for Supabase. They apply through `applyTo` and leave `.github/copilot-instructions.md` in place. Use `supabase-security-review` for a review.

## Updated for supabase-js 2.119.0, Nov 2026

`@supabase/supabase-js` 2.119.0 is the npm `latest` release checked on 11 November 2026. Realtime broadcast persistence and per-request fetch options are on this line. Read the installed version before using them. Do not upgrade the client as a side effect of another edit.

## Project shape

The browser client uses the anon key. The service-role key stays on the server, in the environment the project already uses. A Next.js or other SSR app creates the server client the way the repo already does, with the request cookies. Do not invent a second auth helper.

SQL lives in migrations. Generated database types are generated. Do not hand-edit the generated file.

## Queries and RLS

Every table that holds user data has row level security enabled. A policy for `SELECT` does not cover `INSERT`, `UPDATE`, or `DELETE`. Writes need a `WITH CHECK` expression, not only `USING`. A policy that is `true` for every role is a bug unless the table is genuinely public.

The user id in a policy comes from `auth.uid()` or the project's equivalent. A column filled from a client-supplied id is not identity. Filter tenant rows in the policy, not only in the UI.

Use the typed client when the project generates types. Select the columns you need. Do not `select('*')` on a table that contains secrets and then return the row to the browser.

## Auth

Sign-in, refresh, and sign-out go through the project's auth helpers. After a session change, the server client sees the new cookies. Do not trust a user id, role, or tenant id posted from the browser. Read them from the session.

A route that mutates data checks the session before the write. Hiding the button is not the check.

## Realtime

Subscribe with a filter that matches the rows the user may see. Unsubscribe on cleanup. A persisted broadcast is still data. Do not put secrets in a broadcast payload. If you pass a custom fetch on a request, keep it local to that call. Do not replace the global fetch with a logger that prints headers.

## Errors and security

Map a Postgres error to a message the UI can show. Do not return the raw policy failure plus the service key's context. Log the code on the server.

Never ship the service-role key, a JWT secret, or a database URL to a client bundle. Search the diff for those names before you finish.

## Performance and tests

Add the index a new filter needs. A policy that calls a heavy function per row needs a reason. Paginate lists.

Test a policy with two users. The second user cannot read or write the first user's row. Run that test against a local database, not production. Record the command.

## Mistakes to avoid

- A service-role client constructed in browser code.
- A policy missing `WITH CHECK` on a write.
- Trusting `user_id` from the request body.
- A realtime channel with no filter and no cleanup.
- A generated types file edited by hand.
