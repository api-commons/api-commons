---
name: Chargeback Policy
description: A ChargebackPolicy property references a document describing how an API provider or internal platform allocates and recovers costs across teams, cost centers, or business units — including chargeback (actual cost transfer) and showback (visibility without transfer) methodologies. Chargeback and invoicing are formal capabilities in the FinOps Framework. Publishing a chargeback policy makes internal billing transparency discoverable, especially important for platform APIs used across multiple organizational units.
image: /images/policies.png
url: '#'
tags:
  - Chargeback
  - FinOps
  - Cost Allocation
  - Showback
aliases:
  - Cost Allocation Policy
  - Showback Policy
  - Internal Billing Policy
yaml_example: |
  - type: ChargebackPolicy
    url: https://developers.example.com/billing/chargeback

standards:
  - name: FinOps FOCUS Specification
    url: https://focus.finops.org/
    kind: FinOps Foundation
  - name: FinOps Framework — Allocation capability
    url: https://www.finops.org/framework/capabilities/allocation/
    kind: FinOps Foundation
  - name: FinOps Framework — Chargeback & Finance Integration
    url: https://www.finops.org/framework/capabilities/chargeback-finance-integration/
    kind: FinOps Foundation
  - name: ISO/IEC 19086-1 — Cloud SLA Framework
    url: https://www.iso.org/standard/67545.html
    kind: ISO/IEC
  - name: OpenCost Specification
    url: https://www.opencost.io/docs/specification
    kind: CNCF
  - name: AWS Cost Categories
    url: https://docs.aws.amazon.com/cost-management/latest/userguide/manage-cost-categories.html
    kind: Vendor
  - name: GCP Recommender
    url: https://cloud.google.com/recommender/docs
    kind: Vendor
  - name: Azure Cost Management
    url: https://learn.microsoft.com/azure/cost-management-billing/
    kind: Vendor

media_types:
  - type: text/html
    note: Most chargeback policies are published as human-readable documents.
  - type: application/json
    note: FOCUS-aligned cost data is typically delivered as JSON or Parquet.
  - type: text/csv
    note: FOCUS billing datasets are commonly distributed as CSV.

governance_rules:
  - id: info-contact
    source: Spectral built-in
    description: Cost-allocation disputes need a documented owner.
  - id: tag-description
    source: Spectral built-in
    description: Tags that drive allocation (cost-center, team, env) should carry explicit descriptions.

risk:
  compliance:
    - SOX — chargeback affects intercompany accounting and revenue recognition controls
    - GDPR — cost reports tied to individual user usage may contain personal data
    - IFRS 15 / ASC 606 — intercompany cost transfers must be auditable
    - SOC 2 CC4.1 — monitoring of internal financial controls
  security_implications: Cost-allocation tags often leak organizational structure, project codenames, and customer identifiers. Restrict access to detailed cost-and-usage reports the same way you would treat HR or revenue data.

tools:
  - name: OpenCost
    url: https://www.opencost.io/
    license: Apache-2.0
    category: Kubernetes cost allocation
  - name: Kubecost
    url: https://www.kubecost.com/
    category: Kubernetes cost allocation
  - name: CloudHealth
    url: https://www.vmware.com/products/cloud-health.html
    category: FinOps platform
  - name: Apptio Cloudability
    url: https://www.apptio.com/products/cloudability/
    category: FinOps platform
  - name: Vantage
    url: https://www.vantage.sh/
    category: FinOps platform
  - name: CloudZero
    url: https://www.cloudzero.com/
    category: Unit-economics analytics

metrics:
  - name: allocated_cost_ratio
    description: Share of total spend that is attributed to a named cost owner.
  - name: untagged_spend
    description: Spend that cannot be assigned to a cost center — the "shame metric" in FinOps.
  - name: chargeback_dispute_rate
    description: Share of monthly invoices internal teams formally dispute.
  - name: cost_per_team
    description: Recovered cost grouped by team / business unit.
  - name: showback_coverage
    description: Fraction of services that publish a showback report.

examples:
  - provider: AWS
    url: https://providers.apis.io/providers/aws/
    note: Cost Categories + Cost Allocation Tags drive chargeback across linked accounts.
  - provider: Google Cloud
    url: https://providers.apis.io/providers/google-cloud/
    note: Billing labels and folder hierarchy feed chargeback reports.
  - provider: Microsoft Azure
    url: https://providers.apis.io/providers/microsoft-azure/
    note: Management groups and tag inheritance support enterprise chargeback.
  - provider: Snowflake
    url: https://providers.apis.io/providers/snowflake/
    note: Resource monitors and warehouse-level usage support per-team chargeback.

related_properties:
  - pricing
  - unit-economics
  - plans
  - terms-of-service
  - service-level-agreement
---
