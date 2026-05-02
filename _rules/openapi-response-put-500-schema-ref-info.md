---
name: OpenAPI Response Put 500 Schema Ref Info
description: >-
  PUT 500 internal server error requests HTTP status codes have a schema
  references to standardize the response payload returned for the error response
message: PUT 500 Responses Uses Schema Reference
given: $.paths.*.put.responses.500
severity: info
tags:
  - OpenAPI
  - Responses
  - PUT
  - 5xx
  - Schema
view_sort: M
guidance: Errors
guidanceUrl: https://guidance.apievangelist.com/errors
rule:
  openapi-response-put-500-schema-ref-info:
    description: >-
      PUT 500 internal server error requests HTTP status codes have a schema
      references to standardize the response payload returned for the error
      response
    message: PUT 500 Responses Uses Schema Reference
    severity: info
    given: $.paths.*.put.responses.500
    then:
      field: $ref
      function: truthy
slug: openapi-response-put-500-schema-ref-info
---