---
name: OpenAPI Response Delete 400 Schema Ref Error
description: >-
  DELETE 400 bad request HTTP status codes have a schema references to
  standardize the response payload returned for the error response
message: DELETE 400 Responses MUST Use Schema Reference
given: $.paths.*.delete.responses.400
severity: error
tags:
  - OpenAPI
  - Responses
  - DELETE
  - 4xx
view_sort: C
guidance: Errors
guidanceUrl: https://guidance.apievangelist.com/errors
rule:
  openapi-response-delete-400-schema-ref-error:
    description: >-
      DELETE 400 bad request HTTP status codes have a schema references to
      standardize the response payload returned for the error response
    message: DELETE 400 Responses MUST Use Schema Reference
    severity: error
    given: $.paths.*.delete.responses.400
    then:
      field: $ref
      function: falsy
slug: openapi-response-delete-400-schema-ref-error
---