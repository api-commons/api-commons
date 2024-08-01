---
openapi-response-get-400-status-code-info:
  description: Has 400 status code for GET response.
  message: 400 Status Code for GET Responses
  severity: info
  given: $.paths.*.get.responses
  then:
    field: '400'
    function: falsy
---