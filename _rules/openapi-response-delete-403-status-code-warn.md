---
openapi-response-delete-403-status-code-warn:
  description: Warn 403 status code for DELETE response.
  message: 403 Status Code for DELETE Responses
  severity: warn
  given: $.paths.*.delete.responses
  then:
    field: "403"
    function: truthy
---