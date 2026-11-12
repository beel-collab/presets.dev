# Terraform sources

Fetched 12 November 2026.

- https://github.com/hashicorp/terraform/releases/tag/v1.17.1 is Terraform 1.17.1, published 28 October 2026. The notes are bug fixes: `fmt` preserves the original file if a write fails, module policies run during a destroy plan, and stacks report every policy result for a replaced resource. Review the plan. Do not apply or destroy from the agent.
- https://docs.aws.amazon.com/service-authorization/latest/reference/reference_policies_actions-resources-contextkeys.html is the reference for actions that have no resource-level permissions and therefore require `Resource "*"`. Flag a permission that is broader than the action needs, not the star by itself.
- https://registry.terraform.io/providers/hashicorp/template/latest/docs says the template provider is deprecated and archived. Replace `template_file` with the `templatefile()` function.
