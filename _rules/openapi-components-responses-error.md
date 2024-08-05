---
openapi-components-responses-error:
  description: Require components responses.
  message: Components MUST have a responses property.
  severity: error
  given: $.components
  then:
    field: responses
    function: truthy
---