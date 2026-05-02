---
name: OpenAPI Response Get 200 Media Type Info
description: >-
  GET 200 success HTTP status codes have a application/json media type,
  standardizing the response payload returned for a successful response
message: GET 200 Response Has Media Type.
given: $.paths.*.get.responses.200.content
severity: info
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
  openapi-response-get-200-media-type-info:
    description: >-
      GET 200 success HTTP status codes have a application/json media type,
      standardizing the response payload returned for a successful response
    message: GET 200 Response Has Media Type.
    severity: info
    given: $.paths.*.get.responses.200.content
    then:
      field: application/json
      function: falsy
slug: openapi-response-get-200-media-type-info
---