---
name: OpenAPI Response Delete 401 Schema Ref Info
description: >-
  DELETE 401 unauthorized HTTP status codes have a schema references to
  standardize the response payload returned for the error response
message: DELETE 401 Responses Uses Schema Reference
given: $.paths.*.delete.responses.401
severity: info
tags:
  - OpenAPI
  - Responses
  - DELETE
  - 4xx
view_sort: E
guidance: Errors
guidanceUrl: https://guidance.apievangelist.com/errors
rule:
  openapi-response-delete-401-schema-ref-info:
    description: >-
      DELETE 401 unauthorized HTTP status codes have a schema references to
      standardize the response payload returned for the error response
    message: DELETE 401 Responses Uses Schema Reference
    severity: info
    given: $.paths.*.delete.responses.401
    then:
      field: $ref
      function: truthy
slug: openapi-response-delete-401-schema-ref-info
---