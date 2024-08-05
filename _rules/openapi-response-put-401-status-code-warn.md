---
openapi-response-put-401-status-code-warn:
  description: Warn 401 status code for PUT response.
  message: 401 Status Code for PUT Responses
  severity: warn
  given: $.paths.*.put.responses
  then:
    field: "401"
    function: truthy
---