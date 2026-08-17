---
name: Benefits
description: >-
  The outcomes an API claims to produce for the people who adopt it — not what it does,
  but what changes for them. Benefits sit one level above features. A feature is a
  capability; a benefit is the result someone expects from using it. This is the softest
  thing an API publishes and the first thing a buyer reads, which is exactly why it is
  worth making machine-readable. The point is not to make marketing rigorous, it is to
  make it accountable — a benefit that names its audience, states the measure that would
  have to move for it to be true, and links to evidence that it did is a different object
  from one that does none of those, and publishing them in the same shape makes the
  difference visible without anyone having to argue about it.
image: /images/values.png
url: '#'
machineReadable: true
source: business
tags:
  - Benefits
  - Outcomes
  - Value
  - Marketing
aliases:
  - Value Proposition
  - Outcomes
  - Why Use This API
  - Business Value
yaml_example: |
  - name: Benefits
    type: Benefits
    url: https://example.com/benefits
    source_date: '2026-08-17'
    data:
      - name: Reduce onboarding time
        description: Get a new customer live without a services engagement.
        audience: business
        category: speed
        metric: days from contract signature to first successful call
        evidence_url: https://example.com/case-studies/onboarding

standards:
  - name: API Commons Benefits schema
    url: https://github.com/api-commons/benefits
    kind: API Commons (Apache-2.0)
  - name: schema.org Offer
    url: https://schema.org/Offer
    kind: Schema.org
  - name: schema.org Product
    url: https://schema.org/Product
    kind: Schema.org
  - name: schema.org Review
    url: https://schema.org/Review
    kind: Schema.org

openapi_expression:
  - field: info.description
    spec: OpenAPI 3.x
    description: Where the top-level value claim usually restates itself, in the provider's own words.
  - field: info.summary
    spec: OpenAPI 3.1
    description: A short statement of what the API is for — in practice, the benefit compressed to a line.
  - field: externalDocs
    spec: OpenAPI 3.x
    description: Can point at the benefits or case-study page substantiating the claims.

risk:
  compliance:
    - FTC Act §5 — substantiation for advertising claims
    - EU Directive 2005/29/EC — unfair commercial practices, including unsubstantiated claims
  security_implications: >-
    Benefit claims about security and compliance are the ones that cause real damage when
    they are loose. "Offload integration security" and "SOC 2 compliant" are routinely
    read as stronger than they are — offloading moves credentials to a different trust
    boundary rather than eliminating them, and a provider's certification does not
    transfer to its consumer. State which obligations actually move and which stay,
    especially where a shared-responsibility boundary is involved.

tools:
  - name: API Commons Benefits schema + validator
    url: https://github.com/api-commons/benefits
    license: Apache-2.0
    category: Machine-readable schema

metrics:
  - name: benefits_with_metric
    description: Share of published benefit claims that name a measure which would have to move for the claim to be true.
  - name: benefits_with_evidence
    description: Share of claims linked to a case study, benchmark, or report.
  - name: benefits_without_audience
    description: Count of claims that name no audience — usually addressed to everyone and landing with no one.
  - name: benefit_to_feature_coverage
    description: Share of claims traceable to a named feature that delivers them.

examples:
  - provider: Stripe
    url: https://stripe.com/payments
    note: Outcome-led product pages that lead with what changes for the business, with features underneath.
  - provider: Twilio
    url: https://www.twilio.com/en-us/messaging
    note: Per-channel value claims paired with customer stories.
  - provider: Plaid
    url: https://plaid.com/
    note: Benefits framed separately for developers and for the institutions buying.

related_properties:
  - features
  - use-cases
  - solutions
  - pricing
  - plans
  - compare
---
