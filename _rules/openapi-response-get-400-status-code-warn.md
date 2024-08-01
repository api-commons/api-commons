---
openapi-response-get-400-status-code-warn:
  description: Warn 400 status code for GET response.
  message: 400 Status Code for GET Responses
  severity: warn
  given: $.paths.*.get.responses
  then:
    field: '400'
    function: truthy
---