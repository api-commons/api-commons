---
name: OpenAPI Response Delete 404 Schema Ref Error
description: >-
  DELETE 404 not found HTTP status codes have a schema references to standardize
  the response payload returned for the error response
message: DELETE 404 Responses MUST Use Schema Reference
given: $.paths.*.delete.responses.404
severity: error
tags:
  - OpenAPI
  - Responses
  - DELETE
  - 4xx
  - Default
view_sort: I
guidance: Errors
guidanceUrl: https://guidance.apievangelist.com/errors
rule:
  openapi-response-delete-404-schema-ref-error:
    description: >-
      DELETE 404 not found HTTP status codes have a schema references to
      standardize the response payload returned for the error response
    message: DELETE 404 Responses MUST Use Schema Reference
    severity: error
    given: $.paths.*.delete.responses.404
    then:
      field: $ref
      function: falsy
slug: openapi-response-delete-404-schema-ref-error
---