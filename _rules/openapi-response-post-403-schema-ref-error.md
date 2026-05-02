---
name: OpenAPI Response Post 403 Schema Ref Error
description: >-
  POST 403 forbidden HTTP status codes have a schema references to standardize
  the response payload returned for the error response
message: POST 403 Responses MUST Use Schema Reference
given: $.paths.*.post.responses.403
severity: error
tags:
  - OpenAPI
  - Responses
  - POST
  - 4xx
  - Schema
view_sort: O
guidance: Errors
guidanceUrl: https://guidance.apievangelist.com/errors
rule:
  openapi-response-post-403-schema-ref-error:
    description: >-
      POST 403 forbidden HTTP status codes have a schema references to
      standardize the response payload returned for the error response
    message: POST 403 Responses MUST Use Schema Reference
    severity: error
    given: $.paths.*.post.responses.403
    then:
      field: $ref
      function: falsy
slug: openapi-response-post-403-schema-ref-error
---