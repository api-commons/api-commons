---
name: OpenAPI Method POST Error
description: >-
  POST HTTP methods should be available.
message: POST Request Body
given: $.paths.*
severity: info
tags:
  - OpenAPI
  - Request Bodies
  - POST  
view_sort: A
guidance: Standards
guidanceUrl: https://guidance.apievangelist.com/standards
rule:
  openapi-method-post-error:
    description: >-
      POST HTTP methods should be available.
    message: POST Request Body
    given: $.paths.*
    severity: info
    then:
      field: '@key'
      function: pattern
      functionOptions:
        notMatch: ^\b(POST|post)\b
slug: openapi-method-post-error
---