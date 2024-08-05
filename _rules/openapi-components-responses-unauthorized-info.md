---
openapi-components-responses-unauthorized-info:
  description: Require components unauthorized response.
  message: Components has a unauthorized response.
  severity: info
  given: $.components.responses
  then:
    field: Unauthorized
    function: falsy  
---