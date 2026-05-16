---
name: FOCUS Billing Export
description: A FocusBillingExport property references an endpoint or documentation for a billing data export that conforms to the FOCUS (FinOps Open Cost and Usage Specification) schema — the cross-vendor open standard maintained by the FinOps Foundation for normalizing cloud, SaaS, and PaaS billing data. A FOCUS-conformant export allows API consumers, enterprise buyers, and FinOps tools to ingest cost and usage data in a consistent format without custom transformation.
image: /images/financial.png
url: '#'
tags:
  - FOCUS
  - FinOps
  - Billing
  - Cost
aliases:
  - FOCUS Export
  - FinOps Open Cost and Usage Specification Export
  - Cost and Usage Export
yaml_example: |
  - type: FocusBillingExport
    url: https://developers.example.com/billing/focus-export
    mediaType: application/json

standards:
  - name: FOCUS — FinOps Open Cost and Usage Specification
    url: https://focus.finops.org/
    kind: FinOps Foundation
  - name: FOCUS Specification (latest)
    url: https://focus.finops.org/focus-specification/
    kind: FinOps Foundation
  - name: FOCUS Conformance Program
    url: https://focus.finops.org/conformance/
    kind: FinOps Foundation
  - name: Apache Parquet
    url: https://parquet.apache.org/docs/file-format/
    kind: Apache Software Foundation
  - name: RFC 4180 — Common Format and MIME Type for CSV Files
    url: https://www.rfc-editor.org/rfc/rfc4180
    kind: IETF

media_types:
  - type: text/csv
    spec: RFC 4180
    note: Common delivery format for FOCUS exports.
  - type: application/vnd.apache.parquet
    note: Parquet is widely used for FOCUS billing exports; no IANA-registered media type at time of writing.
  - type: application/json
    note: Used by some providers for FOCUS-aligned API responses.

governance_rules:
  - id: focus-required-columns
    source: FOCUS Specification
    description: Export must include the mandatory FOCUS columns (e.g., BilledCost, EffectiveCost, ListCost, ContractedCost, UsageQuantity, BillingPeriodStart, BillingPeriodEnd, ChargePeriodStart, ChargePeriodEnd).
  - id: focus-currency-iso4217
    source: FOCUS Specification
    description: BillingCurrency must be an ISO 4217 currency code.
  - id: focus-version-declared
    source: FOCUS Specification
    description: Export should declare the FOCUS specification version it targets (e.g., 1.0, 1.1, 1.2).
  - id: focus-charge-class-categories
    source: FOCUS Specification
    description: ChargeClass and ChargeCategory values must use the FOCUS-defined enumerations.

risk:
  compliance:
    - SOC 2 — billing data is in scope for financial reporting controls
    - SOX — FOCUS exports often feed financial close processes
    - GDPR — billing exports may contain identifiers that are personal data
  security_implications: Billing exports concentrate commercially sensitive pricing, discount, and consumption data. Encrypt at rest, scope access via short-lived credentials, and avoid exposing per-row tenant identifiers without need.

tools:
  - name: FOCUS Specification
    url: https://focus.finops.org/
    category: Specification
  - name: FOCUS Converters (community)
    url: https://github.com/finopsfoundation
    category: Converters
  - name: OpenCost FOCUS export
    url: https://www.opencost.io/
    license: Apache-2.0
    category: Exporter
  - name: DuckDB
    url: https://duckdb.org/
    license: MIT
    category: Query engine for CSV/Parquet exports
  - name: Apache Parquet
    url: https://parquet.apache.org/
    license: Apache-2.0
    category: Columnar storage format

metrics:
  - name: focus_rows_exported
    description: Number of FOCUS rows produced for a billing period.
  - name: focus_columns_present
    description: Count of FOCUS-defined columns populated by the export.
  - name: focus_version_supported
    description: Highest FOCUS specification version a provider's export conforms to.
  - name: export_freshness_hours
    description: Time between charge incurrence and availability of the FOCUS row.

examples:
  - provider: AWS
    url: https://providers.apis.io/providers/aws/
    note: AWS Data Exports supports FOCUS 1.0 exports of the Cost and Usage Report.
  - provider: Microsoft Azure
    url: https://providers.apis.io/providers/azure/
    note: Microsoft Cost Management offers a FOCUS-aligned cost export.
  - provider: Google Cloud
    url: https://providers.apis.io/providers/google-cloud/
    note: Cloud Billing BigQuery export includes a FOCUS-aligned view.
  - provider: Oracle Cloud
    url: https://providers.apis.io/providers/oracle-cloud/
    note: OCI publishes FOCUS-conformant billing exports.

related_properties:
  - focus-conformance-report
  - focus-contract-commitments
  - invoice-reconciliation
  - finops-framework
  - opencost-specification
  - pricing
  - billing
---
