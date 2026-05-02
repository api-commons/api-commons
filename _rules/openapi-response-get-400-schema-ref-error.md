---
name: OpenAPI Response Get 400 Schema Ref Error
description: >-
  GET 400 bad request HTTP status codes have a schema references to standardize
  the response payload returned for the error response
message: GET 400 Responses MUST Use Schema Reference
given: $.paths.*.get.responses.400
severity: error
tags:
  - OpenAPI
  - Responses
  - GET
  - 4xx
  - Schema
view_sort: I
guidance: Errors
guidanceUrl: https://guidance.apievangelist.com/errors
rule:
  openapi-response-get-400-schema-ref-error:
    description: >-
      GET 400 bad request HTTP status codes have a schema references to
      standardize the response payload returned for the error response
    message: GET 400 Responses MUST Use Schema Reference
    severity: error
    given: $.paths.*.get.responses.400
    then:
      field: $ref
      function: falsy
slug: openapi-response-get-400-schema-ref-error
---