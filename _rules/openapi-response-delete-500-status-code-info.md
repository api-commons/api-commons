---
openapi-response-delete-500-status-code-info:
  description: Require 500 status code for DELETE response.
  message: 500 Status Code for DELETE Responses
  severity: info
  given: $.paths.*.delete.responses
  then:
    field: '500'
    function: falsy
---