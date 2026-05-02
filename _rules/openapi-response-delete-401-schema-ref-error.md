---
name: OpenAPI Response Delete 401 Schema Ref Error
description: >-
  DELETE 401 unauthorized HTTP status codes have a schema references to
  standardize the response payload returned for the error response
message: DELETE 401 Responses MUST Use Schema Reference
given: $.paths.*.delete.responses.401
severity: error
tags:
  - OpenAPI
  - Responses
  - DELETE
  - 4xx
view_sort: E
guidance: Errors
guidanceUrl: https://guidance.apievangelist.com/errors
rule:
  openapi-response-delete-401-schema-ref-error:
    description: >-
      DELETE 401 unauthorized HTTP status codes have a schema references to
      standardize the response payload returned for the error response
    message: DELETE 401 Responses MUST Use Schema Reference
    severity: error
    given: $.paths.*.delete.responses.401
    then:
      field: $ref
      function: falsy
slug: openapi-response-delete-401-schema-ref-error
---