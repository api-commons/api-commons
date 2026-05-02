---
name: OpenAPI Components Examples Info
description: >-
  Utilizing an example object in the centralized OpenAPI components library
  helps make examples reusable across API requests and responses
message: Components Have a Examples Property
given: $.components
severity: info
tags:
  - OpenAPI
  - Components
guidance: Documentation
guidanceUrl: https://guidance.apievangelist.com/documentation
rule:
  openapi-components-examples-info:
    description: >-
      Utilizing an example object in the centralized OpenAPI components library
      helps make examples reusable across API requests and responses
    message: Components Have a Examples Property
    severity: info
    given: $.components
    then:
      field: examples
      function: falsy
slug: openapi-components-examples-info
---