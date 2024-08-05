---
openapi-components-responses-conflict-error:
  description: Require components conflict response.
  message: Components MUST have a conflict response.
  severity: error
  given: $.components.responses
  then:
    field: Conflict
    function: truthy
---