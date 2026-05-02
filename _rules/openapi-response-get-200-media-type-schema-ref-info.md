---
name: OpenAPI Response Get 200 Media Type Schema Ref Info
description: >-
  GET 200 success HTTP status codes have a schema references to standardize the
  response payload returned for a successful response
message: GET 200 Responses Uses Schema Reference
given: $.paths.*.get.responses.200.content['application/json'].schema
severity: info
tags:
  - OpenAPI
  - Responses
  - GET
  - 2xx
  - Media Types
  - Schema
view_sort: G
guidance: Errors
guidanceUrl: https://guidance.apievangelist.com/errors
rule:
  openapi-response-get-200-media-type-schema-ref-info:
    description: >-
      GET 200 success HTTP status codes have a schema references to standardize
      the response payload returned for a successful response
    message: GET 200 Responses Uses Schema Reference
    severity: info
    given: $.paths.*.get.responses.200.content['application/json'].schema
    then:
      field: $ref
      function: truthy
slug: openapi-response-get-200-media-type-schema-ref-info
---