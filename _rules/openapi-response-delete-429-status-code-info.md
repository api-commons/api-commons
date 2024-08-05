---
openapi-response-delete-429-status-code-info:
  description: Has 429 status code for DELETE response.
  message: 429 Status Code for DELETE Responses
  severity: info
  given: $.paths.*.delete.responses
  then:
    field: "429"
    function: falsy 
---