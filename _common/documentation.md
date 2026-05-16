---
name: Documentation
description: A reference to the human readable documentation for an API, that describes the surface area of an API with all the details consumers need. This documentation may or may not be generated from an OpenAPI or other machine-readable artifact, but is published as HTML or Markdown, and mean for human consumption when onboarding with an API.
image: /images/documentation.png
url: '#'
machineReadable: false
source: concept
tags:
  - Onboarding
  - Documentation
  - Information
aliases:
  - Docs
  - API Reference
  - Developer Documentation
  - Reference
yaml_example: |
  - type: Documentation
    url: https://developers.example.com/docs

standards:
  - name: OpenAPI Specification 3.1
    url: https://spec.openapis.org/oas/v3.1.0
    kind: OpenAPI Initiative
  - name: OpenAPI Specification 3.0
    url: https://spec.openapis.org/oas/v3.0.3
    kind: OpenAPI Initiative
  - name: AsyncAPI 3.0
    url: https://www.asyncapi.com/docs/reference/specification/v3.0.0
    kind: AsyncAPI Initiative
  - name: JSON Schema 2020-12
    url: https://json-schema.org/specification-links#2020-12
    kind: IETF (draft)
  - name: RFC 9727 — api-catalog Well-Known URI
    url: https://www.rfc-editor.org/rfc/rfc9727
    kind: IETF
  - name: CommonMark 0.31
    url: https://spec.commonmark.org/0.31.2/
    kind: CommonMark
  - name: GraphQL — June 2018 Specification
    url: https://spec.graphql.org/
    kind: GraphQL Foundation
  - name: Schema.org APIReference
    url: https://schema.org/APIReference
    kind: Schema.org

headers:
  - name: Link
    direction: response
    spec: RFC 8288
    description: Carries link relations such as `service-doc` and `describedby` pointing to documentation.

well_known:
  - path: /.well-known/api-catalog
    spec: RFC 9727
    description: Discoverable catalog of an organization's APIs and their documentation.

media_types:
  - type: text/html
    note: Canonical rendered documentation format.
  - type: text/markdown
    spec: RFC 7763
  - type: application/vnd.oai.openapi
    note: OpenAPI document (YAML form).
  - type: application/vnd.oai.openapi+json
    note: OpenAPI document (JSON form).

openapi_expression:
  - field: info.description
    spec: OpenAPI 3.x
    description: Long-form Markdown description shown at the top of generated reference docs.
  - field: info.summary
    spec: OpenAPI 3.1
    description: Short description of the API.
  - field: info.termsOfService
    spec: OpenAPI 3.x
  - field: externalDocs
    spec: OpenAPI 3.x
    description: Pointer to additional human documentation (URL + description).
  - field: tags[].description
    spec: OpenAPI 3.x
    description: Per-tag prose used to group operations in rendered docs.
  - field: tags[].externalDocs
    spec: OpenAPI 3.x
  - field: operation.description
    spec: OpenAPI 3.x
    description: Per-operation Markdown rendered as the body of each endpoint section.

link_relations:
  - rel: service-doc
    spec: IANA Link Relations
    description: Link to documentation about the service in a human-readable form.
  - rel: describedby
    spec: RFC 8288
    description: Link to a resource describing the current resource.
  - rel: service-desc
    spec: IANA Link Relations
    description: Machine-readable service description (often paired with service-doc).

governance_rules:
  - id: info-description
    source: Spectral built-in
    description: "`info.description` must be present and non-empty."
  - id: info-contact
    source: Spectral built-in
    description: "`info.contact` must be defined so readers can reach the maintainers."
  - id: oas-tag-description
    source: Spectral built-in
    description: Every tag must have a description.
  - id: operation-description
    source: Spectral built-in
    description: Every operation must have a description.
  - id: operation-tag-defined
    source: Spectral built-in
    description: Operation tags must be declared at the document level (with descriptions).

risk:
  security_implications: Documentation often leaks sensitive details — internal hostnames, example tokens, unredacted PII in samples, or undocumented but discoverable endpoints. Treat docs as a publication surface; review samples for secrets and keep internal-only operations out of public bundles.
  compliance:
    - WCAG 2.2 — documentation sites are user-facing and subject to accessibility requirements
    - Export controls — cryptography-related docs may require classification review

tools:
  - name: Redocly
    url: https://redocly.com/
    category: Docs generator
  - name: Stoplight Elements
    url: https://stoplight.io/open-source/elements
    license: Apache-2.0
    category: Docs generator
  - name: Mintlify
    url: https://mintlify.com/
    category: Docs platform
  - name: Bump.sh
    url: https://bump.sh/
    category: Docs and change tracking
  - name: Scalar
    url: https://scalar.com/
    license: MIT
    category: Docs generator
  - name: ReadMe
    url: https://readme.com/
    category: Docs platform

metrics:
  - name: docs_coverage
    description: Share of operations with non-empty descriptions and at least one example.
  - name: time_to_first_doc_view
    description: Median time from signup to first documentation page view.
  - name: search_zero_results_rate
    description: Fraction of in-docs searches that return no results — proxy for content gaps.
  - name: stale_pages
    description: Count of pages whose last-modified date trails the latest spec revision.

examples:
  - provider: Stripe
    url: https://providers.apis.io/providers/stripe/
    note: Three-column reference docs generated from internal spec with side-by-side code samples.
  - provider: Twilio
    url: https://providers.apis.io/providers/twilio/
    note: Multi-product docs site with versioned reference and tutorials.
  - provider: GitHub
    url: https://providers.apis.io/providers/github/
    note: REST and GraphQL reference generated from the public OpenAPI description.
  - provider: Plaid
    url: https://providers.apis.io/providers/plaid/
    note: Narrative docs interleaved with reference, common in financial-data APIs.

related_properties:
  - openapi
  - getting-started
  - software-development-kits
  - change-log
  - tutorials
---
