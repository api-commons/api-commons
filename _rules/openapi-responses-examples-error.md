---
openapi-responses-examples-error:
  description: OpenAPI - Responses - Examples
  message: Schema COULD have an example.
  severity: warn
  given: $.paths.*.get.responses.*
  then:
    - field: examples
      function: truthy
---