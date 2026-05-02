---
name: OpenAPI Response Post 404 Schema Ref Info
description: >-
  POST 404 not found HTTP status codes have a schema references to standardize
  the response payload returned for the error response
message: POST 404 Responses Uses Schema Reference
given: $.paths.*.post.responses.404
severity: info
tags:
  - OpenAPI
  - Responses
  - POST
  - 4xx
  - Schema
view_sort: Q
guidance: Errors
guidanceUrl: https://guidance.apievangelist.com/errors
rule:
  openapi-response-post-404-schema-ref-info:
    description: >-
      POST 404 not found HTTP status codes have a schema references to
      standardize the response payload returned for the error response
    message: POST 404 Responses Uses Schema Reference
    severity: info
    given: $.paths.*.post.responses.404
    then:
      field: $ref
      function: truthy
slug: openapi-response-post-404-schema-ref-info
---