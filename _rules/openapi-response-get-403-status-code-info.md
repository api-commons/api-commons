---
openapi-response-get-403-status-code-info:
  description: Has 403 status code for GET response.
  message: 403 Status Code for GET Responses
  severity: info
  given: $.paths.*.get.responses
  then:
    field: "403"
    function: falsy 
---