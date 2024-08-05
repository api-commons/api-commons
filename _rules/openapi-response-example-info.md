---
openapi-response-example-info:
  description: OpenAPI - Responses - Example
  message: Response has an example.
  severity: info
  given: $.paths.*.*.responses.*.content[?(@.example)]
  then:
      function: falsy
---