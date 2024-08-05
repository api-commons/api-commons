---
openapi-response-delete-401-status-code-warn:
  description: Warn 401 status code for DELETE response.
  message: 401 Status Code for DELETE Responses
  severity: warn
  given: $.paths.*.delete.responses
  then:
    field: "401"
    function: truthy
---