---
name: "terraform-security-review"
description: "Review a Terraform plan for provider fields, IAM scope, state secrets, and destructive actions. Use for a Terraform security review. Do not use to apply or destroy, or for a non-Terraform repository."
---

# Terraform Security Review Skill for Cline

Cline skill `terraform-security-review` for Terraform. `/terraform-security-review` forces it. A global skill of the same name overrides this project file.

## When to run

Run this review for a Terraform change or a request to "review the plan". The work is read-only.

## When to leave it

Stop if the user asks you to apply or destroy. Explain that a person runs those. Do not run them.

## Steps

1. Read the required Terraform version and the provider lock. An attribute you cannot find in that provider's schema is a high finding. Do not guess a replacement field.
2. Review IAM and security groups in the diff. `*` or `0.0.0.0/0` on an admin port is a high finding.
3. Search for secrets in variables, outputs, and tfvars. A committed secret is a high finding. Do not copy the secret into the report. Say the file and the variable name.
4. If a saved plan or `terraform plan` output is available and the user asked for a read-only plan, summarize creates, changes, replaces, and destroys. A replace of a data store is a high finding. If you cannot run plan, write `not run`.
5. Do not run `apply` or `destroy`.

## Output

Findings with severity, file, line, the risky action, and a narrower change. State clearly that nothing was applied.

## Stop

Stop when the user asks for apply, destroy, or a prod workspace you were not given read-only access to.
