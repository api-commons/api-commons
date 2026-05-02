---
name: OpenAPI Response Get 401 Schema Ref Info
description: >-
  GET 401 unauthorized HTTP status codes have a schema references to standardize
  the response payload returned for the error response
message: GET 401 Responses Has Schema Reference
given: $.paths.*.get.responses.401
severity: info
tags:
  - OpenAPI
  - Responses
  - GET
  - 4xx
  - Schema
view_sort: K
guidance: Errors
guidanceUrl: https://guidance.apievangelist.com/errors
rule:
  openapi-response-get-401-schema-ref-info:
    description: >-
      GET 401 unauthorized HTTP status codes have a schema references to
      standardize the response payload returned for the error response
    message: GET 401 Responses Has Schema Reference
    severity: info
    given: $.paths.*.get.responses.401
    then:
      field: $ref
      function: truthy
slug: openapi-response-get-401-schema-ref-info
---