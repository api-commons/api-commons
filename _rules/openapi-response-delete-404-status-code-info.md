---
openapi-response-delete-404-status-code-info:
  description: Warn 404 status code for DELETE response.
  message: 404 Status Code for DELETE Responses
  severity: info
  given: $.paths.*.delete.responses
  then:
    field: '404'
    function: falsy
---