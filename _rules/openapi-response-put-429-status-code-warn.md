---
openapi-response-put-429-status-code-warn:
  description: Warn 429 status code for PUT response.
  message: 429 Status Code for PUT Responses
  severity: warn
  given: $.paths.*.put.responses
  then:
    field: "429"
    function: truthy
---