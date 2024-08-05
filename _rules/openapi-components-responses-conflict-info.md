---
openapi-components-responses-conflict-info:
  description: Require components conflict response.
  message: Components has a conflict response.
  severity: info
  given: $.components.responses
  then:
    field: Conflict
    function: falsy   
---