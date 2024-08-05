---
openapi-components-responses-not-found-info:
  description: Require components not found response.
  message: Components has a not found response.
  severity: info
  given: $.components.responses
  then:
    field: NotFound
    function: falsy 
---