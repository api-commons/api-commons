---
name: OpenAPI Response Get 404 Schema Ref Error
description: >-
  GET 404 not found HTTP status codes have a schema references to standardize
  the response payload returned for the error response
message: GET 404 Responses MUST Use Schema Reference
given: $.paths.*.get.responses.404
severity: error
tags:
  - OpenAPI
  - Responses
  - GET
  - 4xx
  - Schema
view_sort: O
guidance: Errors
guidanceUrl: https://guidance.apievangelist.com/errors
rule:
  openapi-response-get-404-schema-ref-error:
    description: >-
      GET 404 not found HTTP status codes have a schema references to
      standardize the response payload returned for the error response
    message: GET 404 Responses MUST Use Schema Reference
    severity: error
    given: $.paths.*.get.responses.404
    then:
      field: $ref
      function: falsy
slug: openapi-response-get-404-schema-ref-error
---