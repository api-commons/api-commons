---
name: OpenAPI Response Put 400 Schema Ref Error
description: >-
  PUT 400 bad request HTTP status codes have a schema references to standardize
  the response payload returned for the error response
message: PUT 400 Responses MUST Use Schema Reference
given: $.paths.*.put.responses.400
severity: error
tags:
  - OpenAPI
  - Responses
  - PUT
  - 4xx
  - Schema
view_sort: C
guidance: Errors
guidanceUrl: https://guidance.apievangelist.com/errors
rule:
  openapi-response-put-400-schema-ref-error:
    description: >-
      PUT 400 bad request HTTP status codes have a schema references to
      standardize the response payload returned for the error response
    message: PUT 400 Responses MUST Use Schema Reference
    severity: error
    given: $.paths.*.put.responses.400
    then:
      field: $ref
      function: falsy
slug: openapi-response-put-400-schema-ref-error
---