---
name: OpenAPI Response Put 404 Schema Ref Error
description: >-
  PUT 404 not found HTTP status codes have a schema references to standardize
  the response payload returned for the error response
message: PUT 404 Responses MUST Use Schema Reference
given: $.paths.*.put.responses.404
severity: error
tags:
  - OpenAPI
  - Responses
  - PUT
  - 4xx
  - Schema
view_sort: I
guidance: Errors
guidanceUrl: https://guidance.apievangelist.com/errors
rule:
  openapi-response-put-404-schema-ref-error:
    description: >-
      PUT 404 not found HTTP status codes have a schema references to
      standardize the response payload returned for the error response
    message: PUT 404 Responses MUST Use Schema Reference
    severity: error
    given: $.paths.*.put.responses.404
    then:
      field: $ref
      function: falsy
slug: openapi-response-put-404-schema-ref-error
---