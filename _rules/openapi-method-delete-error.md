---
name: OpenAPI Method DELETE Error
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
  openapi-method-delete-error:
    description: >-
      DELETE HTTP methods should be available.
    message: DELETE Request Body
    given: $.paths.*
    severity: info
    then:
      field: '@key'
      function: pattern
      functionOptions:
        notMatch: ^\b(DELETE|delete)\b
slug: openapi-method-delete-error
---