---
openapi-response-get-200-status-code-info:
  description: Ensures GET operations have a 200 status code response.
  message: GET Response Has 200 Status Code
  severity: info
  given: $.paths.*.get.responses
  then:
    field: '200'
    function: falsy
---