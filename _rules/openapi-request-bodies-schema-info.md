---
name: OpenAPI Request Body Have Schema Info
description: >-
  POST, PUT, and PATCH request bodies should have schema defined, providing more
  detail on what the structure of the API request body should be
message: Request Body Schema
given: $.paths.*.*.requestBody.content.*
severity: info
tags:
  - OpenAPI
  - Request Bodies
  - Schema  
view_sort: M
guidance: OpenAPI
guidanceUrl: https://guidance.apievangelist.com/openapi
rule:
  openapi-request-bodies-schema-info:
    description: >-
      POST, PUT, and PATCH request bodies should have schema defined, providing
      more detail on what the structure of the API request body should be
    message: Request Body Schema
    given: $.paths.*.*.requestBody.content.*
    severity: info
    then:
      field: schema
      function: falsy
slug: openapi-request-bodies-schema-info
---