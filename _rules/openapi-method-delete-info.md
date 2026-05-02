---
name: OpenAPI Method DELETE Info
description: >-
  DELETE HTTP methods should be available.
message: DELETE Request Body
given: $.paths.*
severity: info
tags:
  - OpenAPI
  - Request Bodies
  - DELETE  
view_sort: A
guidance: Standards
guidanceUrl: https://guidance.apievangelist.com/standards
rule:
  openapi-method-delete-info:
    description: >-
      DELETE HTTP methods should be available.
    message: DELETE Request Body
    given: $.paths.*
    severity: info
    then:
      field: '@key'
      function: pattern
      functionOptions:
        match: ^\b(DELETE|delete)\b
slug: openapi-method-delete-info
---