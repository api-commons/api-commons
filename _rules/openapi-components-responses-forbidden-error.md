---
openapi-components-responses-forbidden-error:
  description: Require components forbidden response.
  message: Components MUST have a forbidden response.
  severity: error
  given: $.components.responses
  then:
    field: Forbidden
    function: truthy
---