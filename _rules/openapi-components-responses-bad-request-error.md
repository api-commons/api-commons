---
openapi-components-responses-bad-request-error:
  description: Require components bad request response.
  message: Components MUST have a bad request response.
  severity: error
  given: $.components.responses
  then:
    field: BadRequest
    function: truthy
---