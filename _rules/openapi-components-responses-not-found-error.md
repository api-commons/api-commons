---
openapi-components-responses-not-found-error:
  description: Require components not found response.
  message: Components MUST have a not found response.
  severity: error
  given: $.components.responses
  then:
    field: NotFound
    function: truthy
---