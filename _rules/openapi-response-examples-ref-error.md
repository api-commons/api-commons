---
name: OpenAPI Response Examples Ref Error
description: >-
  Have example references to show one or many
  examples of responses for different types of API requests
message: Responses MUST Use Examples Reference
given: $.paths.*.get.responses.200.content['application/json'].examples.*
severity: error
tags:
  - OpenAPI
  - Responses
  - Examples
view_sort: E
guidance: Errors
guidanceUrl: https://guidance.apievangelist.com/errors
rule:
  openapi-response-examples-ref-error:
    description: >-
      Have example references to show one or
      many examples of responses for different types of API requests
    message: Responses MUST Use Examples Reference
    severity: error
    given: $.paths.*.get.responses.*.*.*.examples.*
    then:
      field: $ref
      function: falsy
slug: openapi-response-examples-ref-error
---