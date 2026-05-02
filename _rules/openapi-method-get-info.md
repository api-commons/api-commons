---
name: OpenAPI Method GET Info
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
  openapi-method-get-info:
    description: >-
      GET HTTP methods should be available.
    message: GET Request Body
    given: $.paths.*
    severity: info
    then:
      field: '@key'
      function: pattern
      functionOptions:
        match: ^\b(GET|get)\b
slug: openapi-method-get-info
---