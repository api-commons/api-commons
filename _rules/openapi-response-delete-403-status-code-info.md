---
openapi-response-delete-403-status-code-info:
  description: Has 403 status code for DELETE response.
  message: 403 Status Code for DELETE Responses
  severity: info
  given: $.paths.*.delete.responses
  then:
    field: "403"
    function: falsy
---