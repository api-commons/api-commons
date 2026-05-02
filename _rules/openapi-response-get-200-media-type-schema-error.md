---
name: OpenAPI Response Get 200 Media Type Schema Error
description: >-
  GET 200 success HTTP status codes have a schema to standardize the response
  payload returned for a successful response
message: GET 200 Response MUST Have Schema
given: $.paths.*.get.responses.200.content['application/json']
severity: error
tags:
  - OpenAPI
  - Responses
  - GET
  - 2xx
  - Media Types
  - Schema
view_sort: F
guidance: Errors
guidanceUrl: https://guidance.apievangelist.com/errors
rule:
  openapi-response-get-200-media-type-schema-error:
    description: >-
      GET 200 success HTTP status codes have a schema to standardize the
      response payload returned for a successful response
    message: GET 200 Response MUST Have Schema
    severity: error
    given: $.paths.*.get.responses.200.content['application/json']
    then:
      field: schema
      function: truthy
slug: openapi-response-get-200-media-type-schema-error
---