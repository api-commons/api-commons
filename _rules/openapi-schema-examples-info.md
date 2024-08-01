---
openapi-schema-examples-info:
  description: Schema has examples.
  message: Schema Examples
  severity: info
  given: $.components.*
  then:
    - field: examples
      function: truthy
---