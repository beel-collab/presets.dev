## When to run

Run this review for a Spring Boot controller, service, security matcher, or JPA query.

## When to leave it

Stop for a Java program that is not Spring. Do not upgrade Boot or the JDK unless the user asked. Do not take a 4.2 RC.

## Steps

1. Read the Boot version in the build file. A bump to a release candidate is a high finding unless the user asked for it.
2. Review new endpoints for an authorization rule. A missing matcher or `permitAll` on a write is a high finding.
3. Review `@Transactional` and `@Async`. A transaction that wraps an HTTP call is a finding. A self-call (`this.method()`) onto a `@Transactional` or `@Async` method in the same class is a high finding, because the proxy never sees it.
4. Review JPA. A loop that triggers lazy loads is a finding. A query that returns entities the controller then mutates across requests is a finding.
5. Check validation on the request DTO. A body bound straight onto an entity is a high finding.
6. Run the project's test task only if the user asked. Otherwise write `not run`.

## Output

Findings with severity, file, line, the missing auth or the transaction bug, and a fix.

```
## Findings
- high | path:line | what is wrong | what to do instead

## No findings
Say "No findings" and list the files you opened. A search you skipped is not a clean result.

## Example
Input: `NoteService.create` is `@Transactional` and `NoteService.importAll` calls `this.create(row)`.
Output: high | NoteService.java:28 | self-invocation skips the proxy, so the transaction does not start | call `create` through the injected bean.
```

Do not flag the valid pattern named in the standards. Flag the mistake next to it.

## What to check

- Injection: a native query built by concatenating a request parameter.
- XSS: a template renders user text with the escape disabled.
- CSRF: a browser state change with CSRF disabled on the security filter chain.
- Secrets: a password in `application.yml` that is committed.
- IDOR: a path id loaded with no authorization check.
- SSRF: `RestClient` calls a URL from the request with no allow-list.
- Transactions: `this.method()` on a `@Transactional` or `@Async` method, which skips the proxy.

## Stop

Stop when the user asks you to open every endpoint or to point tests at production.

## Severity

`high` is a bug a caller can hit or a secret that leaks. `medium` is a broken contract that needs a specific input. `low` is a cleanup that does not change behaviour.
