---
name: OpenAPI Parameters Componentized Info
description: >-
  Having all parameters using the central OpenAPI components parameters object
  helps increase the reusability of parameters across API operations, but it
  also help standardize parameter across all APIs
message: Parameters use components $ref.
given: $.paths.*.*.parameters.*
severity: info
tags:
  - OpenAPI
  - Components
  - Parameters
view_sort: A   
guidance: OpenAPI
guidanceUrl: https://guidance.apievangelist.com/openapi
rule:
  openapi-parameters-componentized-info:
    description: >-
      Having all parameters using the central OpenAPI components parameters
      object helps increase the reusability of parameters across API operations,
      but it also help standardize parameter across all APIs
    message: Parameters use components $ref.
    severity: info
    resolved: false
    given: $.paths.*.*.parameters.*
    then:
      field: $ref
      function: falsy
slug: openapi-parameters-componentized-info
---