---
name: OpenAPI Response Post 404 Schema Ref Error
description: >-
  POST 404 not found HTTP status codes have a schema references to standardize
  the response payload returned for the error response
message: POST 404 Responses MUST Use Schema Reference
given: $.paths.*.post.responses.404
severity: error
tags:
  - OpenAPI
  - Responses
  - POST
  - 4xx
  - Schema
view_sort: Q
guidance: Errors
guidanceUrl: https://guidance.apievangelist.com/errors
rule:
  openapi-response-post-404-schema-ref-error:
    description: >-
      POST 404 not found HTTP status codes have a schema references to
      standardize the response payload returned for the error response
    message: POST 404 Responses MUST Use Schema Reference
    severity: error
    given: $.paths.*.post.responses.404
    then:
      field: $ref
      function: falsy
slug: openapi-response-post-404-schema-ref-error
---