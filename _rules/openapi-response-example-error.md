---
openapi-response-example-error:
  description: OpenAPI - Responses - Example
  message: Schema COULD have an example.
  severity: warn
  given: $.paths.*.*.responses.*.content[?(!@.examples)]
  then:
    - field: example
      function: truthy 
---