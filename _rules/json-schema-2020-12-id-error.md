---
name: JSON Schema Draft 2020-12 ID Error
description: Each JSON Schema object MUST have a unique identifier, represented as a URL pointing to its location. The $id property in JSON Schema is used to establish the source of truth for any object being defined and validated.
slug: json-schema-2020-12-id-error
engine: Unknown
specification: Unknown
specificationUrl: https://example.com
guidance: API Evangelist
guidanceUrl: https://guidance.apievangelist.com
severity: error
type: Default
tags:
  - JSON Schema
  - Metadata
  - Identifiers
view_sort: A
rule:
  json-schema-2020-12-id-error:
    description: Each JSON Schema object MUST have a unique identifier, represented as a URL pointing to its location. The $id property in JSON Schema is used to establish the source of truth for any object being defined and validated.
    given: $
    severity: error
    then:
      field: "$id"
      function: truthy
---