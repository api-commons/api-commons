---
openapi-components-responses-unauthorized-error:
  description: Require components unauthorized response.
  message: Components MUST have a unauthorized response.
  severity: error
  given: $.components.responses
  then:
    field: Unauthorized
    function: truthy
---