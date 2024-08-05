---
openapi-response-delete-401-status-code-info:
  description: Has 401 status code for DELETE response.
  message: 401 Status Code for DELETE Responses
  severity: info
  given: $.paths.*.delete.responses
  then:
    field: "401"
    function: falsy
---