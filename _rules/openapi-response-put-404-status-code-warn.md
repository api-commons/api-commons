---
openapi-response-put-404-status-code-warn:
  description: Warn 404 status code for PUT response.
  message: 404 Status Code for PUT Responses
  severity: warn
  given: $.paths.*.put.responses
  then:
    field: '404'
    function: truthy
---