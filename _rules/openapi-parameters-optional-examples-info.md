---
slug: openapi-parameters-optional-examples-info
icon: book-open
name: OpenAPI Parameters Optional Examples
description: >-
  Optional parameters should include examples to support API mocking, testing, and documentation. While not strictly required, examples help consumers understand the range of acceptable values.
message: Optional parameters SHOULD include examples.
given: $.paths[*][*].parameters[?(@.required==false)]
severity: info
view_sort: B
tags:
  - OpenAPI
  - Parameters
  - Examples
  - Mocking
guidance: Documentation
guidanceUrl: https://guidance.apievangelist.com/documentation
rule:
  openapi-parameters-optional-examples-info:
    description: >-
      Optional parameters should include examples to support API mocking, testing, and documentation. While not strictly required, examples help consumers understand the range of acceptable values.
    message: Optional parameters SHOULD include examples.
    given: $.paths[*][*].parameters[?(@.required==false)]
    severity: info
    then:
      function: xor
      functionOptions:
        properties:
          - example
          - examples
---
