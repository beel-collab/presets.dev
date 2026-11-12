# Terraform sources

- Terraform 1.17.1 is the patch named at https://github.com/hashicorp/terraform/releases/tag/v1.17.1 in the release plan. This session did not download the changelog body again. The behaviour rules below are AWS IAM, not a Terraform language change.
- https://docs.aws.amazon.com/service-authorization/latest/reference/reference_policies_actions-resources-contextkeys.html is the reference for actions that have no resource-level permissions and therefore require `Resource "*"`.
