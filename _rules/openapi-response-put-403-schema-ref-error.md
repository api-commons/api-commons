---
name: OpenAPI Response Put 403 Schema Ref Error
description: >-
  PUT 403 forbidden HTTP status codes have a schema references to standardize
  the response payload returned for the error response
message: PUT 403 Responses MUST Use Schema Reference
given: $.paths.*.put.responses.403
severity: error
tags:
  - OpenAPI
  - Responses
  - PUT
  - 4xx
  - Schema
view_sort: G
guidance: Errors
guidanceUrl: https://guidance.apievangelist.com/errors
rule:
  openapi-response-put-403-schema-ref-error:
    description: >-
      PUT 403 forbidden HTTP status codes have a schema references to
      standardize the response payload returned for the error response
    message: PUT 403 Responses MUST Use Schema Reference
    severity: error
    given: $.paths.*.put.responses.403
    then:
      field: $ref
      function: falsy
slug: openapi-response-put-403-schema-ref-error
---