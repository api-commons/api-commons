---
name: OpenAPI Response Put 401 Schema Ref Info
description: >-
  PUT 401 unauthorized HTTP status codes have a schema references to standardize
  the response payload returned for the error response
message: PUT 401 Responses Uses Schema Reference
given: $.paths.*.put.responses.401
severity: info
tags:
  - OpenAPI
  - Responses
  - PUT
  - 4xx
  - Schema
view_sort: E
guidance: Errors
guidanceUrl: https://guidance.apievangelist.com/errors
rule:
  openapi-response-put-401-schema-ref-info:
    description: >-
      PUT 401 unauthorized HTTP status codes have a schema references to
      standardize the response payload returned for the error response
    message: PUT 401 Responses Uses Schema Reference
    severity: info
    given: $.paths.*.put.responses.401
    then:
      field: $ref
      function: truthy
slug: openapi-response-put-401-schema-ref-info
---