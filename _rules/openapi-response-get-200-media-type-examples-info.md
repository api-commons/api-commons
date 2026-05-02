---
name: OpenAPI Response Get 200 Media Type Examples Info
description: >-
  GET 200 success HTTP status codes have examples to show one or many examples
  of responses for different types of API requests
message: GET 200 ResponseHas Examples
given: $.paths.*.get.responses.200.content['application/json']
severity: info
tags:
  - OpenAPI
  - Responses
  - GET
  - 2xx
  - Media Types
  - Examples
view_sort: D
guidance: Errors
guidanceUrl: https://guidance.apievangelist.com/errors
rule:
  openapi-response-get-200-media-type-examples-info:
    description: >-
      GET 200 success HTTP status codes have examples to show one or many
      examples of responses for different types of API requests
    message: GET 200 ResponseHas Examples
    severity: info
    given: $.paths.*.get.responses.200.content['application/json']
    then:
      field: examples
      function: falsy
slug: openapi-response-get-200-media-type-examples-info
---