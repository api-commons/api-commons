---
openapi-response-get-403-status-code-warn:
  description: Warn 403 status code for GET response.
  message: 403 Status Code for GET Responses
  severity: warn
  given: $.paths.*.get.responses
  then:
    field: "403"
    function: truthy
---