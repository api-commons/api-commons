---
name: OpenAPI Response Get 500 Schema Ref Info
description: >-
  GET 500 internal server error requests HTTP status codes have a schema
  references to standardize the response payload returned for the error response
message: GET 500 Responses Uses Schema Reference
given: $.paths.*.get.responses.500
severity: info
tags:
  - OpenAPI
  - Responses
  - GET
  - 5xx
  - Schema
view_sort: S
guidance: Errors
guidanceUrl: https://guidance.apievangelist.com/errors
rule:
  openapi-response-get-500-schema-ref-info:
    description: >-
      GET 500 internal server error requests HTTP status codes have a schema
      references to standardize the response payload returned for the error
      response
    message: GET 500 Responses Uses Schema Reference
    severity: info
    given: $.paths.*.get.responses.500
    then:
      field: $ref
      function: truthy
slug: openapi-response-get-500-schema-ref-info
---