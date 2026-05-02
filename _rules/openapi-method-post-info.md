---
name: OpenAPI Method POST Info
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
  openapi-method-post-info:
    description: >-
      POST HTTP methods should be available.
    message: POST Request Body
    given: $.paths.*
    severity: info
    then:
      field: '@key'
      function: pattern
      functionOptions:
        match: ^\b(POST|post)\b
slug: openapi-method-post-info
---