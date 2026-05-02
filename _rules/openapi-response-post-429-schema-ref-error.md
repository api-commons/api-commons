---
name: OpenAPI Response Post 429 Schema Ref Error
description: >-
  POST 429 too many requests HTTP status codes have a schema references to
  standardize the response payload returned for the error response
message: POST 429 Responses MUST Use Schema Reference
given: $.paths.*.post.responses.429
severity: error
tags:
  - OpenAPI
  - Responses
  - POST
  - 4xx
  - Schema
view_sort: S
guidance: Errors
guidanceUrl: https://guidance.apievangelist.com/errors
rule:
  openapi-response-post-429-schema-ref-error:
    description: >-
      POST 429 too many requests HTTP status codes have a schema references to
      standardize the response payload returned for the error response
    message: POST 429 Responses MUST Use Schema Reference
    severity: error
    given: $.paths.*.post.responses.429
    then:
      field: $ref
      function: falsy
slug: openapi-response-post-429-schema-ref-error
---