---
name: OpenAPI Response Post 400 Schema Ref Error
description: >-
  POST 400 bad request HTTP status codes have a schema references to standardize
  the response payload returned for the error response
message: POST 400 Responses MUST Use Schema Reference
given: $.paths.*.post.responses.400
severity: error
tags:
  - OpenAPI
  - Responses
  - POST
  - 4xx
  - Schema
view_sort: K
guidance: Errors
guidanceUrl: https://guidance.apievangelist.com/errors
rule:
  openapi-response-post-400-schema-ref-error:
    description: >-
      POST 400 bad request HTTP status codes have a schema references to
      standardize the response payload returned for the error response
    message: POST 400 Responses MUST Use Schema Reference
    severity: error
    given: $.paths.*.post.responses.400
    then:
      field: $ref
      function: falsy
slug: openapi-response-post-400-schema-ref-error
---