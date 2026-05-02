---
name: OpenAPI Response Post 401 Schema Ref Info
description: >-
  POST 401 unauthorized HTTP status codes have a schema references to
  standardize the response payload returned for the error response
message: POST 401 Responses Uses Schema Reference
given: $.paths.*.post.responses.401
severity: info
tags:
  - OpenAPI
  - Responses
  - POST
  - 4xx
  - Schema
view_sort: M
guidance: Errors
guidanceUrl: https://guidance.apievangelist.com/errors
rule:
  openapi-response-post-401-schema-ref-info:
    description: >-
      POST 401 unauthorized HTTP status codes have a schema references to
      standardize the response payload returned for the error response
    message: POST 401 Responses Uses Schema Reference
    severity: info
    given: $.paths.*.post.responses.401
    then:
      field: $ref
      function: truthy
slug: openapi-response-post-401-schema-ref-info
---