---
openapi-responses-examples-info:
  description: OpenAPI - Responses - Examples
  message: Responses have examples.
  severity: info
  given: $.paths.*.get.responses.*
  then:
    - field: examples
      function: falsy
---