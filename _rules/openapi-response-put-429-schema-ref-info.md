---
name: OpenAPI Response Put 429 Schema Ref Info
description: >-
  PUT 429 too many requests HTTP status codes have a schema references to
  standardize the response payload returned for the error response
message: PUT 429 Responses Uses Schema Reference
given: $.paths.*.put.responses.429
severity: info
tags:
  - OpenAPI
  - Responses
  - PUT
  - 4xx
  - Schema
view_sort: K
guidance: Errors
guidanceUrl: https://guidance.apievangelist.com/errors
rule:
  openapi-response-put-429-schema-ref-info:
    description: >-
      PUT 429 too many requests HTTP status codes have a schema references to
      standardize the response payload returned for the error response
    message: PUT 429 Responses Uses Schema Reference
    severity: info
    given: $.paths.*.put.responses.429
    then:
      field: $ref
      function: truthy
slug: openapi-response-put-429-schema-ref-info
---