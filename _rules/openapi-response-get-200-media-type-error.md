---
name: OpenAPI Response Get 200 Media Type Error
description: >-
  GET 200 success HTTP status codes have a application/json media type,
  standardizing the response payload returned for a successful response
message: GET 200 Response MUST Have Media Type.
given: $.paths.*.get.responses.200.content
severity: error
tags:
  - OpenAPI
  - Responses
  - GET
  - 2xx
  - Media Types
view_sort: C
guidance: Errors
guidanceUrl: https://guidance.apievangelist.com/errors
rule:
  openapi-response-get-200-media-type-error:
    description: >-
      GET 200 success HTTP status codes have a application/json media type,
      standardizing the response payload returned for a successful response
    message: GET 200 Response MUST Have Media Type.
    severity: error
    given: $.paths.*.get.responses.200.content
    then:
      field: application/json
      function: truthy
slug: openapi-response-get-200-media-type-error
---