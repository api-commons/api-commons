---
name: Terms Of Service
description: Breaking up the terms of service into machine-readable, schema defined properties that allow for the legal side of an API to be understood programmatically. Providing a break down of what the legal constraints involved with putting an API to use will help consumers understand if it is a fit for their business needs.
image: /images/terms-of-service.png
url: '#'
machineReadable: false
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
  - type: TermsOfService
    url: https://example.com/terms

standards:
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
