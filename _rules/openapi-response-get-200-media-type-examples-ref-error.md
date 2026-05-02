---
name: OpenAPI Response Get 200 Media Type Examples Ref Error
description: >-
  GET 200 success HTTP status codes have example references to show one or many
  examples of responses for different types of API requests
message: GET 200 Responses MUST Use Examples Reference
given: $.paths.*.get.responses.200.content['application/json'].examples.*
severity: error
tags:
  - OpenAPI
  - Responses
  - GET
  - 2xx
  - Media Types
  - Examples
view_sort: E
guidance: Errors
guidanceUrl: https://guidance.apievangelist.com/errors
rule:
  openapi-response-get-200-media-type-examples-ref-error:
    description: >-
      GET 200 success HTTP status codes have example references to show one or
      many examples of responses for different types of API requests
    message: GET 200 Responses MUST Use Examples Reference
    severity: error
    given: $.paths.*.get.responses.200.content['application/json'].examples.*
    then:
      field: $ref
      function: falsy
slug: openapi-response-get-200-media-type-examples-ref-error
---