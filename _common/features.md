---
name: Features
description: A summary of what an API can do — the consumer-facing capability list that bridges marketing claims and reference documentation. Features pages are how prospective consumers evaluate fit before they read the reference, and how internal teams confirm parity with competitors. A clear features pointer lets discovery tools surface capability summaries without crawling the entire docs site.
image: /images/features.png
url: '#'
machineReadable: true
source: commons
tags:
  - Discovery
  - Capabilities
  - Marketing
aliases:
  - Capabilities
  - Platform Features
  - Feature List
  - Product Features
  - What You Can Do
yaml_example: |
  - name: Features
    type: Features
    url: https://example.com/features
    source_date: '2026-08-17'
    data:
      - name: Bulk send
        description: Send the same message to up to 10,000 recipients in one request.
        category: Messaging
        status: ga
        tiers:
          - Pro
        operations:
          - createBulkSend

standards:
  - name: API Commons Features schema
    url: https://github.com/api-commons/features
    kind: API Commons (Apache-2.0)
  - name: schema.org Product
    url: https://schema.org/Product
    kind: Schema.org
  - name: schema.org Service
    url: https://schema.org/Service
    kind: Schema.org
  - name: schema.org PropertyValue
    url: https://schema.org/PropertyValue
    kind: Schema.org

openapi_expression:
  - field: info.description
    spec: OpenAPI 3.x
    description: Frequently restates the top-level feature summary at the head of the spec.
  - field: tags
    spec: OpenAPI 3.x
    description: Operation tags often map 1:1 to the feature areas advertised externally.

risk:
  security_implications: Features pages occasionally enumerate capabilities (admin actions, data exports, write operations) that the reference docs gate behind elevated scopes — making them an accidental scope-discovery surface for attackers. Keep the features list aligned with what is actually authorized at the default tier.

tools:
  - name: API Commons Features schema + validator
    url: https://github.com/api-commons/features
    license: Apache-2.0
    category: Machine-readable schema

metrics:
  - name: features_to_signup_conversion
    description: Share of features-page visits that convert to a signup or contact-sales event.
  - name: features_parity_with_reference
    description: Count of advertised features not yet covered by an operation in the OpenAPI description.
  - name: features_freshness_days
    description: Days since each feature entry was last reviewed against actual product behavior.

examples:
  - provider: Stripe
    url: https://stripe.com/payments/features
    note: Per-product features pages broken down by payment method and capability.
  - provider: Twilio
    url: https://www.twilio.com/messaging/features
    note: Channel-by-channel features grid for the Messaging API.
  - provider: GitHub
    url: https://github.com/features
    note: Platform-level features index linking into per-feature deep dives.

related_properties:
  - benefits
  - documentation
  - use-cases
  - pricing
  - portal
---
