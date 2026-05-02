---
slug: openapi-schema-names-snake-case-info
icon: type
name: OpenAPI Schema Names Snake Case
description: >-
  Schema component keys should use snake_case naming convention for consistency, particularly in APIs that follow Python or Ruby conventions.
message: Schema key SHOULD be snake_case.
given: $.components.schemas.*~
severity: info
view_sort: B
tags:
  - OpenAPI
  - Schema
  - Naming
  - Casing
guidance: Descriptions
guidanceUrl: https://guidance.apievangelist.com/descriptions
rule:
  openapi-schema-names-snake-case-info:
    description: >-
      Schema component keys should use snake_case naming convention for consistency, particularly in APIs that follow Python or Ruby conventions.
    message: Schema key SHOULD be snake_case.
    given: $.components.schemas.*~
    severity: info
    then:
      function: pattern
      functionOptions:
        match: "^[a-z][a-z0-9]*(_[a-z0-9]+)*$"
---
