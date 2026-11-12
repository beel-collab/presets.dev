---
id: "windsurf-terraform-security-review"
slug: "windsurf/terraform/terraform-security-review/SKILL"
title: "Terraform Security Review Skill for Windsurf"
description: "Review a Terraform plan for provider fields, IAM scope, state secrets, and destructive actions. Use for a Terraform security review. Do not use to apply or destroy, or for a non-Terraform repository."
type: "skill"
tools:
  - "windsurf"
stack: "terraform"
tags:
  - "terraform"
  - "infrastructure"
  - "security"
author:
  name: "presets.dev"
  github: "beel-collab"
license: "MIT"
origin: "original"
version: "1.0.0"
tested_with:
  - "Devin and Cascade docs 2026-11-11; not run"
created: "2026-11-11"
updated: "2026-11-11"
libs:
  - "terraform@1.17"
updated_for: "Terraform 1.17, Nov 2026"
---

# Terraform Security Review Skill for Windsurf

## Install

Install the native export at `.devin/skills/terraform-security-review/SKILL.md`.
Copy that export, not this catalog file. Catalog fields such as `tools` and `author` are for presets.dev.
Install one tool's skill for a checkout. Do not drop every tool's copy into `.agents/skills` under the same name.

<!-- native:start -->

# Terraform Security Review Skill for Windsurf

Devin skill `terraform-security-review` for Terraform. Invoke it with `/terraform-security-review`. Install only `.devin/skills`. This file is not a subagent.

## When to run

Run this review for a Terraform change or a request to "review the plan". The work is read-only.

## When to leave it

Do not upgrade dependencies or the framework version unless the user asked.

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

- State: a state file committed to the repo, or a remote backend with no lock.
- IAM: an action allowed more broadly than it needs. `Resource "*"` is required for some actions that have no resource-level permissions, so do not flag the star by itself.
- Secrets: a password or key written in `.tf` or committed `.tfvars`.
- Network: `0.0.0.0/0` on an admin port such as 22 or 3389.
- Apply: do not plan an `apply` or `destroy` from the agent.

## Stop

Stop when the user asks for apply, destroy, or a prod workspace you were not given read-only access to.

## Severity

`high` is a bug a caller can hit or a secret that leaks. `medium` is a broken contract that needs a specific input. `low` is a cleanup that does not change behaviour.
