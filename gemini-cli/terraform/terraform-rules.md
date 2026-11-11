---
id: "gemini-cli-terraform-rules"
slug: "gemini-cli/terraform/terraform-rules"
title: "Terraform Gemini CLI Rules: Providers, State and Plan Review"
description: "Gemini CLI rules for Terraform: Providers, State and Plan Review. Append to GEMINI.md. Structure, security, and tests. Terraform 1.17, Nov 2026."
type: "rule"
tools:
  - "gemini-cli"
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
  - "Gemini CLI docs 2026-11-11; CLI not run"
created: "2026-11-11"
updated: "2026-11-11"
libs:
  - "terraform@1.17"
updated_for: "Terraform 1.17, Nov 2026"
---

# Terraform Gemini CLI Rules: Providers, State and Plan Review

## Install

Install the native export at `GEMINI.md` as an appended section, then check `/memory show`.
Copy that export, not this catalog file. Catalog fields such as `tools` and `author` are for presets.dev.
Install one tool's skill for a checkout. Do not drop every tool's copy into `.agents/skills` under the same name.

<!-- native:start -->

# Terraform Gemini CLI Rules: Providers, State and Plan Review

Section to append to `GEMINI.md` for Terraform. Confirm with `/memory show`. The review skill waits for consent before it runs.

## Updated for Terraform 1.17, Nov 2026

Stay on the Terraform version in `.terraform-version` or the CI image. Terraform 1.17 is the current line to write for when CI is already on it. Do not invent a provider argument. Read the locked provider schema. Required version constraints and the lock file are committed. Do not bump a provider because a plan failed on an unknown attribute you guessed.

## Project shape

Modules have a small interface: variables, outputs, and resources. A root module wires providers and backends. A child module does not configure a backend. Names describe the resource, not `main` copied ten times.

State lives in the remote backend the project already uses, with locking. Do not commit `terraform.tfstate`. A local state file in a PR is a leak.

## Changes

`plan` is the review artifact. `apply` and `destroy` are human actions. Do not run them from an agent turn. A `-target` apply is a last resort with a written reason.

Read the plan JSON or the plan output for replaces, destroys, and IAM changes. A `force_new` that replaces a database is a high-severity review, not a routine edit.

## Security

IAM actions are the verbs the resource needs, on the ARN it needs. `*` on action or resource is a finding. A security group does not open `0.0.0.0/0` on an admin port.

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
