---
openapi-response-get-500-status-code-info:
  description: Has 500 status code for GET response.
  message: 500 Status Code for GET Responses
  severity: info
  given: $.paths.*.get.responses
  then:
    field: '500'
    function: falsy
---