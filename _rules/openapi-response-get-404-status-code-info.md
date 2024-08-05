---
openapi-response-get-404-status-code-info:
  description: Has 404 status code for GET response.
  message: 404 Status Code for GET Responses
  severity: info
  given: $.paths.*.get[?(@.properties)]
  then:
    field: "404"
    function: falsy
---