---
openapi-response-put-400-status-code-warn:
  description: Warn 400 status code for PUT response.
  message: 400 Status Code for PUT Responses
  severity: warn
  given: $.paths.*.put.responses
  then:
    field: '400'
    function: truthy
---