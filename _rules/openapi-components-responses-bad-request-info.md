---
openapi-components-responses-bad-request-info:
  description: Require components bad request response.
  message: Components has a bad request response.
  severity: info
  given: $.components.responses
  then:
    field: BadRequest
    function: falsy
---