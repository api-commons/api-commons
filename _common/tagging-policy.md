---
name: Tagging Policy
description: A TaggingPolicy property references a document defining the cost allocation tag taxonomy for an API or platform — including required tag keys such as CostCenter, Environment, Product, and Owner, along with allowed values and compliance requirements. Cost allocation tagging is a foundational FinOps practice, and the FinOps Foundation publishes guidance on tagging policy compliance. Publishing a tagging policy makes cost attribution requirements discoverable by consumers integrating the API into their FinOps workflows.
image: /images/tags.png
url: '#'
tags:
  - Tagging
  - FinOps
  - Cost Allocation
  - Governance
aliases:
  - Tag Policy
  - Cost Allocation Tags
  - Resource Tagging Policy
yaml_example: |
  - type: TaggingPolicy
    url: https://developers.example.com/billing/tagging

standards:
  - name: OpenAPI Specification 3.1 — Tag Object
    url: https://spec.openapis.org/oas/v3.1.0#tag-object
    kind: OpenAPI Initiative
  - name: Redocly x-tagGroups vendor extension
    url: https://redocly.com/docs/api-reference-docs/specification-extensions/x-tag-groups
    kind: Redocly
  - name: AWS Tagging Best Practices
    url: https://docs.aws.amazon.com/whitepapers/latest/tagging-best-practices/tagging-best-practices.html
    kind: AWS
  - name: Google Cloud — Resource labels
    url: https://cloud.google.com/resource-manager/docs/creating-managing-labels
    kind: Google Cloud
  - name: Azure — Tag resources
    url: https://learn.microsoft.com/en-us/azure/azure-resource-manager/management/tag-resources
    kind: Microsoft Azure
  - name: FinOps Foundation — Tagging
    url: https://www.finops.org/framework/capabilities/onboarding-workloads/
    kind: FinOps Foundation

media_types:
  - type: application/json
    note: Machine-readable tagging policy documents.
  - type: application/yaml
    note: Common authoring format for tag taxonomies.

openapi_expression:
  - field: tags
    spec: OpenAPI 3.x
    description: Global array of tag objects with names and descriptions used to organize operations.
  - field: tags (operation)
    spec: OpenAPI 3.x
    description: Operation-level tags grouping endpoints by domain, lifecycle, or audience.
  - field: x-tagGroups
    spec: Redocly vendor extension
    description: Groups tags into named sections for navigation in rendered documentation.

governance_rules:
  - id: operation-tag-defined
    source: Spectral built-in (spectral:oas)
    description: Every operation tag must be declared in the global tags array.
  - id: oas-tag-description
    source: Spectral built-in (spectral:oas)
    description: Tags must include a description so their scope is unambiguous.
  - id: tags-alphabetical
    source: Spectral built-in (spectral:oas, recommended off by default)
    description: Tags should be ordered alphabetically for consistency.

risk:
  compliance:
    - SOC 2 CC2.x — accurate cost attribution underpins financial reporting controls
    - ISO/IEC 27001 A.8 — asset inventory and ownership rely on consistent tagging
  governance: Inconsistent or missing required tags produces unallocated cloud spend, broken chargeback/showback, and ungoverned shadow workloads.

tools:
  - name: AWS Tag Editor
    url: https://docs.aws.amazon.com/ARG/latest/userguide/tag-editor.html
    category: Tag management
  - name: AWS Config — required-tags rule
    url: https://docs.aws.amazon.com/config/latest/developerguide/required-tags.html
    category: Tag compliance
  - name: Azure Policy — tag policies
    url: https://learn.microsoft.com/en-us/azure/governance/policy/samples/built-in-policies
    category: Tag compliance
  - name: Spectral
    url: https://github.com/stoplightio/spectral
    license: Apache-2.0
    category: OpenAPI tag linting

metrics:
  - name: tag_coverage_percent
    description: Share of resources or operations carrying all required tag keys.
  - name: untagged_cost_share
    description: Percentage of monthly spend not attributable due to missing tags.
  - name: tag_policy_violations
    description: Count of resources or operations failing the active tagging policy.
  - name: tag_key_cardinality
    description: Distinct values per tag key; high cardinality often signals taxonomy drift.

examples:
  - provider: AWS
    url: https://providers.apis.io/providers/aws/
    note: Resource tags drive cost allocation reports and Service Control Policy enforcement.
  - provider: Google Cloud
    url: https://providers.apis.io/providers/google-cloud/
    note: Labels on resources feed Cloud Billing export and BigQuery analysis.
  - provider: Microsoft Azure
    url: https://providers.apis.io/providers/microsoft-azure/
    note: Azure Policy enforces required tags across subscriptions and management groups.

related_properties:
  - policies
  - rules
  - billing
  - openapi
  - governance
---
