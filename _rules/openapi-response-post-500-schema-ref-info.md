---
name: OpenAPI Response Post 500 Schema Ref Info
description: >-
  POST 500 internal server error requests HTTP status codes have a schema
  references to standardize the response payload returned for the error response
message: POST 500 Responses Uses Schema Reference
given: $.paths.*.post.responses.500
severity: info
tags:
  - OpenAPI
  - Responses
  - POST
  - 5xx
  - Schema
view_sort: U
guidance: Errors
guidanceUrl: https://guidance.apievangelist.com/errors
rule:
  openapi-response-post-500-schema-ref-info:
    description: >-
      POST 500 internal server error requests HTTP status codes have a schema
      references to standardize the response payload returned for the error
      response
    message: POST 500 Responses Uses Schema Reference
    severity: info
    given: $.paths.*.post.responses.500
    then:
      field: $ref
      function: truthy
slug: openapi-response-post-500-schema-ref-info
---