---
openapi-response-put-204-status-code-info:
  description: Has 204 status code for PUT responses.
  message: PUT 204 Status Code
  severity: info
  given: $.paths.*.put.responses
  then:
    field: '204'
    function: falsy
---