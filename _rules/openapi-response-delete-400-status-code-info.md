---
openapi-response-delete-400-status-code-info:
  description: Has 400 status code for DELETE response.
  message: 400 Status Code for DELETE Responses
  severity: info
  given: $.paths.*.delete.responses
  then:
    field: '400'
    function: falsy
---