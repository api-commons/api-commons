---
name: OpenAPI Response Post 403 Schema Ref Info
description: >-
  POST 403 forbidden HTTP status codes have a schema references to standardize
  the response payload returned for the error response
message: POST 403 Responses Uses Schema Reference
given: $.paths.*.post.responses.403
severity: info
tags:
  - OpenAPI
  - Responses
  - POST
  - 4xx
  - Schema
view_sort: O
guidance: Errors
guidanceUrl: https://guidance.apievangelist.com/errors
rule:
  openapi-response-post-403-schema-ref-info:
    description: >-
      POST 403 forbidden HTTP status codes have a schema references to
      standardize the response payload returned for the error response
    message: POST 403 Responses Uses Schema Reference
    severity: info
    given: $.paths.*.post.responses.403
    then:
      field: $ref
      function: truthy
slug: openapi-response-post-403-schema-ref-info
---