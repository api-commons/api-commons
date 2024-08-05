---
openapi-response-put-429-status-code-info:
  description: Has 429 status code for PUT response.
  message: 429 Status Code for PUT Responses
  severity: info
  given: $.paths.*.put.responses
  then:
    field: "429"
    function: falsy 
---