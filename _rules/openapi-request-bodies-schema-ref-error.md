---
name: OpenAPI Request Body Have Schema Ref Error
description: >-
  POST, PUT, and PATCH request bodies should have schema reference defined,
  providing more detail on what the structure of the API request body should be
message: Request Bodies MUST Use Schema Reference
given: $.paths.*.*.requestBody.content.*.schema
severity: error
tags:
  - OpenAPI
  - Request Bodies
  - Schema  
view_sort: N
guidance: OpenAPI
guidanceUrl: https://guidance.apievangelist.com/openapi
rule:
  openapi-request-bodies-schema-ref-error:
    description: >-
      POST, PUT, and PATCH request bodies should have schema reference defined,
      providing more detail on what the structure of the API request body should
      be
    message: Request Bodies MUST Use Schema Reference
    severity: error
    given: $.paths.*.*.requestBody.content.*.schema
    then:
      field: $ref
      function: falsy
slug: openapi-request-bodies-schema-ref-error
---