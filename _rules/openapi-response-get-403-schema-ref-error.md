---
name: OpenAPI Response Get 403 Schema Ref Error
description: >-
  GET 403 forbidden HTTP status codes have a schema references to standardize
  the response payload returned for the error response
message: GET 403 Responses MUST Use Schema Reference
given: $.paths.*.get.responses.403
severity: error
tags:
  - OpenAPI
  - Responses
  - GET
  - 4xx
  - Schema
view_sort: M
guidance: Errors
guidanceUrl: https://guidance.apievangelist.com/errors
rule:
  openapi-response-get-403-schema-ref-error:
    description: >-
      GET 403 forbidden HTTP status codes have a schema references to
      standardize the response payload returned for the error response
    message: GET 403 Responses MUST Use Schema Reference
    severity: error
    given: $.paths.*.get.responses.403
    then:
      field: $ref
      function: falsy
slug: openapi-response-get-403-schema-ref-error
---