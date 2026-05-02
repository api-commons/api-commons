---
name: OpenAPI Response Get 200 Media Type Examples Ref Info
description: >-
  GET 200 success HTTP status codes have example references to show one or many
  examples of responses for different types of API requests
message: GET 200 Responses Uses Examples Reference
given: $.paths.*.get.responses.200.content['application/json'].examples.*
severity: info
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
  openapi-response-get-200-media-type-examples-ref-info:
    description: >-
      GET 200 success HTTP status codes have example references to show one or
      many examples of responses for different types of API requests
    message: GET 200 Responses Uses Examples Reference
    severity: info
    given: $.paths.*.get.responses.200.content['application/json'].examples.*
    then:
      field: $ref
      function: truthy
slug: openapi-response-get-200-media-type-examples-ref-info
---