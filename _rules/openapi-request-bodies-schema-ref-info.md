---
name: OpenAPI Request Body Have Schema Ref Info
description: >-
  POST, PUT, and PATCH request bodies should have schema reference defined,
  providing more detail on what the structure of the API request body should be
message: Request Bodies Use Schema Reference
given: $.paths.*.*.requestBody.content.*.schema
severity: info
tags:
  - OpenAPI
  - Request Bodies
  - Schema  
view_sort: N
guidance: OpenAPI
guidanceUrl: https://guidance.apievangelist.com/openapi
rule:
  openapi-request-bodies-schema-ref-info:
    description: >-
      POST, PUT, and PATCH request bodies should have schema reference defined,
      providing more detail on what the structure of the API request body should
      be
    message: Request Bodies Use Schema Reference
    severity: info
    given: $.paths.*.*.requestBody.content.*.schema
    then:
      field: $ref
      function: truthy
slug: openapi-request-bodies-schema-ref-info
---