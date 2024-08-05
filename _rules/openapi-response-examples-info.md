---
openapi-response-example-info:
  description: OpenAPI - Responses - Examples
  message: Response has examples.
  severity: info
  given: $.paths.*.*.responses.*.content[?(@.example || @.examples)]
  then:
      function: falsy 
---