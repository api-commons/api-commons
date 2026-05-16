---
name: OpenAPI
description: The OpenAPI Specification provides a formal standard for describing HTTP APIs, describing the surface area of request and response APIs. OpenAPI can be used to publish documentation, generate mock servers, and produce SDKs. An OpenAPI has become an expected artifact by API consumers and is widely considered to act as the technical contract between API produce and consumer and has become common for many leading API providers.
image: /images/openapi.png
url: https://www.openapis.org/
machineReadable: true
source: community
tags:
  - Machine-Readable
  - APIs
aliases:
  - OAS
  - OpenAPI Specification
  - Swagger (historical, pre-3.0)

standards:
  - name: OpenAPI Specification 3.1.0
    url: https://spec.openapis.org/oas/v3.1.0
    kind: OpenAPI Initiative (Linux Foundation)
  - name: OpenAPI Specification 3.0.4
    url: https://spec.openapis.org/oas/v3.0.4
    kind: OpenAPI Initiative (Linux Foundation)
  - name: Arazzo Specification 1.0.1
    url: https://spec.openapis.org/arazzo/v1.0.1
    kind: OpenAPI Initiative (Linux Foundation)
  - name: Overlay Specification 1.0
    url: https://spec.openapis.org/overlay/v1.0.0
    kind: OpenAPI Initiative (Linux Foundation)
  - name: JSON Schema Draft 2020-12 (aligned by OAS 3.1)
    url: https://json-schema.org/draft/2020-12
    kind: IETF (JSON Schema WG)
  - name: RFC 9727 — api-catalog Well-Known URI
    url: https://www.rfc-editor.org/rfc/rfc9727
    kind: IETF
  - name: RFC 8615 — Well-Known URIs
    url: https://www.rfc-editor.org/rfc/rfc8615
    kind: IETF

media_types:
  - type: application/vnd.oai.openapi
    note: IANA-registered for OpenAPI in YAML.
  - type: application/vnd.oai.openapi+json
    note: IANA-registered for OpenAPI in JSON.
  - type: application/json
    note: Common transport for OAS documents in JSON.
  - type: application/yaml
    note: Common transport for OAS documents in YAML.

well_known:
  - path: /.well-known/api-catalog
    spec: RFC 9727
    description: Linkset advertising API descriptions; entries typically use the service-desc relation.
  - path: /openapi.json
    spec: Convention (not IANA-registered)
    description: De facto path for an OpenAPI JSON document at the API root.
  - path: /openapi.yaml
    spec: Convention (not IANA-registered)
    description: De facto path for an OpenAPI YAML document at the API root.

link_relations:
  - rel: service-desc
    spec: RFC 8631
    note: Points to a machine-readable API description (commonly an OpenAPI document).
  - rel: service-doc
    spec: RFC 8631
    note: Points to human-readable API documentation generated from OpenAPI.
  - rel: describedby
    spec: RFC 8288
    note: Used to associate a resource with its schema.

openapi_expression:
  - field: openapi
    spec: OpenAPI 3.x
    description: Version string at the root of every document (e.g. "3.1.0").
  - field: info
    spec: OpenAPI 3.x
    description: API metadata — title, version, license, contact, summary.
  - field: servers
    spec: OpenAPI 3.x
  - field: paths
    spec: OpenAPI 3.x
  - field: webhooks
    spec: OpenAPI 3.1
    description: Top-level map of incoming webhook operations (new in 3.1).
  - field: components
    spec: OpenAPI 3.x
  - field: tags
    spec: OpenAPI 3.x

governance_rules:
  - id: oas3-schema
    source: Spectral built-in
    description: Document must validate against the OpenAPI 3.x JSON Schema.
  - id: operation-operationId
    source: Spectral built-in
    description: Every operation should have a unique operationId.
  - id: operation-tags
    source: Spectral built-in
    description: Operations should be tagged for discoverability.
  - id: info-contact
    source: Spectral built-in
    description: Info object should include a contact.
  - id: oas-tag-description
    source: Spectral built-in
    description: Each tag should carry a description.
  - id: no-$ref-siblings
    source: Spectral built-in
    description: Siblings of $ref are ignored in OAS 3.0 — flag them.

risk:
  owasp:
    - 'OWASP API Security Top 10: API9:2023 Improper Inventory Management — outdated or undocumented OAS leads to shadow/zombie endpoints'
    - 'OWASP API Security Top 10: API8:2023 Security Misconfiguration — OAS without security requirements masks unauthenticated endpoints'
  compliance:
    - SOC 2 CC8.1 — change management requires accurate API inventory
    - PCI DSS v4 Req. 6.2 — documented system components and interfaces
  security_implications: An incomplete or stale OpenAPI hides attack surface. Publish OAS as part of CI, validate that every deployed route is described, and never expose servers pointing at internal hosts. Treat the OAS itself as build-time governance input for gateways and WAFs.

tools:
  - name: Swagger Editor / UI
    url: https://swagger.io/tools/swagger-editor/
    license: Apache-2.0
    category: Editor / Renderer
  - name: Redocly CLI
    url: https://redocly.com/docs/cli/
    license: MIT
    category: Linter / Renderer
  - name: Spectral
    url: https://stoplight.io/open-source/spectral
    license: Apache-2.0
    category: Linter
  - name: openapi-generator
    url: https://openapi-generator.tech/
    license: Apache-2.0
    category: Codegen
  - name: Prism
    url: https://stoplight.io/open-source/prism
    license: Apache-2.0
    category: Mock server
  - name: Optic
    url: https://www.useoptic.com/
    category: Diff / governance

metrics:
  - name: oas_coverage
    description: Share of production endpoints described in an OpenAPI document.
  - name: oas_lint_violations
    description: Count of governance-rule violations across the document.
  - name: oas_breaking_changes
    description: Count of breaking changes detected between versions (e.g. via openapi-diff).
  - name: oas_freshness_days
    description: Days since the OpenAPI document was last regenerated or published.

examples:
  - provider: Stripe
    url: https://providers.apis.io/providers/stripe/
    note: Publishes an OpenAPI document at github.com/stripe/openapi.
  - provider: GitHub
    url: https://providers.apis.io/providers/github/
    note: Publishes the REST API description at github.com/github/rest-api-description.
  - provider: Twilio
    url: https://providers.apis.io/providers/twilio/
    note: Publishes per-product OAS at github.com/twilio/twilio-oai.
  - provider: DigitalOcean
    url: https://providers.apis.io/providers/digitalocean/
    note: Publishes OAS at github.com/digitalocean/openapi.

related_properties:
  - asyncapi
  - json-schema
  - webhooks
  - openapi-plugin-manifest
  - postman-collection
---
