---
openapi-components-responses-too-many-requests-info:
  description: Require components too many requests response.
  message: Components has a too many requests response.
  severity: info
  given: $.components.responses
  then:
    field: TooManyRequests
    function: falsy  
---