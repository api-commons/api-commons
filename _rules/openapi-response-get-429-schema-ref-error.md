---
name: OpenAPI Response Get 429 Schema Ref Error
description: >-
  GET 429 too many requests HTTP status codes have a schema references to
  standardize the response payload returned for the error response
message: GET 429 Responses MUST Use Schema Reference
given: $.paths.*.get.responses.429
severity: error
tags:
  - OpenAPI
  - Responses
  - GET
  - 4xx
  - Schema
view_sort: Q
guidance: Errors
guidanceUrl: https://guidance.apievangelist.com/errors
rule:
  openapi-response-get-429-schema-ref-error:
    description: >-
      GET 429 too many requests HTTP status codes have a schema references to
      standardize the response payload returned for the error response
    message: GET 429 Responses MUST Use Schema Reference
    severity: error
    given: $.paths.*.get.responses.429
    then:
      field: $ref
      function: falsy
slug: openapi-response-get-429-schema-ref-error
---