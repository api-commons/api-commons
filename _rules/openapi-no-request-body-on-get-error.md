---
openapi-no-request-body-on-get-error:
  description: Requires no request body on GET
  message: GET Request Body
  given: $.paths.*.get
  severity: error
  then:
    field: requestBody
    function: falsy
---