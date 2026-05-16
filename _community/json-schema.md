---
name: JSONSchema
description: The JSON Schema allows for the validation of JSON objects, and is used by OpenAPI & AsyncAPI. JSON Schema is a fundamental building block of the enterprise, and is ubiquitous across operations, whether teams are aware of it or not. JSON Schema is essential to standardizing and streamlining API operations across REST, GraphQL, and event-driven APis.
image: /images/json-schema.png
url: https://www.json-schema.org/
machineReadable: true
source: community
tags:
  - Machine-Readable
  - Schema
  - Validation
aliases:
  - JSON Schema
  - JSON Schema Draft

standards:
  - name: JSON Schema Draft 2020-12 (Core)
    url: https://json-schema.org/draft/2020-12/json-schema-core
    kind: IETF (JSON Schema WG)
  - name: JSON Schema Draft 2020-12 (Validation)
    url: https://json-schema.org/draft/2020-12/json-schema-validation
    kind: IETF (JSON Schema WG)
  - name: JSON Schema Draft 2019-09
    url: https://json-schema.org/draft/2019-09/release-notes
    kind: IETF (JSON Schema WG)
  - name: JSON Schema Draft 07
    url: https://json-schema.org/draft-07/schema
    kind: IETF (JSON Schema WG)
  - name: JSON Hyper-Schema (Draft 2019-09)
    url: https://json-schema.org/draft/2019-09/json-schema-hypermedia
    kind: IETF (JSON Schema WG)
  - name: RFC 8259 — JSON
    url: https://www.rfc-editor.org/rfc/rfc8259
    kind: IETF
  - name: RFC 6901 — JSON Pointer
    url: https://www.rfc-editor.org/rfc/rfc6901
    kind: IETF
  - name: RFC 6902 — JSON Patch
    url: https://www.rfc-editor.org/rfc/rfc6902
    kind: IETF
  - name: OpenAPI 3.1 (full alignment with JSON Schema 2020-12)
    url: https://spec.openapis.org/oas/v3.1.0
    kind: OpenAPI Initiative

media_types:
  - type: application/schema+json
    note: Proposed media type for JSON Schema documents.
  - type: application/schema-instance+json
    note: Proposed media type for instances validated by a JSON Schema.
  - type: application/json
    note: Default transport for both schemas and instances.

headers:
  - name: Content-Type
    direction: response
    spec: RFC 9110
    description: May carry application/schema+json for a schema document, or application/json with a Link header pointing to one for instances.
  - name: Link
    direction: response
    spec: RFC 8288
    description: Carries a describedby relation pointing to the JSON Schema for the response body.

link_relations:
  - rel: describedby
    spec: RFC 8288
    note: Associates an instance document with its JSON Schema.
  - rel: profile
    spec: RFC 6906
    note: Identifies the schema/profile an instance conforms to.

openapi_expression:
  - field: components.schemas
    spec: OpenAPI 3.x
    description: Reusable schema definitions; OAS 3.1 uses JSON Schema 2020-12 vocabulary, OAS 3.0 uses a subset.
  - field: schema
    spec: OpenAPI 3.x
    description: Inline schema on a parameter, request body, response, or header.
  - field: $schema
    spec: JSON Schema 2020-12
    description: Optional dialect identifier supported in OAS 3.1 schemas.
  - field: $ref
    spec: JSON Schema / OAS
    description: Reference to another schema by URI.

governance_rules:
  - id: oas3-valid-media-example
    source: Spectral built-in
    description: Example values must validate against the declared schema.
  - id: oas3-schema
    source: Spectral built-in
    description: Inline schemas must validate against the JSON Schema dialect declared by the OAS version.
  - id: no-$ref-siblings
    source: Spectral built-in
    description: Properties alongside $ref are ignored in OAS 3.0 (allowed in 3.1 / JSON Schema 2020-12).

risk:
  owasp:
    - 'OWASP API Security Top 10: API6:2023 Unrestricted Access to Sensitive Business Flows — missing schemas allow over-posting / mass assignment'
    - 'OWASP API Security Top 10: API3:2023 Broken Object Property Level Authorization — schemas without additionalProperties:false leak fields'
  compliance:
    - PCI DSS v4 Req. 6.2 — input validation against documented contracts
    - HIPAA 45 CFR §164.312(c)(1) — integrity controls require validated data shapes
    - GDPR Art. 5 — data minimization benefits from explicit schemas
  security_implications: Loose schemas (no additionalProperties:false, missing format/pattern, unbounded strings/arrays) cause injection, ReDoS, and mass-assignment bugs. Pin a $schema dialect, validate at the edge, and fail closed on unknown properties.

tools:
  - name: Ajv
    url: https://ajv.js.org/
    license: MIT
    category: Validator (JS)
  - name: jsonschema (Python)
    url: https://python-jsonschema.readthedocs.io/
    license: MIT
    category: Validator (Python)
  - name: JSON Schema Store
    url: https://www.schemastore.org/
    license: Apache-2.0
    category: Registry of schemas
  - name: quicktype
    url: https://quicktype.io/
    license: Apache-2.0
    category: Schema-to-type codegen
  - name: json-schema-faker
    url: https://github.com/json-schema-faker/json-schema-faker
    license: MIT
    category: Mock data generator
  - name: Hyperjump JSV
    url: https://json-schema.hyperjump.io/
    license: MIT
    category: Validator / playground

metrics:
  - name: schema_validation_failure_rate
    description: Share of requests/responses rejected by schema validation at the edge.
  - name: schema_coverage
    description: Share of API operations whose request and response bodies have a defined schema.
  - name: schema_strictness_score
    description: Composite score for additionalProperties:false, required arrays, and bounded types.
  - name: schema_drift_events
    description: Count of breaking changes detected between schema versions.

examples:
  - provider: Stripe
    url: https://providers.apis.io/providers/stripe/
    note: JSON Schema embedded inside the OpenAPI document for every object.
  - provider: GitHub
    url: https://providers.apis.io/providers/github/
    note: REST API description uses JSON Schema throughout; webhook payloads also schema-described.
  - provider: Kubernetes
    url: https://providers.apis.io/providers/kubernetes/
    note: OpenAPI / CRD schemas drive validation and codegen across the ecosystem.

related_properties:
  - openapi
  - asyncapi
  - graphql-schema
  - webhooks
---
