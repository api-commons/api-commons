---
name: OpenAPI Response Get 401 Schema Ref Error
description: >-
  GET 401 unauthorized HTTP status codes have a schema references to standardize
  the response payload returned for the error response
message: GET 401 Responses MUST Use Schema Reference
given: $.paths.*.get.responses.401
severity: error
tags:
  - OpenAPI
  - Responses
  - GET
  - 4xx
  - Schema
view_sort: K
guidance: Errors
guidanceUrl: https://guidance.apievangelist.com/errors
rule:
  openapi-response-get-401-schema-ref-error:
    description: >-
      GET 401 unauthorized HTTP status codes have a schema references to
      standardize the response payload returned for the error response
    message: GET 401 Responses MUST Use Schema Reference
    severity: error
    given: $.paths.*.get.responses.401
    then:
      field: $ref
      function: falsy
slug: openapi-response-get-401-schema-ref-error
---