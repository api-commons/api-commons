---
openapi-response-put-500-status-code-error:
  description: Require 500 status code for PUT response.
  message: 500 Status Code for PUT Responses
  severity: error
  given: $.paths.*.put.responses
  then:
    field: '500'
    function: truthy
---