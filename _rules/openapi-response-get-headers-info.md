---
openapi-response-get-headers-info:
  description: Ensures GET responses have headers.
  message: GET response has headers.
  severity: info
  given: $.paths.*.get.responses.200
  then:
    field: headers
    function: falsy 
---