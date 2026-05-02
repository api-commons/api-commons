---
name: OpenAPI Response Delete 403 Schema Ref Error
description: >-
  DELETE 403 forbidden HTTP status codes have a schema references to standardize
  the response payload returned for the error response
message: DELETE 403 Responses MUST Use Schema Reference
given: $.paths.*.delete.responses.403
severity: error
tags:
  - OpenAPI
  - Responses
  - DELETE
  - 4xx
view_sort: G
guidance: Errors
guidanceUrl: https://guidance.apievangelist.com/errors
rule:
  openapi-response-delete-403-schema-ref-error:
    description: >-
      DELETE 403 forbidden HTTP status codes have a schema references to
      standardize the response payload returned for the error response
    message: DELETE 403 Responses MUST Use Schema Reference
    severity: error
    given: $.paths.*.delete.responses.403
    then:
      field: $ref
      function: falsy
slug: openapi-response-delete-403-schema-ref-error
---