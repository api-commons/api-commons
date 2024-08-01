---
openapi-response-put-500-status-code-info:
  description: Require 500 status code for PUT response.
  message: 500 Status Code for PUT Responses
  severity: info
  given: $.paths.*.put.responses
  then:
    field: '500'
    function: falsy
---