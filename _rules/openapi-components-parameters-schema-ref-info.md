---
name: OpenAPI Components Parameters Schema Ref Info
description: >-
  Parameters must always use a schema reference that utilizes reusable schema
  that are defined as part of a centralized schema components library
message: Parameters Use Schema Reference
given: $.components.parameters.*.schema
severity: info
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
  openapi-components-parameters-schema-ref-info:
    description: >-
      Parameters must always use a schema reference that utilizes reusable
      schema that are defined as part of a centralized schema components library
    message: Parameters Use Schema Reference
    severity: info
    given: $.components.parameters.*.schema
    then:
      field: $ref
      function: truthy
slug: openapi-components-parameters-schema-ref-info
---