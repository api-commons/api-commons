---
openapi-request-body-on-put-error-info:
  description: Requires request body on PUT.
  message: Request Body PUT
  given: $.paths.*.put
  severity: error
  then:
    field: requestBody
    function: truthy
---