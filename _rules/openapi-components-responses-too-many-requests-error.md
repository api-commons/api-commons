---
openapi-components-responses-too-many-requests-error:
  description: Require components too many requests response.
  message: Components MUST have a too many requests response.
  severity: error
  given: $.components.responses
  then:
    field: TooManyRequests
    function: truthy
---