---
name: Pricing
description: Providing a machine-readable scaffolding to define the plans and pricing for APIs, and the common elements of each tier of pricing and access available. Pricing is not just about the financial aspect of access to APIs, it is also about which APIs you will have access to, and how much of a resource you can consume over time. Pricing is about enabling API consumers to have a plan for how they will use digital resources that is in alignment with a platform business strategy.
image: /images/pricing.png
url: '#'
machineReadable: true
source: commons
tags:
  - SDKs
aliases:
  - Plans
  - Tiers
  - Rate Card
  - Price List
yaml_example: |
  - type: Pricing
    url: https://example.com/pricing

standards:
  - name: schema.org Offer
    url: https://schema.org/Offer
    kind: schema.org
  - name: schema.org PriceSpecification
    url: https://schema.org/PriceSpecification
    kind: schema.org
  - name: schema.org UnitPriceSpecification
    url: https://schema.org/UnitPriceSpecification
    kind: schema.org
  - name: FinOps FOCUS Specification
    url: https://focus.finops.org/
    kind: FinOps Foundation
  - name: Stripe Pricing Table
    url: https://docs.stripe.com/payments/checkout/pricing-table
    kind: Vendor
  - name: Naftiko plans/*.yml
    url: https://github.com/naftiko
    kind: Community
  - name: ISO 4217 — Currency codes
    url: https://www.iso.org/iso-4217-currency-codes.html
    kind: ISO
  - name: ISO 8601 — Date and time / durations
    url: https://www.iso.org/iso-8601-date-and-time-format.html
    kind: ISO

headers:
  - name: Content-Type
    direction: response
    spec: RFC 9110
    description: Pricing documents are typically served as text/html or application/json; machine-readable feeds may use application/json or application/yaml.

status_codes:
  - code: '402'
    name: Payment Required
    spec: RFC 9110 §15.5.3
    description: Reserved for future use; some APIs (e.g. Stripe, GitHub) use it to signal billing failure or quota exhaustion.
  - code: '429'
    name: Too Many Requests
    spec: RFC 6585 §4
    description: Used when a consumer exceeds the request volume permitted by their pricing tier.

media_types:
  - type: text/html
    note: Most public pricing pages are human-readable HTML.
  - type: application/json
    note: Machine-readable plan / price feeds.
  - type: application/yaml
    note: Naftiko plans/*.yml and API Commons descriptors.

openapi_expression:
  - field: info.x-pricing
    spec: OpenAPI extension (vendor)
    description: No standard OpenAPI field for pricing; commonly expressed via x- extensions or links in info.description.
  - field: info.termsOfService
    spec: OpenAPI 3.x
    description: Often points to a page that bundles terms with pricing tier definitions.

governance_rules:
  - id: info-contact
    source: Spectral built-in
    description: API metadata must include a contact — pricing inquiries depend on a reachable owner.
  - id: info-license
    source: Spectral built-in
    description: License is required and is frequently surfaced alongside pricing.

risk:
  compliance:
    - PCI DSS v4 — applies whenever pricing pages collect or display cardholder data
    - EU Consumer Rights Directive (2011/83/EU) — price transparency for EU consumers
    - GDPR — pricing experiments that profile users may require lawful basis
    - SOX — material pricing changes for public companies require disclosure controls
  security_implications: Pricing endpoints are scraped aggressively. Inconsistent pricing surfaces (web vs. API vs. sales) cause customer disputes; cache invalidation on tier changes is a frequent source of overcharges.

tools:
  - name: Stripe Billing
    url: https://stripe.com/billing
    category: Subscription billing
  - name: Recurly
    url: https://recurly.com/
    category: Subscription billing
  - name: Chargebee
    url: https://www.chargebee.com/
    category: Subscription billing
  - name: Metronome
    url: https://metronome.com/
    category: Usage-based billing
  - name: Orb
    url: https://www.withorb.com/
    category: Usage-based billing
  - name: OpenMeter
    url: https://openmeter.io/
    license: Apache-2.0
    category: Open-source metering

metrics:
  - name: arpu
    description: Average revenue per user across a plan or cohort.
  - name: plan_conversion_rate
    description: Share of free / trial accounts that upgrade to a paid tier.
  - name: price_per_call
    description: Effective unit price derived from total spend over total billable calls.
  - name: overage_rate
    description: Share of customers exceeding their plan limits in a period.
  - name: tier_distribution
    description: Headcount or revenue split across plan tiers.

examples:
  - provider: Stripe
    url: https://providers.apis.io/providers/stripe/
    note: Tiered, volume, and graduated pricing models exposed via Prices and Products APIs.
  - provider: AWS
    url: https://providers.apis.io/providers/aws/
    note: Per-service price lists published as Price List Bulk API (JSON / CSV).
  - provider: Anthropic
    url: https://providers.apis.io/providers/anthropic/
    note: Per-million-token input / output pricing tiers with cached-token discounts.
  - provider: OpenAI
    url: https://providers.apis.io/providers/openai/
    note: Per-model token pricing with batch and cached-input discounts.

related_properties:
  - plans
  - rate-limits
  - unit-economics
  - chargeback-policy
  - terms-of-service
  - interface-license
---
