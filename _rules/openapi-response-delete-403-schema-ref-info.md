---
name: OpenAPI Response Delete 403 Schema Ref Info
description: >-
  DELETE 403 forbidden HTTP status codes have a schema references to standardize
  the response payload returned for the error response
message: DELETE 403 Responses Uses Schema Reference
given: $.paths.*.delete.responses.403
severity: info
tags:
  - OpenAPI
  - Responses
  - DELETE
  - 4xx
view_sort: G
guidance: Errors
guidanceUrl: https://guidance.apievangelist.com/errors
rule:
  openapi-response-delete-403-schema-ref-info:
    description: >-
      DELETE 403 forbidden HTTP status codes have a schema references to
      standardize the response payload returned for the error response
    message: DELETE 403 Responses Uses Schema Reference
    severity: info
    given: $.paths.*.delete.responses.403
    then:
      field: $ref
      function: truthy
slug: openapi-response-delete-403-schema-ref-info
---