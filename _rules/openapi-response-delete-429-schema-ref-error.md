---
name: OpenAPI Response Delete 429 Schema Ref Error
description: >-
  DELETE 429 too many requests HTTP status codes have a schema references to
  standardize the response payload returned for the error response
message: DELETE 429 Responses MUST Use Schema Reference
given: $.paths.*.delete.responses.429
severity: error
tags:
  - OpenAPI
  - Responses
  - DELETE
  - 4xx
view_sort: K
guidance: Errors
guidanceUrl: https://guidance.apievangelist.com/errors
rule:
  openapi-response-delete-429-schema-ref-error:
    description: >-
      DELETE 429 too many requests HTTP status codes have a schema references to
      standardize the response payload returned for the error response
    message: DELETE 429 Responses MUST Use Schema Reference
    severity: error
    given: $.paths.*.delete.responses.429
    then:
      field: $ref
      function: falsy
slug: openapi-response-delete-429-schema-ref-error
---