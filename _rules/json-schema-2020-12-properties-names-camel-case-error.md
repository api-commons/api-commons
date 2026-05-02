---
name: JSON Schema Draft 2020-12 Properties Names Camel Case Error
description: >-
  Schema property names are camel case, providing consistent casing across all
  the schema properties used by APIs
message: Schema Property Names MUST Be camelCase.
given: $properties
severity: error
tags:
  - JSON Schema
  - Schema
  - Properties
  - Metadata
view_sort: B
guidance: Descriptions
guidanceUrl: https://guidance.apievangelist.com/descriptions
rule:
  json-schema-2020-12-properties-names-camel-case-error:
    description: >-
      Schema property names are camel case, providing consistent casing across
      all the schema properties used by APIs
    message: Schema Property Names MUST Be camelCase.
    severity: error
    given: $properties
    then:
      - field: '@key'
        function: pattern
        functionOptions:
          notMatch: ^[A-Z][a-z0-9]*[A-Z0-9][a-z0-9]+[A-Za-z0-9]*$
slug: json-schema-2020-12-properties-names-camel-case-error
---