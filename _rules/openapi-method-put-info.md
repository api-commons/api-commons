---
name: OpenAPI Method PUT Info
description: >-
  PUT HTTP methods should be available.
message: PUT Request Body
given: $.paths.*
severity: info
tags:
  - OpenAPI
  - Request Bodies
  - PUT  
view_sort: A
guidance: Standards
guidanceUrl: https://guidance.apievangelist.com/standards
rule:
  openapi-method-put-info:
    description: >-
      PUT HTTP methods should be available.
    message: PUT Request Body
    given: $.paths.*
    severity: info
    then:
      field: '@key'
      function: pattern
      functionOptions:
        match: ^\b(PUT|put)\b
slug: openapi-method-put-info
---