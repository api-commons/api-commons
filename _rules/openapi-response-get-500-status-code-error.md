---
openapi-response-get-500-status-code-error:
  description: Require 500 status code for GET response.
  message: 500 Status Code for GET Responses
  severity: error
  given: $.paths.*.get.responses
  then:
    field: '500'
    function: truthy
---