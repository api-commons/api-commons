---
name: Vocabulary
description: A controlled vocabulary or term set that an API's data references — the shared dictionary of codes, enums, and concepts that gives fields consistent meaning.
image: /images/schema.png
url: '#'
machineReadable: true
source: contracts
tags:
  - Vocabulary
  - Terms
  - Semantics
aliases:
  - Controlled Vocabulary
  - Terminology
  - Term Set
  - Code System
yaml_example: |
  - type: Vocabulary
    url: https://developers.example.com/vocabulary

standards:
  - name: API Anatomy — a shared vocabulary for the parts of an API
    url: https://github.com/APIPatterns/api-anatomy
    kind: Community (MIT, APIPatterns)
  - name: SKOS — Simple Knowledge Organization System
    url: https://www.w3.org/TR/skos-reference/
    kind: W3C Recommendation
  - name: JSON-LD 1.1
    url: https://www.w3.org/TR/json-ld11/
    kind: W3C Recommendation
  - name: schema.org
    url: https://schema.org/
    kind: Schema.org

openapi_expression:
  - field: components.schemas.{name}.enum
    spec: OpenAPI 3.x
    description: Where a controlled vocabulary usually surfaces in a description — as an inline enum with no pointer back to the term set that governs it.
  - field: components.schemas.{name}.x-vocabulary
    spec: Vendor extension
    description: Used to name the authoritative vocabulary an enum is drawn from, so consumers can resolve terms rather than hard-code them.
  - field: externalDocs
    spec: OpenAPI 3.x
    description: Can point at the published vocabulary backing the API's codes and terms.

related_properties:
  - json-ld
  - json-ld-context
  - json-schema
  - standards
  - data-contract
---
