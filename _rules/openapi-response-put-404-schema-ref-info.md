---
name: OpenAPI Response Put 404 Schema Ref Info
description: >-
  PUT 404 not found HTTP status codes have a schema references to standardize
  the response payload returned for the error response
message: PUT 404 Responses Uses Schema Reference
given: $.paths.*.put.responses.404
severity: info
tags:
  - OpenAPI
  - Responses
  - PUT
  - 4xx
  - Schema
view_sort: I
guidance: Errors
guidanceUrl: https://guidance.apievangelist.com/errors
rule:
  openapi-response-put-404-schema-ref-info:
    description: >-
      PUT 404 not found HTTP status codes have a schema references to
      standardize the response payload returned for the error response
    message: PUT 404 Responses Uses Schema Reference
    severity: info
    given: $.paths.*.put.responses.404
    then:
      field: $ref
      function: truthy
slug: openapi-response-put-404-schema-ref-info
---