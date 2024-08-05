---
openapi-response-delete-404-status-code-error:
  description: Warn 404 status code for DELETE response.
  message: 404 Status Code for DELETE Responses
  severity: warn
  given: $.paths.*.delete.responses
  then:
    field: '404'
    function: truthy
---