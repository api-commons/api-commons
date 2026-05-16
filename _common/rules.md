---
name: Rules
description: Providing an index of the machine-readable rules available for governing APIs, offering rules for linting API operations, as well as the surface area of each API, helping standardize how APIs are design, but also delivered across teams within an enterprise.
image: /images/rules.png
url: '#'
machineReadable: false
source: concept
tags:
  - Rules 
  - Spectral
  - Governance
  - Technical
  - Engineering
  - Linting
aliases:
  - Linting Rules
  - Style Rules
  - Governance Rules
  - Rulesets
yaml_example: |
  - type: SpectralRules
    url: https://developers.example.com/.spectral.yaml
    mediaType: application/yaml

standards:
  - name: OpenAPI Specification 3.1
    url: https://spec.openapis.org/oas/v3.1.0
    kind: OpenAPI Initiative
  - name: AsyncAPI Specification
    url: https://www.asyncapi.com/docs/reference/specification/latest
    kind: AsyncAPI Initiative
  - name: JSON Schema 2020-12
    url: https://json-schema.org/specification-links#2020-12
    kind: JSON Schema
  - name: RFC 9535 — JSONPath
    url: https://www.rfc-editor.org/rfc/rfc9535
    kind: IETF
  - name: Spectral built-in ruleset — spectral:oas
    url: https://docs.stoplight.io/docs/spectral/4dec24461f3af-open-api-rules
    kind: Stoplight
  - name: Spectral built-in ruleset — spectral:asyncapi
    url: https://docs.stoplight.io/docs/spectral/asyncapi-rules
    kind: Stoplight
  - name: Spectral custom rulesets
    url: https://docs.stoplight.io/docs/spectral/01baf06bdd05a-create-a-ruleset
    kind: Stoplight

media_types:
  - type: application/yaml
    note: Spectral, Redocly, and Vacuum rulesets are typically authored as YAML.
  - type: application/json
    note: Rulesets and JSON Schema documents.
  - type: text/x-javascript
    note: Spectral custom functions and rulesets authored as ES modules.

openapi_expression:
  - field: x-spectral-ruleset
    spec: Vendor extension (de facto)
    description: Points to a Spectral ruleset that governs the API description.
  - field: info.x-api-governance
    spec: Vendor extension
    description: Custom marker linking a description to its governance ruleset.

governance_rules:
  - id: oas3-api-servers
    source: Spectral built-in (spectral:oas)
    description: OpenAPI 3.x descriptions must define a servers array.
  - id: operation-operationId
    source: Spectral built-in (spectral:oas)
    description: Every operation must have an operationId.
  - id: operation-tag-defined
    source: Spectral built-in (spectral:oas)
    description: Operation tags must be defined in the global tags array.
  - id: no-$ref-siblings
    source: Spectral built-in (spectral:oas)
    description: $ref must not have sibling properties (OAS 3.0).
  - id: info-contact
    source: Spectral built-in (spectral:oas)
    description: info.contact is required so consumers can reach the producer.

risk:
  security_implications: Weak or absent linting rules let security-sensitive defects (missing security schemes, undefined responses, leaked debug servers) ship to production. Pair lint rules with CI gates and treat rule changes as audited governance artifacts.
  governance: Inconsistent rule enforcement across teams produces drift between API descriptions, breaking generated SDKs, mocks, and gateway configuration.

tools:
  - name: Spectral
    url: https://github.com/stoplightio/spectral
    license: Apache-2.0
    category: Linter
  - name: Vacuum
    url: https://quobix.com/vacuum/
    license: MIT
    category: Linter (Go, Spectral-compatible)
  - name: Optic
    url: https://www.useoptic.com/
    category: API diff and governance
  - name: Redocly CLI lint
    url: https://redocly.com/docs/cli/commands/lint
    category: Linter
  - name: AJV
    url: https://ajv.js.org/
    license: MIT
    category: JSON Schema validator
  - name: JSONPath Plus
    url: https://github.com/JSONPath-Plus/JSONPath
    license: MIT
    category: JSONPath engine (Spectral default)

metrics:
  - name: rule_violation_count
    description: Number of rule violations per lint run, broken down by severity.
  - name: lint_pass_rate
    description: Share of CI runs whose API description passes the active ruleset without errors.
  - name: ruleset_version_drift
    description: Number of repositories pinned to an outdated central ruleset.
  - name: time_to_fix_violation_p50
    description: Median time between a rule violation being reported and its resolution.

examples:
  - provider: Stoplight
    url: https://providers.apis.io/providers/stoplight/
    note: Reference implementation of Spectral and the spectral:oas / spectral:asyncapi rulesets.
  - provider: Redocly
    url: https://providers.apis.io/providers/redocly/
    note: Redocly CLI lint with configurable OpenAPI rules and decorators.
  - provider: Postman
    url: https://providers.apis.io/providers/postman/
    note: API governance rules surfaced inside the Postman API platform.

related_properties:
  - policies
  - openapi
  - asyncapi
  - schema
  - tests
  - governance
---
