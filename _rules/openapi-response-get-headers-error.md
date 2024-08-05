---
openapi-response-get-headers-error:
  description: Ensures GET responses have headers.
  message: GET responses MUST have headers.
  severity: error
  given: $.paths.*.get.responses.200
  then:
    field: headers
    function: truthy
---