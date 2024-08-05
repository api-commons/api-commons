---
openapi-response-get-429-status-code-warn:
  description: Warn 429 status code for GET response.
  message: 429 Status Code for GET Responses
  severity: warn
  given: $.paths.*.get.responses
  then:
    field: "429"
    function: truthy
---