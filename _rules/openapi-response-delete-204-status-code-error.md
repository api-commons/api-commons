---
openapi-response-delete-204-status-code-error:
  description: Require 204 status code for DELETE responses.
  message: DELETE 204 Status Code
  severity: info
  given: $.paths.*.delete.responses
  then:
    field: '204'
    function: truthy
---