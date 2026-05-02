---
name: OpenAPI Response Post 500 Schema Ref Error
description: >-
  POST 500 internal server error requests HTTP status codes have a schema
  references to standardize the response payload returned for the error response
message: POST 500 Responses MUST Use Schema Reference
given: $.paths.*.post.responses.500
severity: error
tags:
  - OpenAPI
  - Responses
  - POST
  - 5xx
  - Schema
view_sort: U
guidance: Errors
guidanceUrl: https://guidance.apievangelist.com/errors
rule:
  openapi-response-post-500-schema-ref-error:
    description: >-
      POST 500 internal server error requests HTTP status codes have a schema
      references to standardize the response payload returned for the error
      response
    message: POST 500 Responses MUST Use Schema Reference
    severity: error
    given: $.paths.*.post.responses.500
    then:
      field: $ref
      function: falsy
slug: openapi-response-post-500-schema-ref-error
---