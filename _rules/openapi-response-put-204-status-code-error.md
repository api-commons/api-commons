---
openapi-response-put-204-status-code-error:
  description: Require 204 status code for PUT responses.
  message: PUT 204 Status Code
  severity: error
  given: $.paths.*.put.responses
  then:
    field: '204'
    function: truthy
---