---
openapi-response-get-default-status-code-info:
  description: Has a default status code.
  message: Response Has Default Status Code
  severity: info
  given: $.paths.*.*.responses
  then:
    field: default
    function: falsy
---