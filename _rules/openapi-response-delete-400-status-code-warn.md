---
openapi-response-delete-400-status-code-warn:
  description: Warn 400 status code for DELETE response.
  message: 400 Status Code for DELETE Responses
  severity: warn
  given: $.paths.*.delete.responses
  then:
    field: '400'
    function: truthy
---