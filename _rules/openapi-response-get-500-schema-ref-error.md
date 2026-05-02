---
name: OpenAPI Response Get 500 Schema Ref Error
description: >-
  GET 500 internal server error requests HTTP status codes have a schema
  references to standardize the response payload returned for the error response
message: GET 500 Responses MUST Use Schema Reference
given: $.paths.*.get.responses.500
severity: error
tags:
  - OpenAPI
  - Responses
  - GET
  - 5xx
  - Schema
view_sort: S
guidance: Errors
guidanceUrl: https://guidance.apievangelist.com/errors
rule:
  openapi-response-get-500-schema-ref-error:
    description: >-
      GET 500 internal server error requests HTTP status codes have a schema
      references to standardize the response payload returned for the error
      response
    message: GET 500 Responses MUST Use Schema Reference
    severity: error
    given: $.paths.*.get.responses.500
    then:
      field: $ref
      function: falsy
slug: openapi-response-get-500-schema-ref-error
---