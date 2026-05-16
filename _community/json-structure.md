---
name: JSON Structure
description: A complement to JSON Schema that describes the shape of resources in a way that is optimized for human comprehension and code-generation — what fields exist, how they relate, and what each is for — rather than for runtime validation. JSON Structure files sit alongside JSON Schema files in the same repository; the schema enforces correctness, the structure communicates intent. Together they form a richer picture of a resource than either provides alone.
image: /images/json-structure.png
url: '#'
machineReadable: true
source: community
tags:
  - Machine-Readable
  - Schema
  - Resources
aliases:
  - Structure
  - Resource Structure
yaml_example: |
  - type: JSONStructure
    url: json-structure/example-resource-structure.json

standards:
  - name: JSON Structure (community spec)
    url: https://jsonstructure.org/
    kind: Community
  - name: JSON Schema 2020-12
    url: https://json-schema.org/specification-links#2020-12
    kind: IETF (draft)
  - name: ECMA-404 — The JSON Data Interchange Syntax
    url: https://ecma-international.org/publications-and-standards/standards/ecma-404/
    kind: ECMA

media_types:
  - type: application/json
    note: JSON Structure files are typically served as application/json.

risk:
  security_implications: Structure documents describe the surface area of an API's resources in detail; treat them as you would JSON Schema or OpenAPI. Field names that suggest internal-only attributes (debug, internal_id, source_record) should be omitted from public structure documents, not just hidden behind authorization.

tools:
  - name: openapi-generator
    url: https://openapi-generator.tech/
    license: Apache-2.0
    category: Codegen — can consume structure-equivalent JSON
  - name: quicktype
    url: https://quicktype.io/
    license: Apache-2.0
    category: Generates types from JSON examples and schemas

metrics:
  - name: structure_coverage
    description: Share of resources in an API that have a published JSON Structure file.
  - name: structure_schema_parity
    description: Count of resources with a Structure file but no parallel JSON Schema (or vice versa).
  - name: structure_freshness_days
    description: Days since each Structure file was last updated against the resource it describes.

examples:
  - provider: API Evangelist catalogs
    url: https://apis.io/
    note: The api-evangelist provider catalog co-locates `json-structure/<slug>-structure.json` alongside `json-schema/<slug>-schema.json`, `examples/`, and `json-ld/` for each resource.

related_properties:
  - json-schema
  - openapi
  - asyncapi
  - vocabulary
---
