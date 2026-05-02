---
name: OpenAPI Response Get 403 Schema Ref Info
description: >-
  GET 403 forbidden HTTP status codes have a schema references to standardize
  the response payload returned for the error response
message: GET 403 Responses Uses Schema Reference
given: $.paths.*.get.responses.403
severity: info
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
  openapi-response-get-403-schema-ref-info:
    description: >-
      GET 403 forbidden HTTP status codes have a schema references to
      standardize the response payload returned for the error response
    message: GET 403 Responses Uses Schema Reference
    severity: info
    given: $.paths.*.get.responses.403
    then:
      field: $ref
      function: truthy
slug: openapi-response-get-403-schema-ref-info
---