---
name: OpenAPI Schema Properties Names Camel Case Info
description: >-
  Schema property names are camel case, providing consistent casing across all
  the schema properties used by APIs
message: Schema Property Names Are camelCase.
given: $.components.schemas.*.properties
severity: info
tags:
  - OpenAPI
  - Schema
  - Properties
  - Metadata
  - Default
view_sort: B
guidance: Descriptions
guidanceUrl: https://guidance.apievangelist.com/descriptions
rule:
  openapi-schema-properties-names-camel-case-info:
    description: >-
      Schema property names are camel case, providing consistent casing across
      all the schema properties used by APIs
    message: Schema Property Names Are camelCase.
    severity: info
    given: $.components.schemas.*.properties
    then:
      - field: '@key'
        function: pattern
        functionOptions:
          match: ^[A-Z][a-z0-9]*[A-Z0-9][a-z0-9]+[A-Za-z0-9]*$
slug: openapi-schema-properties-names-camel-case-info
---