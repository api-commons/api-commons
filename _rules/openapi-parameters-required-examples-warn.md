---
slug: openapi-parameters-required-examples-warn
icon: book-open
name: OpenAPI Parameters Required Examples
description: >-
  Required parameters should include examples to support API mocking, testing, and documentation. Examples help consumers understand expected values and enable tools like Microcks to generate realistic mock responses.
message: Required parameters SHOULD include examples.
given: $.paths[*][*].parameters[?(@.required==true)]
severity: warn
view_sort: B
tags:
  - OpenAPI
  - Parameters
  - Examples
  - Mocking
guidance: Documentation
guidanceUrl: https://guidance.apievangelist.com/documentation
rule:
  openapi-parameters-required-examples-warn:
    description: >-
      Required parameters should include examples to support API mocking, testing, and documentation. Examples help consumers understand expected values and enable tools like Microcks to generate realistic mock responses.
    message: Required parameters SHOULD include examples.
    given: $.paths[*][*].parameters[?(@.required==true)]
    severity: warn
    then:
      function: xor
      functionOptions:
        properties:
          - example
          - examples
---
