---
openapi-response-delete-429-status-code-warn:
  description: Warn 429 status code for DELETE response.
  message: 429 Status Code for DELETE Responses
  severity: warn
  given: $.paths.*.delete.responses
  then:
    field: "429"
    function: truthy
---