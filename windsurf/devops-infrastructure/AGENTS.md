---
title: "Infrastructure / DevOps"
description: "Place in your infrastructure/, deploy/, or .github/ directory. Auto-applies when Cascade works with CI configs, Dockerfiles, or IaC files."
tags: ["devops-infrastructure"]
author:
  name: Community
  url: 'https://github.com/beel-collab/presets.dev'
---

# Infrastructure Conventions

## Docker
- Pin base image versions — never `:latest` in production (`node:20.11-alpine`)
- Multi-stage builds to minimize final image size
- Run as non-root user: `USER node` before `CMD`
- Health check on every service container
- Secrets via environment variables — never baked into images or layers

## CI/CD Pipeline Order
1. Lint & format check (fastest — fail early)
2. Unit tests
3. Build
4. Integration tests
5. Security scan (Trivy, npm audit)
6. Deploy to staging
7. Smoke tests
8. Deploy to production

## Deployment Strategy
- Blue/green or canary deployments — no in-place replacement
- Rollback must be possible in under 5 minutes
- Feature flags for risky changes — decouple deploy from release
- Never deploy on Fridays or before holidays

## Environment Variables
- All config via environment variables — no hardcoded values
- Required vars validated at startup — crash immediately if missing
- Never log env var values — they may contain secrets
- Three environments minimum: `development`, `staging`, `production`

## Infrastructure as Code
- All infrastructure defined in code (Terraform, Pulumi, CDK) — no manual console changes
- State stored remotely (S3 + DynamoDB lock, Terraform Cloud)
- Plan reviewed before apply — no auto-apply in production
- Tag all resources: `environment`, `service`, `owner`, `cost-center`

## Observability Requirements
Every service must expose:
- `/health` endpoint — liveness check
- `/ready` endpoint — readiness check (DB connected, cache warm)
- Structured JSON logs with `request_id`, `service`, `level`, `message`
- Metrics: request rate, error rate, p95 latency
