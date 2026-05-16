---
name: Unit Economics
description: A UnitEconomics property references a document describing the per-unit cost model for an API — such as cost per API call, cost per gigabyte processed, cost per token consumed, or cost per transaction. Unit economics are a core FinOps capability under the Quantify Business Value domain. Publishing a unit cost breakdown alongside an API makes pricing structure discoverable by enterprise procurement, FinOps tools, and developers building cost-aware applications.
image: /images/pricing.png
url: '#'
tags:
  - Unit Economics
  - FinOps
  - Pricing
  - Cost
aliases:
  - Cost per Unit
  - Per-Unit Cost
  - Unit Cost Model
yaml_example: |
  - type: UnitEconomics
    url: https://developers.example.com/billing/unit-economics

standards:
  - name: FinOps FOCUS Specification
    url: https://focus.finops.org/
    kind: FinOps Foundation
  - name: FinOps Framework — Quantify Business Value
    url: https://www.finops.org/framework/domains/quantify/
    kind: FinOps Foundation
  - name: FinOps Framework — Unit Economics capability
    url: https://www.finops.org/framework/capabilities/forecasting/
    kind: FinOps Foundation
  - name: FOCUS columns — BilledCost, EffectiveCost, UsageQuantity, UsageUnit
    url: https://focus.finops.org/focus-specification/
    kind: FinOps Foundation
  - name: SaaS Metrics — CAC, LTV, Gross Margin
    url: https://www.saasmetrics.co/
    kind: SaaS Metrics
  - name: schema.org UnitPriceSpecification
    url: https://schema.org/UnitPriceSpecification
    kind: schema.org
  - name: UN/CEFACT Recommendation 20 — Units of Measure
    url: https://unece.org/trade/uncefact/cl-recommendations
    kind: UN/CEFACT

media_types:
  - type: text/html
    note: Unit-economics dashboards are typically rendered as HTML.
  - type: application/json
    note: Machine-readable unit-cost feeds and FOCUS exports.
  - type: text/csv
    note: FinOps tooling commonly ingests CSV exports.

governance_rules:
  - id: info-description
    source: Spectral built-in
    description: API descriptions should document the billable unit (call, token, GB, row).
  - id: operation-description
    source: Spectral built-in
    description: Operations that bill differently than the API default need explicit notes.

risk:
  compliance:
    - SOX — unit-cost reporting feeds material financial disclosures
    - IFRS 15 / ASC 606 — revenue recognition tied to billable units
    - SOC 2 CC4.1 — internal controls over operational metrics
  security_implications: Per-unit cost data exposes infrastructure efficiency and customer concentration. Restrict access at the same level as gross-margin and revenue data.

tools:
  - name: CloudZero
    url: https://www.cloudzero.com/
    category: Unit economics analytics
  - name: Vantage
    url: https://www.vantage.sh/
    category: FinOps platform
  - name: OpenCost
    url: https://www.opencost.io/
    license: Apache-2.0
    category: Kubernetes unit cost
  - name: Finout
    url: https://www.finout.io/
    category: FinOps platform
  - name: Datadog Cloud Cost Management
    url: https://www.datadoghq.com/product/cloud-cost-management/
    category: Cost observability
  - name: OpenMeter
    url: https://openmeter.io/
    license: Apache-2.0
    category: Usage metering

metrics:
  - name: cost_per_request
    description: Total cost divided by total billable requests.
  - name: cost_per_token
    description: Cost per input / output token for LLM and AI APIs.
  - name: cost_per_gb
    description: Cost per gigabyte processed or stored.
  - name: cost_per_customer
    description: Fully-loaded cost divided by active customer count.
  - name: gross_margin_per_unit
    description: Revenue per unit minus cost per unit.
  - name: cac_ltv_ratio
    description: Customer acquisition cost relative to lifetime value.

examples:
  - provider: AWS
    url: https://providers.apis.io/providers/aws/
    note: Per-service unit pricing exposed through the Price List API.
  - provider: Anthropic
    url: https://providers.apis.io/providers/anthropic/
    note: Per-million-token unit economics with input / output / cached / batch differentiation.
  - provider: OpenAI
    url: https://providers.apis.io/providers/openai/
    note: Per-token unit pricing per model family with batch and cached-input discounts.
  - provider: Twilio
    url: https://providers.apis.io/providers/twilio/
    note: Per-message and per-minute unit pricing across SMS, voice, and verify products.

related_properties:
  - pricing
  - chargeback-policy
  - plans
  - rate-limits
  - service-level-agreement
---
