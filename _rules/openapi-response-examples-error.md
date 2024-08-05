---
openapi-response-examples-error:
  description: OpenAPI - Responses - Examples
  message: Schema COULD have an examples.
  severity: warn
  given: $.paths.*.*.responses.*.content[?(!@.example || @.examples)]
  then:
    - field: examples
      function: truthy 
---