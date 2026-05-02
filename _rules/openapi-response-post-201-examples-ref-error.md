---
name: OpenAPI Response Post 201 Examples Ref Error
description: >-
  POST 201 success HTTP status codes have example references to show one or many
  examples of responses for different types of API requests
message: POST 201 Responses MUST Use Examples Reference
given: $.paths.*.post.responses.201.content.*.examples
severity: error
tags:
  - OpenAPI
  - Responses
  - POST
  - 2xx
  - Examples
view_sort: G
guidance: Errors
guidanceUrl: https://guidance.apievangelist.com/errors
rule:
  openapi-response-post-201-examples-ref-error:
    description: >-
      POST 201 success HTTP status codes have example references to show one or
      many examples of responses for different types of API requests
    message: POST 201 Responses MUST Use Examples Reference
    given: $.paths.*.post.responses.201.content.*.examples
    severity: error
    then:
      field: $ref
      function: falsy
slug: openapi-response-post-201-examples-ref-error
---