---
name: OpenAPI Response Get 429 Schema Ref Info
description: >-
  GET 429 too many requests HTTP status codes have a schema references to
  standardize the response payload returned for the error response
message: GET 429 Responses Uses Schema Reference
given: $.paths.*.get.responses.429
severity: info
tags:
  - OpenAPI
  - Responses
  - GET
  - 4xx
  - Schema
view_sort: Q
guidance: Errors
guidanceUrl: https://guidance.apievangelist.com/errors
rule:
  openapi-response-get-429-schema-ref-info:
    description: >-
      GET 429 too many requests HTTP status codes have a schema references to
      standardize the response payload returned for the error response
    message: GET 429 Responses Uses Schema Reference
    severity: info
    given: $.paths.*.get.responses.429
    then:
      field: $ref
      function: truthy
slug: openapi-response-get-429-schema-ref-info
---