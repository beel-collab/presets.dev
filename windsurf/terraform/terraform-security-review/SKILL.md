---
id: "windsurf-terraform-security-review"
slug: "windsurf/terraform/terraform-security-review/SKILL"
title: "Terraform Security Review Skill for Windsurf"
description: "Windsurf skill for a Terraform security review. Use when you want that security review on a Terraform change. Do not use it for a different stack."
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

Install the native export at `.devin/skills/terraform-security-review/SKILL.md` and `.windsurf/skills/terraform-security-review/SKILL.md`.
Copy that export, not this catalog file. Catalog fields such as `tools` and `author` are for presets.dev.
Install one tool's skill for a checkout. Do not drop every tool's copy into `.agents/skills` under the same name.

<!-- native:start -->

# Terraform Security Review Skill for Windsurf

Skill `terraform-security-review` for Devin CLI and the legacy Windsurf skills folder. Invoke it with `/terraform-security-review`. This file is not a subagent.

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
