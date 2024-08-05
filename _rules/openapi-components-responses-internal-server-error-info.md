---
openapi-components-responses-internal-server-error-info:
  description: Require components internal server error response.
  message: Components has a internal server error response.
  severity: info
  given: $.components.responses
  then:
    field: InternalServerError
    function: falsy  
---