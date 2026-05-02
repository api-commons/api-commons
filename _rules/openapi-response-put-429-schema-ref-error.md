---
name: OpenAPI Response Put 429 Schema Ref Error
description: >-
  PUT 429 too many requests HTTP status codes have a schema references to
  standardize the response payload returned for the error response
message: PUT 429 Responses MUST Use Schema Reference
given: $.paths.*.put.responses.429
severity: error
tags:
  - OpenAPI
  - Responses
  - PUT
  - 4xx
  - Schema
view_sort: K
guidance: Errors
guidanceUrl: https://guidance.apievangelist.com/errors
rule:
  openapi-response-put-429-schema-ref-error:
    description: >-
      PUT 429 too many requests HTTP status codes have a schema references to
      standardize the response payload returned for the error response
    message: PUT 429 Responses MUST Use Schema Reference
    severity: error
    given: $.paths.*.put.responses.429
    then:
      field: $ref
      function: falsy
slug: openapi-response-put-429-schema-ref-error
---