---
openapi-request-bodies-required-property-error:
  description: Require request body required.
  message: REQUEST BODIES Required
  severity: error
  given: $.paths.*.requestBody
  then:
    field: required
    function: falsy
---