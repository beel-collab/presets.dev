---
name: "terraform-security-review"
description: "Review a Terraform plan for provider fields, IAM scope, state secrets, and destructive actions. Use for a Terraform security review. Do not use to apply or destroy, or for a non-Terraform repository."
---

# Terraform Security Review Skill for Codex

Codex skill `terraform-security-review` for Terraform. Call it with `$terraform-security-review` or `/skills`. Do not install the other tools' copies beside it.

## When to run

Run this review for a Terraform change or a request to "review the plan". The work is read-only.

## When to leave it

Stop if the user asks you to apply or destroy. Explain that a person runs those. Do not run them.

## Steps

1. Read the required Terraform version and the provider lock. An attribute you cannot find in that provider's schema is a high finding. Do not guess a replacement field.
2. Review IAM and security groups in the diff. Flag a policy that grants more actions or a wider ARN than the resource needs. Do not flag `Resource "*"` when the action has no resource-level permission. `0.0.0.0/0` on an admin port is a high finding.
3. Search for secrets in variables, outputs, and tfvars. A committed secret is a high finding. Do not copy the secret into the report. Say the file and the variable name.
4. If a saved plan or `terraform plan` output is available and the user asked for a read-only plan, summarize creates, changes, replaces, and destroys. A replace of a data store is a high finding. If you cannot run plan, write `not run`.
5. Do not run `apply` or `destroy`.

## Output

Findings with severity, file, line, the risky action, and a narrower change. State clearly that nothing was applied.

```
## Findings
- high | path:line | what is wrong | what to do instead

## No findings
Say "No findings" and list the files you opened. A search you skipped is not a clean result.

## Example
Input: an `aws_security_group_rule` opens port 22 to `0.0.0.0/0`, and an IAM action that has no resource-level permission uses `Resource "*"`.
Output: high | sg.tf:4 | admin SSH is open to the world | restrict the CIDR. No findings for the `Resource "*"` on the action that requires it.
```

Do not flag the valid pattern named in the standards. Flag the mistake next to it.

## What to check

- Injection: concatenated SQL, shell, or HTML.
- XSS: unescaped user text in HTML.
- CSRF: a browser state change with the framework check disabled.
- Secrets: a key in the repo or in a log line.
- IDOR: an id from the client with no owner or permission check.
- SSRF: a user-supplied URL fetched with no allow-list.

## Stop

Stop when the user asks for apply, destroy, or a prod workspace you were not given read-only access to.

## Severity

`high` is a bug a caller can hit or a secret that leaks. `medium` is a broken contract that needs a specific input. `low` is a cleanup that does not change behaviour.
