---
name: JSON Schema Draft 2020-12 Schema Draft Error
description: The $schema property in a JSON Schema MUST always reference the latest draft of the specification to ensure consistent validation across all objects. Using the most up-to-date version of the specification helps maintain stability and reliability in the use of objects within any API.
slug: json-schema-2020-12-schema-draft-error
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
  - Changes
view_sort: D
rule:
  json-schema-2020-12-schema-draft-error:
    description: The $schema property in a JSON Schema MUST always reference the latest draft of the specification to ensure consistent validation across all objects. Using the most up-to-date version of the specification helps maintain stability and reliability in the use of objects within any API.
    given: $
    severity: error
    then:
      field: "$schema"
      function: pattern
      functionOptions:
        match: 'https://json-schema.org/draft/2020-12/schema'
---