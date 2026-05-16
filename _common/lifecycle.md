---
name: Lifecycle
description: Breaking down the stages of the lifecycle across APIs, while also providing instances for individual APIs, with details of each stage, the policies and rules applied within each stage, and the progress that APIs are making throughout the lifecycle
image: /images/lifecycle.png
url: '#'
machineReadable: false
source: concept
tags:
  - Lifecycle
  - Stages
  - Rules
  - Governance
aliases:
  - API Lifecycle
  - Maturity
  - Release Stage
yaml_example: |
  - type: X-Lifecycle
    url: https://developers.example.com/lifecycle

standards:
  - name: Semantic Versioning 2.0.0 (pre-release identifiers)
    url: https://semver.org/spec/v2.0.0.html
    kind: Community spec
  - name: RFC 9745 — The Sunset HTTP Response Header Field
    url: https://www.rfc-editor.org/rfc/rfc9745
    kind: IETF
  - name: The Deprecation HTTP Response Header Field (draft-ietf-httpapi-deprecation-header)
    url: https://datatracker.ietf.org/doc/draft-ietf-httpapi-deprecation-header/
    kind: IETF
  - name: Microsoft REST API Guidelines
    url: https://github.com/microsoft/api-guidelines/blob/vNext/Guidelines.md
    kind: Vendor guideline
  - name: Google API Improvement Proposals (AIPs)
    url: https://google.aip.dev/
    kind: Vendor guideline
  - name: AIP-181 — Stability levels
    url: https://google.aip.dev/181
    kind: Vendor guideline
  - name: OpenAPI Specification (info, deprecated)
    url: https://spec.openapis.org/oas/latest.html
    kind: OpenAPI Initiative

headers:
  - name: Sunset
    direction: response
    spec: RFC 9745
    description: Communicates the retirement date for an API or resource.
  - name: Deprecation
    direction: response
    spec: draft-ietf-httpapi-deprecation-header
    description: Marks a resource as deprecated as it moves through the lifecycle.

openapi_expression:
  - field: info.x-lifecycle
    spec: Vendor extension
    description: Common extension to declare stage (alpha, beta, ga, deprecated, retired).
  - field: info.x-stability
    spec: Vendor extension
    description: Used by some providers (e.g. Google AIP-181) to signal stability level.
  - field: deprecated
    spec: OpenAPI 3.x
    description: Marks operations or schemas at the deprecated stage of the lifecycle.

link_relations:
  - rel: sunset
    spec: RFC 9745
  - rel: deprecation
    spec: draft-ietf-httpapi-deprecation-header
  - rel: successor-version
    spec: RFC 5829

governance_rules:
  - id: naftiko-lifecycle
    source: Naftiko Sandbox (lifecycle/*.yml)
    description: Rules that verify each API declares a lifecycle stage and that deprecated endpoints carry Sunset.
  - id: oas-info-description
    source: Spectral built-in
    description: info.description should communicate stability and lifecycle expectations.
  - id: oas-operation-tag-defined
    source: Spectral built-in
    description: Tags can encode lifecycle (e.g. beta) and must be defined consistently.

risk:
  compliance:
    - SOC 2 CC8.1 — change management across release stages
    - ISO/IEC 27001 A.14.2 — security in development and support processes
  security_implications: Mixing experimental endpoints with production traffic without clearly signalling stability invites consumers to depend on unsupported behaviour. A documented lifecycle with explicit alpha/beta/GA/deprecated/retired stages, plus enforced sunset windows, limits exposure to unsupported code paths.

tools:
  - name: Backstage
    url: https://backstage.io/
    license: Apache-2.0
    category: Catalog
  - name: Spectral
    url: https://github.com/stoplightio/spectral
    license: Apache-2.0
    category: Linter
  - name: oasdiff
    url: https://github.com/oasdiff/oasdiff
    license: Apache-2.0
    category: Breaking-change detector
  - name: optic
    url: https://github.com/opticdev/optic
    license: MIT
    category: Change tracking

metrics:
  - name: apis_by_stage
    description: Count of APIs in each lifecycle stage (alpha, beta, GA, deprecated, retired).
  - name: time_in_stage_median_days
    description: Median dwell time per stage; surfaces stuck APIs.
  - name: beta_to_ga_conversion_rate
    description: Share of beta APIs that reach GA versus being retired.
  - name: retired_traffic
    description: Traffic still hitting retired endpoints; should trend to zero.

examples:
  - provider: Microsoft Graph
    url: https://providers.apis.io/providers/microsoft-graph/
    note: Explicit v1.0 (GA) and beta endpoints with documented promotion path.
  - provider: Google
    url: https://providers.apis.io/providers/google/
    note: AIP-driven stability levels and launch stages (preview, GA, deprecated).
  - provider: GitHub
    url: https://providers.apis.io/providers/github/
    note: Preview features with explicit opt-in media types until graduation.
  - provider: Stripe
    url: https://providers.apis.io/providers/stripe/
    note: Public preview and beta product flags surfaced in documentation.

related_properties:
  - versioning
  - deprecation-policy
  - change-log
  - road-map
  - governance
---
