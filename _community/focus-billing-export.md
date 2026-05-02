---
name: FOCUS Billing Export
description: A FocusBillingExport property references an endpoint or documentation for a billing data export that conforms to the FOCUS (FinOps Open Cost and Usage Specification) schema — the cross-vendor open standard maintained by the FinOps Foundation for normalizing cloud, SaaS, and PaaS billing data. A FOCUS-conformant export allows API consumers, enterprise buyers, and FinOps tools to ingest cost and usage data in a consistent format without custom transformation.
image: /images/financial.png
url: #
tags:
  - FOCUS
  - FinOps
  - Billing
  - Cost
yaml_example: |
  - type: FocusBillingExport
    url: https://developers.example.com/billing/focus-export
    mediaType: application/json
---
