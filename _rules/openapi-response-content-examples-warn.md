---
slug: openapi-response-content-examples-warn
icon: book-open
name: OpenAPI Response Content Examples
description: >-
  Response content should include examples to support API mocking, testing, and documentation. Examples enable tools to generate realistic mock responses and help consumers understand what to expect.
message: Response content SHOULD include examples.
given: $.paths[*][*].responses[*].content.*
severity: warn
view_sort: B
tags:
  - OpenAPI
  - Responses
  - Examples
  - Mocking
guidance: Errors
guidanceUrl: https://guidance.apievangelist.com/errors
rule:
  openapi-response-content-examples-warn:
    description: >-
      Response content should include examples to support API mocking, testing, and documentation. Examples enable tools to generate realistic mock responses and help consumers understand what to expect.
    message: Response content SHOULD include examples.
    given: $.paths[*][*].responses[*].content.*
    severity: warn
    then:
      function: xor
      functionOptions:
        properties:
          - example
          - examples
---
