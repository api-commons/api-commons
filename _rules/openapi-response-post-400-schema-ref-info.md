---
name: OpenAPI Response Post 400 Schema Ref Info
description: >-
  POST 400 bad request HTTP status codes have a schema references to standardize
  the response payload returned for the error response
message: POST 400 Responses Uses Schema Reference
given: $.paths.*.post.responses.400
severity: info
tags:
  - OpenAPI
  - Responses
  - POST
  - 4xx
  - Schema
view_sort: K
guidance: Errors
guidanceUrl: https://guidance.apievangelist.com/errors
rule:
  openapi-response-post-400-schema-ref-info:
    description: >-
      POST 400 bad request HTTP status codes have a schema references to
      standardize the response payload returned for the error response
    message: POST 400 Responses Uses Schema Reference
    severity: info
    given: $.paths.*.post.responses.400
    then:
      field: $ref
      function: truthy
slug: openapi-response-post-400-schema-ref-info
---