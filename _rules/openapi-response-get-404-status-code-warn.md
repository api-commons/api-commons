---
openapi-response-get-404-status-code-warn:
  description: Warn 404 status code for GET response.
  message: 404 Status Code for GET Responses
  severity: warn
  given: $.paths.*.get[?(@.properties)]
  then:
    field: "404"
    function: truthy
---