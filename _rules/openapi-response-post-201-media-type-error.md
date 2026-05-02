---
name: OpenAPI Response Post 201 Media Type Error
description: >-
  POST 201 success HTTP status codes have a application/json media type,
  standardizing the response payload returned for a successful response
message: POST 201 Responses MUST Have Media Type
given: $.paths.*.post.responses.201.content
severity: error
tags:
  - OpenAPI
  - Responses
  - POST
  - 2xx
  - Media Types
view_sort: F
guidance: Errors
guidanceUrl: https://guidance.apievangelist.com/errors
rule:
  openapi-response-post-201-media-type-error:
    description: >-
      POST 201 success HTTP status codes have a application/json media type,
      standardizing the response payload returned for a successful response
    message: POST 201 Responses MUST Have Media Type
    severity: error
    given: $.paths.*.post.responses.201.content
    then:
      field: application/json
      function: truthy
slug: openapi-response-post-201-media-type-error
---