---
name: OpenAPI Response Delete 500 Schema Ref Error
description: >-
  DELETE 500 internal server error requests HTTP status codes have a schema
  references to standardize the response payload returned for the error response
message: DELETE 500 Responses MUST Use Schema Reference
given: $.paths.*.delete.responses.500
severity: error
tags:
  - OpenAPI
  - Responses
  - DELETE
  - 5xx
view_sort: M
guidance: Errors
guidanceUrl: https://guidance.apievangelist.com/errors
rule:
  openapi-response-delete-500-schema-ref-error:
    description: >-
      DELETE 500 internal server error requests HTTP status codes have a schema
      references to standardize the response payload returned for the error
      response
    message: DELETE 500 Responses MUST Use Schema Reference
    severity: error
    given: $.paths.*.delete.responses.500
    then:
      field: $ref
      function: falsy
slug: openapi-response-delete-500-schema-ref-error
---