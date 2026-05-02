---
slug: openapi-request-bodies-examples-content-warn
icon: book-open
name: OpenAPI Request Bodies Examples Content
description: >-
  Request body content should include examples to support API mocking, testing, and documentation. Examples enable tools to generate realistic mock requests and help consumers understand expected payloads.
message: Request body content SHOULD include examples.
given: $.paths[*][*].requestBody.content.*
severity: warn
view_sort: B
tags:
  - OpenAPI
  - Request Bodies
  - Examples
  - Mocking
guidance: OpenAPI
guidanceUrl: https://guidance.apievangelist.com/openapi
rule:
  openapi-request-bodies-examples-content-warn:
    description: >-
      Request body content should include examples to support API mocking, testing, and documentation. Examples enable tools to generate realistic mock requests and help consumers understand expected payloads.
    message: Request body content SHOULD include examples.
    given: $.paths[*][*].requestBody.content.*
    severity: warn
    then:
      function: xor
      functionOptions:
        properties:
          - example
          - examples
---
