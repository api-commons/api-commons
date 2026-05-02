---
name: OpenAPI Response Delete 404 Schema Ref Info
description: >-
  DELETE 404 not found HTTP status codes have a schema references to standardize
  the response payload returned for the error response
message: DELETE 404 Responses Uses Schema Reference
given: $.paths.*.delete.responses.404
severity: info
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
  openapi-response-delete-404-schema-ref-info:
    description: >-
      DELETE 404 not found HTTP status codes have a schema references to
      standardize the response payload returned for the error response
    message: DELETE 404 Responses Uses Schema Reference
    severity: info
    given: $.paths.*.delete.responses.404
    then:
      field: $ref
      function: truthy
slug: openapi-response-delete-404-schema-ref-info
---