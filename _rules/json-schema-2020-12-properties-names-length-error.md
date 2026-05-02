---
name: JSON Schema Draft 2020-12 Properties Names Length Error
description: >-
  Schema property names have a length restriction applied, keeping names
  consistent, and avoiding being too long
message: Schema Properties Name Length
given: $properties
severity: error
tags:
  - JSON Schema
  - Schema
  - Properties
  - Metadata
view_sort: BA
guidance: Descriptions
guidanceUrl: https://guidance.apievangelist.com/descriptions
rule:
  json-schema-2020-12-properties-names-length-error:
    description: >-
      Schema property names have a length restriction applied, keeping names
      consistent, and avoiding being too long
    message: Schema Properties Name Length
    severity: error
    given: $properties
    then:
      field: '@key'
      function: length
      functionOptions:
        max: 25
slug: json-schema-2020-12-properties-names-length-error
---