---
openapi-request-bodies-required-property-info:
  description: Has request body required.
  message: REQUEST BODIES Required
  severity: info
  given: $.paths.*.requestBody
  then:
    field: required
    function: truthy
---