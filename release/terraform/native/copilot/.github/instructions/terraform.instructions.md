---
applyTo: "**/*.tf,**/*.tfvars"
---

# Terraform Copilot Instructions: Providers, State and Plan Review

Path-specific Copilot instructions for Terraform. They apply through `applyTo` and leave `.github/copilot-instructions.md` in place. Use `terraform-security-review` for a review.

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
