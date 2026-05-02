---
name: OpenAPI Response Delete 429 Schema Ref Info
description: >-
  DELETE 429 too many requests HTTP status codes have a schema references to
  standardize the response payload returned for the error response
message: DELETE 429 Responses Uses Schema Reference
given: $.paths.*.delete.responses.429
severity: info
tags:
  - OpenAPI
  - Responses
  - DELETE
  - 4xx
view_sort: K
guidance: Errors
guidanceUrl: https://guidance.apievangelist.com/errors
rule:
  openapi-response-delete-429-schema-ref-info:
    description: >-
      DELETE 429 too many requests HTTP status codes have a schema references to
      standardize the response payload returned for the error response
    message: DELETE 429 Responses Uses Schema Reference
    severity: info
    given: $.paths.*.delete.responses.429
    then:
      field: $ref
      function: truthy
slug: openapi-response-delete-429-schema-ref-info
---