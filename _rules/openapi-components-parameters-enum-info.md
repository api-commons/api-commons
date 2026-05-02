---
name: OpenAPI Components Parameters Enum Info
description: >-
  Providing enums for your parameters helps reduce errors and keeps the inputs
  for your API requests more consistent for consumers
message: Parameters Have Enum
given: $.components.parameters.*
severity: info
tags:
  - OpenAPI
  - Components
  - Parameters
  - Enumerators  
  - Type
view_sort: N
guidance: OpenAPI
guidanceUrl: https://guidance.apievangelist.com/openapi
rule:
  openapi-components-parameters-enum-info:
    description: >-
      Providing enums for your parameters helps reduce errors and keeps the
      inputs for your API requests more consistent for consumers
    message: Parameters Have Enum
    severity: info
    given: $.components.parameters.*
    then:
      field: enum
      function: falsy
slug: openapi-components-parameters-enum-info
---