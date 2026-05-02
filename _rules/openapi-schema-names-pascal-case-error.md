---
name: OpenAPI Schema Names Pascal Case Error
description: >-
  Schema names are pascal case, keeping the naming of them consistent across
  APIs, standardizing how consumers can use in their applications
message: Schema Names MUST Be PascalCase.
given: $.components.schemas
severity: error
tags:
  - OpenAPI
  - Schema
  - Metadata
view_sort: A
guidance: Descriptions
guidanceUrl: https://guidance.apievangelist.com/descriptions
rule:
  openapi-schema-names-pascal-case-error:
    description: >-
      Schema names are pascal case, keeping the naming of them consistent across
      APIs, standardizing how consumers can use in their applications
    message: Schema Names MUST Be PascalCase.
    severity: error
    given: $.components.schemas
    then:
      - field: '@key'
        function: pattern
        functionOptions:
          match: ^[A-Z](([a-z]+[A-Z]?)*)$
      - field: '@key'
        function: pattern
        functionOptions:
          match: ^[A-Z](([a-z0-9]+[A-Z]?)*)$
slug: openapi-schema-names-pascal-case-error
---