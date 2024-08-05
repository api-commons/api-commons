---
openapi-response-get-401-status-code-warn:
  description: Warn 401 status code for GET response.
  message: 401 Status Code for GET Responses
  severity: warn
  given: $.paths.*.get.responses
  then:
    field: "401"
    function: truthy
---