---
name: OpenAPI Response Post 429 Schema Ref Info
description: >-
  POST 429 too many requests HTTP status codes have a schema references to
  standardize the response payload returned for the error response
message: POST 429 Responses Uses Schema Reference
given: $.paths.*.post.responses.429
severity: info
tags:
  - OpenAPI
  - Responses
  - POST
  - 4xx
  - Schema
view_sort: S
guidance: Errors
guidanceUrl: https://guidance.apievangelist.com/errors
rule:
  openapi-response-post-429-schema-ref-info:
    description: >-
      POST 429 too many requests HTTP status codes have a schema references to
      standardize the response payload returned for the error response
    message: POST 429 Responses Uses Schema Reference
    severity: info
    given: $.paths.*.post.responses.429
    then:
      field: $ref
      function: truthy
slug: openapi-response-post-429-schema-ref-info
---