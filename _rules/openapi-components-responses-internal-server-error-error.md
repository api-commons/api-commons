---
openapi-components-responses-internal-server-error-error:
  description: Require components internal server error response.
  message: Components MUST have a internal server error response.
  severity: error
  given: $.components.responses
  then:
    field: InternalServerError
    function: truthy
---