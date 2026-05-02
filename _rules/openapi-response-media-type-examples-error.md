---
name: OpenAPI Response Get 200 Media Type Examples Error
description: >-
  GET 200 success HTTP status codes have examples to show one or many examples
  of responses for different types of API requests
message: GET 200 Response MUST Have Examples
given: $.paths.*.get.responses.200.content['application/json']
severity: error
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
  openapi-response-get-200-media-type-examples-error:
    description: >-
      GET 200 success HTTP status codes have examples to show one or many
      examples of responses for different types of API requests
    message: GET 200 Response MUST Have Examples
    severity: error
    given: $.paths.*.get.responses.200.content['application/json']
    then:
      field: examples
      function: truthy
slug: openapi-response-get-200-media-type-examples-error
---