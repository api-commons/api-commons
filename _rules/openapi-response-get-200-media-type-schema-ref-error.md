---
name: OpenAPI Response Get 200 Media Type Schema Ref Error
description: >-
  GET 200 success HTTP status codes have a schema references to standardize the
  response payload returned for a successful response
message: GET 200 Responses MUST Use Schema Reference
given: $.paths.*.get.responses.200.content['application/json'].schema
severity: error
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
  openapi-response-get-200-media-type-schema-ref-error:
    description: >-
      GET 200 success HTTP status codes have a schema references to standardize
      the response payload returned for a successful response
    message: GET 200 Responses MUST Use Schema Reference
    severity: error
    given: $.paths.*.get.responses.200.content['application/json'].schema
    then:
      field: $ref
      function: falsy
slug: openapi-response-get-200-media-type-schema-ref-error
---