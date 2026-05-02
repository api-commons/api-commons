---
name: JSON Schema Draft 2020-12 Properties Names Camel Case Info
description: >-
  Schema property names are camel case, providing consistent casing across all
  the schema properties used by APIs
message: Schema Property Names Are camelCase.
given: $properties
severity: info
tags:
  - JSON Schema
  - Schema
  - Properties
  - Metadata
view_sort: B
guidance: Descriptions
guidanceUrl: https://guidance.apievangelist.com/descriptions
rule:
  json-schema-2020-12-properties-names-camel-case-info:
    description: >-
      Schema property names are camel case, providing consistent casing across
      all the schema properties used by APIs
    message: Schema Property Names Are camelCase.
    severity: info
    given: $properties
    then:
      - field: '@key'
        function: pattern
        functionOptions:
          match: ^[A-Z][a-z0-9]*[A-Z0-9][a-z0-9]+[A-Za-z0-9]*$
slug: json-schema-2020-12-properties-names-camel-case-info
---