---
openapi-response-put-403-status-code-info:
  description: Has 403 status code for PUT response.
  message: 403 Status Code for PUT Responses
  severity: info
  given: $.paths.*.put.responses
  then:
    field: "403"
    function: falsy 
---