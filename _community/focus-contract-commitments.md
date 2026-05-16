---
name: FOCUS Contract Commitments
description: A FocusContractCommitments property references an endpoint or document for commitment-based pricing data structured according to the FOCUS Contract Commitment Dataset (introduced in FOCUS v1.3). This supplemental dataset isolates reserved instance, savings plan, and enterprise discount program terms — including commitment start and end dates, remaining committed units, and commitment type — from per-row cost and usage data, enabling FinOps tooling to reconcile commitment purchases against actual consumption.
image: /images/contract.png
url: '#'
tags:
  - FOCUS
  - FinOps
  - Commitments
  - Reserved Instances
aliases:
  - Commitment Discount Dataset
  - FOCUS Commitments
  - Reservation and Savings Plan Inventory
yaml_example: |
  - type: FocusContractCommitments
    url: https://developers.example.com/billing/commitments
    mediaType: application/json

standards:
  - name: FOCUS — FinOps Open Cost and Usage Specification
    url: https://focus.finops.org/
    kind: FinOps Foundation
  - name: FOCUS Specification (latest)
    url: https://focus.finops.org/focus-specification/
    kind: FinOps Foundation
  - name: FOCUS CommitmentDiscount columns
    url: https://focus.finops.org/focus-specification/
    kind: FinOps Foundation
  - name: FOCUS Conformance Program
    url: https://focus.finops.org/conformance/
    kind: FinOps Foundation

governance_rules:
  - id: commitment-id-stable
    source: FOCUS Specification
    description: CommitmentDiscountId must be stable for the life of the commitment so consumption rows can be joined to it.
  - id: commitment-type-enum
    source: FOCUS Specification
    description: CommitmentDiscountType must use the FOCUS enumeration (e.g., Reservation, SavingsPlan, Other).
  - id: commitment-status-enum
    source: FOCUS Specification
    description: CommitmentDiscountStatus must use the FOCUS enumeration (e.g., Used, Unused).
  - id: commitment-currency-iso4217
    source: FOCUS Specification
    description: Monetary commitment values must use an ISO 4217 currency code.

risk:
  compliance:
    - SOX — commitment liabilities feed financial accruals and lease-like disclosures
    - SOC 2 — commitment data is in scope for financial reporting controls
  security_implications: Commitment data discloses negotiated discount structures and enterprise spend posture; treat as commercially sensitive.

tools:
  - name: FOCUS Specification
    url: https://focus.finops.org/
    category: Specification
  - name: FOCUS Validator
    url: https://github.com/finopsfoundation/focus_validator
    license: Apache-2.0
    category: Conformance validator
  - name: OpenCost
    url: https://www.opencost.io/
    license: Apache-2.0
    category: Cost allocation engine
  - name: CloudZero
    url: https://www.cloudzero.com/
    category: Commitment management
  - name: Vantage
    url: https://www.vantage.sh/
    category: Commitment management

metrics:
  - name: commitments_active_count
    description: Count of active commitments visible in the dataset.
  - name: commitment_utilization_pct
    description: Percentage of committed units consumed in the period.
  - name: commitment_remaining_value
    description: Remaining monetary value across active commitments.
  - name: commitment_expiring_30d
    description: Number of commitments expiring within 30 days, useful for renewal alerting.

examples:
  - provider: AWS
    url: https://providers.apis.io/providers/aws/
    note: AWS Savings Plans and Reserved Instances map to FOCUS CommitmentDiscount columns.
  - provider: Google Cloud
    url: https://providers.apis.io/providers/google-cloud/
    note: Google Cloud Committed Use Discounts (CUDs) align to FOCUS commitments.
  - provider: Microsoft Azure
    url: https://providers.apis.io/providers/azure/
    note: Azure Reservations and Savings Plans surface through FOCUS CommitmentDiscount fields.
  - provider: Oracle Cloud
    url: https://providers.apis.io/providers/oracle-cloud/
    note: OCI Universal Credits and annual commitments can be expressed as FOCUS commitments.

related_properties:
  - focus-billing-export
  - focus-conformance-report
  - invoice-reconciliation
  - finops-framework
  - pricing
  - contract
---
