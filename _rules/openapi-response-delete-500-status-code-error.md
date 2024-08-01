---
openapi-response-delete-500-status-code-error:
  description: Require 500 status code for DELETE response.
  message: 500 Status Code for DELETE Responses
  severity: error
  given: $.paths.*.delete.responses
  then:
    field: '500'
    function: truthy
---