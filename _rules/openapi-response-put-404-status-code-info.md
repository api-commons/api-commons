---
openapi-response-put-404-status-code-info:
  description: Has 404 status code for PUT response.
  message: 404 Status Code for PUT Responses
  severity: info
  given: $.paths.*.put.responses
  then:
    field: '404'
    function: falsy
---