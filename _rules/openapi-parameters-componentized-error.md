---
name: OpenAPI Parameters Componentized Error
description: >-
  Having all parameters using the central OpenAPI components parameters object
  helps increase the reusability of parameters across API operations, but it
  also help standardize parameter across all APIs
message: Parameters MUST use components $ref.
given: $.paths.*.*.parameters.*
severity: error
tags:
  - OpenAPI
  - Components
  - Parameters
view_sort: A   
guidance: OpenAPI
guidanceUrl: https://guidance.apievangelist.com/openapi
rule:
  openapi-parameters-componentized-error:
    description: >-
      Having all parameters using the central OpenAPI components parameters
      object helps increase the reusability of parameters across API operations,
      but it also help standardize parameter across all APIs
    message: Parameters MUST use components $ref.
    severity: error
    resolved: false
    given: $.paths.*.*.parameters.*
    then:
      field: $ref
      function: truthy
slug: openapi-parameters-componentized-error
---