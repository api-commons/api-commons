---
name: OpenAPI Response Put 400 Schema Ref Info
description: >-
  PUT 400 bad request HTTP status codes have a schema references to standardize
  the response payload returned for the error response
message: PUT 400 Responses Uses Schema Reference
given: $.paths.*.put.responses.400
severity: info
tags:
  - OpenAPI
  - Responses
  - PUT
  - 4xx
  - Schema
view_sort: C
guidance: Errors
guidanceUrl: https://guidance.apievangelist.com/errors
rule:
  openapi-response-put-400-schema-ref-info:
    description: >-
      PUT 400 bad request HTTP status codes have a schema references to
      standardize the response payload returned for the error response
    message: PUT 400 Responses Uses Schema Reference
    severity: info
    given: $.paths.*.put.responses.400
    then:
      field: $ref
      function: truthy
slug: openapi-response-put-400-schema-ref-info
---