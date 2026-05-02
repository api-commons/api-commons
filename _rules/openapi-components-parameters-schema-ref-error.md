---
name: OpenAPI Components Parameters Schema Ref Error
description: >-
  Parameters must always use a schema reference that utilizes reusable schema
  that are defined as part of a centralized schema components library
message: Parameters MUST Use Schema Reference
given: $.components.parameters.*.schema
severity: error
tags:
  - OpenAPI
  - Components
  - Parameters
  - Schema
  - Default
view_sort: G  
guidance: OpenAPI
guidanceUrl: https://guidance.apievangelist.com/openapi
rule:
  openapi-components-parameters-schema-ref-error:
    description: >-
      Parameters must always use a schema reference that utilizes reusable
      schema that are defined as part of a centralized schema components library
    message: Parameters MUST Use Schema Reference
    severity: error
    given: $.components.parameters.*.schema
    then:
      field: $ref
      function: falsy
slug: openapi-components-parameters-schema-ref-error
---