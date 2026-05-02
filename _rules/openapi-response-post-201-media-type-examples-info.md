---
name: OpenAPI Response Post 201 Media Type Examples Info
description: >-
  POST 201 success HTTP status codes have examples to show one or many examples
  of responses for different types of API requests
message: POST 201 Responses Has Examples
given: $.paths.*.post.responses.201.content.application/json
severity: info
tags:
  - OpenAPI
  - Responses
  - POST
  - 2xx
  - Media Types
view_sort: H
guidance: Errors
guidanceUrl: https://guidance.apievangelist.com/errors
rule:
  openapi-response-post-201-media-type-examples-info:
    description: >-
      POST 201 success HTTP status codes have examples to show one or many
      examples of responses for different types of API requests
    message: POST 201 Responses Has Examples
    severity: info
    given: $.paths.*.post.responses.201.content.application/json
    then:
      field: examples
      function: falsy
slug: openapi-response-post-201-media-type-examples-info
---