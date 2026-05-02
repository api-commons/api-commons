---
name: OpenAPI Method GET Error
description: >-
  GET HTTP methods should be available.
message: GET Request Body
given: $.paths.*
severity: info
tags:
  - OpenAPI
  - Request Bodies
  - GET  
view_sort: A
guidance: Standards
guidanceUrl: https://guidance.apievangelist.com/standards
rule:
  openapi-method-get-error:
    description: >-
      GET HTTP methods should be available.
    message: GET Request Body
    given: $.paths.*
    severity: info
    then:
      field: '@key'
      function: pattern
      functionOptions:
        notMatch: ^\b(GET|get)\b
slug: openapi-method-get-error
---