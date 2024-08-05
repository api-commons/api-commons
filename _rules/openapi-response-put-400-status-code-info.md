---
openapi-response-put-400-status-code-info:
  description: Has 400 status code for PUT response.
  message: 400 Status Code for PUT Responses
  severity: info
  given: $.paths.*.put.responses
  then:
    field: '400'
    function: falsy
---