---
id: "windsurf-terraform-rules"
slug: "windsurf/terraform/terraform-rules"
title: "Terraform Windsurf Rules: Providers, State and Plan Review"
description: "Windsurf rules for Terraform: Providers, State and Plan Review. Structure, data, errors, security, performance, and tests. Terraform 1.17, Nov 2026."
type: "rule"
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

# Terraform Windsurf Rules: Providers, State and Plan Review

## Install

Install the native export at `.devin/rules/terraform-rules.md`.
Copy that export, not this catalog file. Catalog fields such as `tools` and `author` are for presets.dev.
Install one skill file per name. Cursor, GitHub Copilot, Codex, Antigravity CLI, and Devin can all read `.agents/skills`, so a second copy with the same name collides.

<!-- native:start -->

# Terraform Windsurf Rules: Providers, State and Plan Review

Devin rule for Terraform. Install the `.devin/rules` file. The trigger is model decision. Do not also copy it into `.windsurf/rules`.

## Updated for Terraform 1.17, Nov 2026
Do not upgrade dependencies or the framework version unless the task asks.

Stay on the Terraform version in `.terraform-version` or the CI image. Terraform 1.17 is the current line to write for when CI is already on it. Do not invent a provider argument. Read the locked provider schema. Required version constraints and the lock file are committed. Do not bump a provider because a plan failed on an unknown attribute you guessed.

## Project shape

Modules have a small interface: variables, outputs, and resources. A root module wires providers and backends. A child module does not configure a backend. Names describe the resource, not `main` copied ten times.

State lives in the remote backend the project already uses, with locking. Do not commit `terraform.tfstate`. A local state file in a PR is a leak.

## Changes

`plan` is the review artifact. `apply` and `destroy` are human actions. Do not run them from an agent turn. A `-target` apply is a last resort with a written reason.

Read the plan JSON or the plan output for replaces, destroys, and IAM changes. A `force_new` that replaces a database is a high-severity review, not a routine edit.

## Security

IAM actions are the verbs the resource needs. Some AWS actions have no resource-level permission and the resource element must be `"*"`. That star is not, by itself, a finding. A finding is a permission wider than the action requires: extra actions, a star on an action that does support resource ARNs, or `0.0.0.0/0` on an admin port.

Secrets are not in `.tfvars` committed to git and not in outputs. Mark sensitive outputs. A variable default that contains a key is a bug. Use the project's secret manager or a write-only input.

Provider aliases and regions match the environment. Do not point a dev workspace at a prod account to "see if it plans".

## Checks

`terraform fmt` and `terraform validate` use the project's version. `plan` runs with the read-only credentials the project documents, in the right workspace. Record the command and whether the plan was applied. The default is not applied.

## Mistakes to avoid

- An invented provider field.
- `apply` or `destroy` run autonomously.
- Broad IAM or an open admin port.
- A secret in state outputs or committed tfvars.
- A state file committed to the repository.

## What changed in this major

Terraform 1.17 plans are the review artifact. Do not invent provider arguments.

## Deprecated APIs to never generate

The `hashicorp/template` provider is deprecated and archived. Replace a `template_file` data source with the `templatefile()` function.

## Commands

Run `terraform fmt` and `terraform validate`. Do not apply.

## Example

```hcl
resource "aws_s3_bucket" "logs" {
  bucket = var.logs_bucket
}
```
Plan this. Do not apply it from the agent.
