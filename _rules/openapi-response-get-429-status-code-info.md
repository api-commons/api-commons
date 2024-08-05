---
openapi-response-get-429-status-code-info:
  description: Has 429 status code for GET response.
  message: 429 Status Code for GET Responses
  severity: info
  given: $.paths.*.get.responses
  then:
    field: "429"
    function: falsy 
---