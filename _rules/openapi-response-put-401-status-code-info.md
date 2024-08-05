---
openapi-response-put-401-status-code-info:
  description: Has 401 status code for PUT response.
  message: 401 Status Code for PUT Responses
  severity: info
  given: $.paths.*.put.responses
  then:
    field: "401"
    function: falsy 
---