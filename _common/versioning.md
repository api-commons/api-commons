---
name: Versioning
description: The details of how an API is being versioned with information about how change is being communicated with consumers across multiple channels. Having a formal approach to versioning published and communicated helps lay the ground work for change, but also keeps API consumers aligned with what has changed.
image: /images/versioning.png
url: '#'
machineReadable: true
source: concept
tags:
  - Change
  - Versioning
  - Semantic
aliases:
  - API Versioning
  - SemVer
  - CalVer
yaml_example: |
  - name: Versioning
    type: Versioning
    url: https://developers.example.com/versioning
    source_date: '2026-08-17'
    data:
      scheme: sequential
      location: path
      path_pattern: /v{version}
      current: '3'
      default: '2'
      required: true
      pinning: per-request
      supported:
        - version: '2'
          status: deprecated
          sunset: '2027-02-01'
        - version: '3'
          status: current

standards:
  - name: API Commons Versioning schema
    url: https://github.com/api-commons/versioning
    kind: API Commons (Apache-2.0)
  - name: Semantic Versioning 2.0.0
    url: https://semver.org/spec/v2.0.0.html
    kind: Community spec
  - name: Calendar Versioning (CalVer)
    url: https://calver.org/
    kind: Community spec
  - name: RFC 9110 — HTTP Semantics (media-type parameters §8.3.2)
    url: https://www.rfc-editor.org/rfc/rfc9110
    kind: IETF
  - name: RFC 6838 — Media Type Specifications and Registration Procedures
    url: https://www.rfc-editor.org/rfc/rfc6838
    kind: IETF
  - name: RFC 7231 — HTTP/1.1 Semantics and Content (historic, content negotiation)
    url: https://www.rfc-editor.org/rfc/rfc7231
    kind: IETF (historic)
  - name: RFC 5829 — Link Relation Types for Simple Version Navigation
    url: https://www.rfc-editor.org/rfc/rfc5829
    kind: IETF
  - name: OpenAPI Specification (info.version)
    url: https://spec.openapis.org/oas/latest.html
    kind: OpenAPI Initiative
  - name: AsyncAPI Specification (info.version)
    url: https://www.asyncapi.com/docs/reference/specification/latest
    kind: AsyncAPI Initiative

headers:
  - name: Accept
    direction: request
    spec: RFC 9110 §12.5.1
    description: Used with versioned media types (e.g. application/vnd.example.v2+json) for content negotiation.
  - name: Content-Type
    direction: response
    spec: RFC 9110 §8.3
    description: Echoes the negotiated versioned media type.
  - name: API-Version
    direction: request / response
    spec: De facto
    description: Custom header used by some providers (e.g. Microsoft Graph, Stripe) to select an API version.

media_types:
  - type: application/vnd.<vendor>.v<n>+json
    spec: RFC 6838
    note: Vendor-tree media type with explicit version segment.
  - type: application/json; version=<n>
    spec: RFC 9110 §8.3.2
    note: Parameterised media type carrying a version parameter.

openapi_expression:
  - field: info.version
    spec: OpenAPI 3.x
    description: Free-form version string for the API document; SemVer or CalVer recommended.
  - field: servers[].url
    spec: OpenAPI 3.x
    description: URL-path versioning (e.g. /v1, /v2) is expressed in the server URL.
  - field: components.parameters
    spec: OpenAPI 3.x
    description: Header or query parameters can carry an api-version selector.

link_relations:
  - rel: latest-version
    spec: RFC 5829
  - rel: successor-version
    spec: RFC 5829
  - rel: predecessor-version
    spec: RFC 5829
  - rel: working-copy
    spec: RFC 5829
  - rel: working-copy-of
    spec: RFC 5829

governance_rules:
  - id: oas-info-version
    source: Spectral built-in
    description: info.version must be present and non-empty.
  - id: oas-semver
    source: Spectral built-in
    description: info.version should follow SemVer.
  - id: oas-path-not-include-query
    source: Spectral built-in
    description: Discourages query-string versioning embedded in path templates.

risk:
  compliance:
    - SOC 2 CC8.1 — change-management with traceable versions
    - ISO/IEC 27001 A.12.1.2 — change management
  security_implications: Ambiguous versioning lets clients pin to vulnerable behaviour or silently roll forward into untested code paths. Explicit, negotiated versions plus a published compatibility policy reduce regression-driven security incidents.

tools:
  - name: API Commons Versioning schema + validator
    url: https://github.com/api-commons/versioning
    license: Apache-2.0
    category: Machine-readable schema
  - name: oasdiff
    url: https://github.com/oasdiff/oasdiff
    license: Apache-2.0
    category: Breaking-change detector
  - name: openapi-diff (OpenAPI Tools)
    url: https://github.com/OpenAPITools/openapi-diff
    license: Apache-2.0
    category: Diff
  - name: optic
    url: https://github.com/opticdev/optic
    license: MIT
    category: Change tracking
  - name: semver (npm)
    url: https://github.com/npm/node-semver
    license: ISC
    category: Library
  - name: Spectral
    url: https://github.com/stoplightio/spectral
    license: Apache-2.0
    category: Linter

metrics:
  - name: active_versions
    description: Count of versions currently receiving production traffic.
  - name: version_adoption_share
    description: Traffic share per version; informs deprecation timing.
  - name: breaking_changes_per_release
    description: Number of breaking changes detected by oasdiff between consecutive releases.
  - name: time_in_version
    description: Median time clients stay on a major version before upgrading.

examples:
  - provider: GitHub
    url: https://providers.apis.io/providers/github/
    note: Media-type and X-GitHub-Api-Version header versioning (e.g. application/vnd.github.v3+json).
  - provider: Stripe
    url: https://providers.apis.io/providers/stripe/
    note: Date-based versions pinned per account, with Stripe-Version request header overrides.
  - provider: Microsoft Graph
    url: https://providers.apis.io/providers/microsoft-graph/
    note: URL-path versioning between v1.0 and beta.
  - provider: Twilio
    url: https://providers.apis.io/providers/twilio/
    note: Path-based versioning (/2010-04-01/) with CalVer-style identifiers.

related_properties:
  - deprecation-policy
  - lifecycle
  - change-log
  - road-map
  - error-codes
---
