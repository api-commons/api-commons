---
openapi-components-responses-forbidden-info:
  description: Require components forbidden response.
  message: Components has a forbidden response.
  severity: info
  given: $.components.responses
  then:
    field: Forbidden
    function: falsy  
---