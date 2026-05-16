---
name: Deprecation Policy
description: Every API will eventually be deprecated, so having a plan and communicating the deprecation policy with consumers via a dedicated page makes a lot of sense. This page will help API providers think a little bit about the future, and establish some guard rails and channels for communication with consumers.
image: /images/deprecation.png
url: '#'
machineReadable: false
source: concept
tags:
  - Deprecation
  - Policies
aliases:
  - Sunset Policy
  - End-of-Life
  - EOL
yaml_example: |
  - type: DeprecationPolicy
    url: https://developers.example.com/deprecation

standards:
  - name: RFC 9745 — The Sunset HTTP Response Header Field
    url: https://www.rfc-editor.org/rfc/rfc9745
    kind: IETF
  - name: RFC 8594 — The Sunset HTTP Header Field (obsoleted by RFC 9745)
    url: https://www.rfc-editor.org/rfc/rfc8594
    kind: IETF (historic)
  - name: The Deprecation HTTP Response Header Field (draft-ietf-httpapi-deprecation-header)
    url: https://datatracker.ietf.org/doc/draft-ietf-httpapi-deprecation-header/
    kind: IETF
  - name: RFC 5829 — Link Relation Types for Simple Version Navigation
    url: https://www.rfc-editor.org/rfc/rfc5829
    kind: IETF
  - name: RFC 8288 — Web Linking
    url: https://www.rfc-editor.org/rfc/rfc8288
    kind: IETF
  - name: OpenAPI Specification (deprecated flag)
    url: https://spec.openapis.org/oas/latest.html
    kind: OpenAPI Initiative

headers:
  - name: Sunset
    direction: response
    spec: RFC 9745
    description: HTTP-date indicating when the resource will become unresponsive.
  - name: Deprecation
    direction: response
    spec: draft-ietf-httpapi-deprecation-header
    description: Indicates a resource is deprecated; value is the deprecation date or the token "true".
  - name: Link
    direction: response
    spec: RFC 8288
    description: Carries sunset, deprecation, successor-version, and alternate relations pointing to migration targets.

link_relations:
  - rel: sunset
    spec: RFC 9745
    note: Points to a policy or document describing the upcoming removal.
  - rel: deprecation
    spec: draft-ietf-httpapi-deprecation-header
    note: Points to documentation about the deprecation.
  - rel: successor-version
    spec: RFC 5829
    note: Identifies the next version of a versioned resource.
  - rel: latest-version
    spec: RFC 5829
  - rel: predecessor-version
    spec: RFC 5829
  - rel: alternate
    spec: RFC 8288

openapi_expression:
  - field: deprecated
    spec: OpenAPI 3.x
    description: Boolean flag on Operation, Parameter, Schema, or Header objects marking the element as deprecated.
  - field: info.x-sunset
    spec: Vendor extension
    description: Common extension for documenting sunset date at the API level.

governance_rules:
  - id: oas-operation-deprecated
    source: Spectral built-in
    description: Deprecated operations should be flagged and ideally include migration guidance.
  - id: oas-path-deprecated
    source: Spectral built-in
    description: Surfaces deprecation across paths so reviewers can plan removal.

risk:
  compliance:
    - SOC 2 CC8.1 — change-management communications to stakeholders
    - ISO/IEC 27001 A.14 — system acquisition, development, and maintenance lifecycle controls
  security_implications: Long-tail use of deprecated endpoints accumulates known vulnerabilities and unsupported authentication patterns. A clear policy with Sunset + Deprecation headers, telemetry on deprecated traffic, and a documented removal date reduces lingering attack surface.

tools:
  - name: Spectral
    url: https://github.com/stoplightio/spectral
    license: Apache-2.0
    category: Linter
  - name: oasdiff
    url: https://github.com/oasdiff/oasdiff
    license: Apache-2.0
    category: Diff / breaking-change detector
  - name: openapi-diff (Tufin)
    url: https://github.com/Tufin/oasdiff
    category: Diff
  - name: optic
    url: https://github.com/opticdev/optic
    license: MIT
    category: Change tracking

metrics:
  - name: deprecated_endpoint_traffic
    description: Share of traffic still hitting deprecated operations; informs sunset readiness.
  - name: time_to_sunset_days
    description: Days remaining between current date and the announced sunset for each deprecated resource.
  - name: migration_completion_rate
    description: Fraction of clients/integrations that have moved to the successor version.
  - name: sunset_header_coverage
    description: Share of deprecated responses that carry the Sunset header.

examples:
  - provider: GitHub
    url: https://providers.apis.io/providers/github/
    note: API version sunset announced via headers and the changelog.
  - provider: Stripe
    url: https://providers.apis.io/providers/stripe/
    note: Versioned API with documented behaviour changes and long-tail support.
  - provider: Google
    url: https://providers.apis.io/providers/google/
    note: API deprecation schedule with minimum support windows per product.
  - provider: Microsoft Graph
    url: https://providers.apis.io/providers/microsoft-graph/
    note: Beta-to-v1.0 promotion path with deprecation announcements.

related_properties:
  - versioning
  - lifecycle
  - change-log
  - road-map
  - status-page
---
