---
name: OpenAPI Response Delete 400 Schema Ref Info
description: >-
  DELETE 400 bad request HTTP status codes have a schema references to
  standardize the response payload returned for the error response
message: DELETE 400 Responses Use Schema Reference
given: $.paths.*.delete.responses.400
severity: info
tags:
  - OpenAPI
  - Responses
  - DELETE
  - 4xx
view_sort: C
guidance: Errors
guidanceUrl: https://guidance.apievangelist.com/errors
rule:
  openapi-response-delete-400-schema-ref-info:
    description: >-
      DELETE 400 bad request HTTP status codes have a schema references to
      standardize the response payload returned for the error response
    message: DELETE 400 Responses Use Schema Reference
    severity: info
    given: $.paths.*.delete.responses.400
    then:
      field: $ref
      function: truthy
slug: openapi-response-delete-400-schema-ref-info
---