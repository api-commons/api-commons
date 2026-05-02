---
name: OpenAPI Components Examples Error
description: >-
  Utilizing an example object in the centralized OpenAPI components library
  helps make examples reusable across API requests and responses
message: Components MUST Have a Examples Property
given: $.components
severity: error
tags:
  - OpenAPI
  - Components
guidance: Documentation
guidanceUrl: https://guidance.apievangelist.com/documentation
rule:
  openapi-components-examples-error:
    description: >-
      Utilizing an example object in the centralized OpenAPI components library
      helps make examples reusable across API requests and responses
    message: Components MUST Have a Examples Property
    severity: error
    given: $.components
    then:
      field: examples
      function: truthy
slug: openapi-components-examples-error
---