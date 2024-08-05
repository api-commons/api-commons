---
openapi-response-put-403-status-code-warn:
  description: Warn 403 status code for PUT response.
  message: 403 Status Code for PUT Responses
  severity: warn
  given: $.paths.*.put.responses
  then:
    field: "403"
    function: truthy
---