---
name: OpenAPI Response Get 400 Schema Ref Info
description: >-
  GET 400 bad request HTTP status codes have a schema references to standardize
  the response payload returned for the error response
message: GET 400 Responses Uses Schema Reference
given: $.paths.*.get.responses.400
severity: info
tags:
  - OpenAPI
  - Responses
  - GET
  - 4xx
  - Schema
view_sort: I
guidance: Errors
guidanceUrl: https://guidance.apievangelist.com/errors
rule:
  openapi-response-get-400-schema-ref-info:
    description: >-
      GET 400 bad request HTTP status codes have a schema references to
      standardize the response payload returned for the error response
    message: GET 400 Responses Uses Schema Reference
    severity: info
    given: $.paths.*.get.responses.400
    then:
      field: $ref
      function: truthy
slug: openapi-response-get-400-schema-ref-info
---