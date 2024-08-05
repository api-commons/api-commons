---
openapi-response-get-401-status-code-info:
  description: Has 401 status code for GET response.
  message: 401 Status Code for GET Responses
  severity: info
  given: $.paths.*.get.responses
  then:
    field: "401"
    function: falsy
---