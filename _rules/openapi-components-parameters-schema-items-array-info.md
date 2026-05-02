---
name: OpenAPI Components Parameters Schema Items Array Info
description: >-
  Parameters that are of an array type should always have the items defined,
  being explicit about what is continued as part of the array
message: Parameter Schema Array MUST Has Items
given: $.components.parameters.schema[?(@.type=='array')]
severity: info
tags:
  - OpenAPI
  - Components
  - Parameters
  - Schema  
  - Type
  - Default
  - Security
view_sort: M
guidance: OpenAPI
guidanceUrl: https://guidance.apievangelist.com/openapi
rule:
  openapi-components-parameters-schema-items-array-info:
    description: >-
      Parameters that are of an array type should always have the items defined,
      being explicit about what is continued as part of the array
    message: Parameter Schema Array MUST Has Items
    severity: info
    given: $.components.parameters.schema[?(@.type=='array')]
    then:
      field: items
      function: falsy
slug: openapi-components-parameters-schema-items-array-info
---