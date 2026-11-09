---
name: Terms Of Service
description: Breaking up the terms of service into machine-readable, schema defined properties that allow for the legal side of an API to be understood programmatically. Providing a break down of what the legal constraints involved with putting an API to use will help consumers understand if it is a fit for their business needs.
image: /images/terms-of-service.png
url: '#'
machineReadable: true
source: concept
tags:
  - Legal
  - TOS
  - Terms of Service
  - Terms of Use
aliases:
  - ToS
  - Terms of Use
  - ToU
  - Acceptable Use Policy
  - Service Agreement
  - EULA
yaml_example: |
  - name: Terms of Service
    type: TermsOfService
    description: The terms of service of the Example Weather API, harvested from its own page.
    url: terms/example-weather-api-terms-of-service.yml
    source_date: '2026-11-09'
    data:
      terms_of_service: 0.1.0
      provider: Example Weather API
      aid: example-weather-api
      url: https://weather.example.com/legal/api-terms
      source_date: '2026-11-09'
      x-apis-io-derivation:
        synthetic: false
        method: harvested
        read: '2026-11-09'
        tool: engine/business/harvest-business.py
        model: claude-haiku-4-5
      effective_date: Last updated March 1, 2026
      permitted_use:
      - summary: Display forecasts in your application
        text: You may use the API to retrieve and display weather data within your own applications.
      prohibited_use:
      - summary: Resale of raw data
        text: You may not resell, sublicense or redistribute raw API data as a standalone data product.
      caching:
        stance: conditional
        max_duration: 24 hours
        text: You may cache API responses for up to 24 hours to improve performance.
      redistribution:
        stance: prohibited
        text: You may not resell, sublicense or redistribute raw API data as a standalone data product.
      attribution:
        required: true
        text: Applications must display "Weather data by Example Weather API" wherever the data
          is shown.
      governing_law:
        jurisdiction: State of Oregon
        text: These Terms are governed by the laws of the State of Oregon.
      liability_cap:
        text: Our total liability will not exceed the fees you paid us in the 12 months before the
          claim.
      termination_notice:
        period: 30 days
        text: We may terminate your access for convenience with 30 days written notice.
      change_notice:
        period: 14 days
        text: We will post changes to these Terms at least 14 days before they take effect.
      rate_or_usage_limits_referenced:
        text: Your use is subject to the rate limits described in our documentation.

standards:
  - name: API Commons Terms of Service schema
    url: https://github.com/api-commons/terms-of-service
    kind: API Commons (CC BY-NC-SA 4.0 artifacts, Apache-2.0 code)
  - name: W3C ODRL Information Model 2.2
    url: https://www.w3.org/TR/odrl-model/
    kind: W3C
  - name: OpenAPI Specification — info.termsOfService
    url: https://spec.openapis.org/oas/v3.1.0#info-object
    kind: OpenAPI Initiative
  - name: schema.org termsOfService
    url: https://schema.org/termsOfService
    kind: schema.org
  - name: IANA Link Relation — terms-of-service
    url: https://www.iana.org/assignments/link-relations/link-relations.xhtml
    kind: IANA
  - name: Common Paper — Cloud Service Agreement Standard
    url: https://commonpaper.com/standards/cloud-service-agreement/
    kind: Common Paper
  - name: Terms of Service; Didn't Read (ToS;DR)
    url: https://tosdr.org/
    kind: Community
  - name: Creative Commons Licenses
    url: https://creativecommons.org/licenses/
    kind: Creative Commons
  - name: SPDX License List
    url: https://spdx.org/licenses/
    kind: Linux Foundation

headers:
  - name: Link
    direction: response
    spec: RFC 8288
    description: May advertise rel="terms-of-service" pointing at the human-readable policy.

status_codes:
  - code: '451'
    name: Unavailable For Legal Reasons
    spec: RFC 7725
    description: Resource withheld due to legal demand; often references terms or jurisdiction.

openapi_expression:
  - field: info.termsOfService
    spec: OpenAPI 3.x §4.8.2 Info Object
    description: URL to the Terms of Service for the API.
  - field: info.license
    spec: OpenAPI 3.x §4.8.2 / License Object
    description: License governing use of the API description (and often referenced from ToS).
  - field: info.contact
    spec: OpenAPI 3.x §4.8.2 / Contact Object
    description: Legal/contractual contact for ToS questions.

link_relations:
  - rel: terms-of-service
    spec: IANA Link Relations registry
    note: Used in Link headers, Atom, HAL, JSON:API, and HTML <link>.
  - rel: license
    spec: RFC 4946 / IANA
    note: Often paired with ToS to describe IP terms.

governance_rules:
  - id: info-contact
    source: Spectral built-in
    description: Info object should include contact details — applies to ToS as well.
  - id: info-license
    source: Spectral built-in
    description: Info object should reference a license — complements ToS.
  - id: info-license-url
    source: Spectral built-in
    description: License must include a URL.

risk:
  compliance:
    - GDPR Art. 13/14 — information to be provided to data subjects (often linked from ToS)
    - CCPA/CPRA §1798.130 — notice at collection
    - EU DSA — clear terms for online intermediary services
    - FTC Act §5 — prohibition on unfair or deceptive terms (US)
    - Consumer Rights Act 2015 — unfair terms (UK/EU equivalents)
  security_implications: A clear, versioned ToS is itself a security control — it sets acceptable-use boundaries (scraping, automation, abuse), defines incident-response and notification obligations, allocates liability, and authorizes the provider to suspend abusive consumers. Track effective_date and prior versions so consumers can detect breaking legal changes the same way they track API versions.

tools:
  - name: API Commons Terms of Service schema + validator
    url: https://github.com/api-commons/terms-of-service
    license: Apache-2.0
    category: Machine-readable schema
  - name: Common Paper
    url: https://commonpaper.com/
    category: Standardized contract templates
  - name: ToS;DR
    url: https://tosdr.org/
    category: Crowd-sourced ToS rating
  - name: Docusign CLM
    url: https://www.docusign.com/products/clm
    category: Contract lifecycle management
  - name: Ironclad
    url: https://ironcladapp.com/
    category: Contract lifecycle management
  - name: PolicyGenius / Termly
    url: https://termly.io/
    category: Policy generator
  - name: Diff-checker for ToS versions
    url: https://www.diffchecker.com/
    category: Change tracking

metrics:
  - name: tos_version_count
    description: Number of distinct ToS versions published; growth signals legal cadence.
  - name: days_since_last_tos_update
    description: Time since the most recent material change.
  - name: tos_acceptance_rate
    description: Share of new signups that explicitly accept the current ToS.
  - name: machine_readable_tos_coverage
    description: Whether info.termsOfService is set across the provider's OpenAPI documents.

examples:
  - provider: Stripe
    url: https://providers.apis.io/providers/stripe/
    note: Versioned Services Agreement plus per-product terms.
  - provider: GitHub
    url: https://providers.apis.io/providers/github/
    note: Customer Agreement, API Terms, Acceptable Use Policies on docs.github.com.
  - provider: Google
    url: https://providers.apis.io/providers/google/
    note: Google APIs Terms of Service plus per-service supplementary terms.
  - provider: Twilio
    url: https://providers.apis.io/providers/twilio/
    note: Master Services Agreement, Acceptable Use Policy.

related_properties:
  - privacy-policy
  - signup
  - security
  - rate-limits
  - service-level-agreement
---
