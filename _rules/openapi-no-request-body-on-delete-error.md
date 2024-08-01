---
openapi-no-request-body-on-delete-error:
  description: Requires no request body on DELETE
  message: DELETE Request Body
  given: $.paths.*.delete
  severity: error
  then:
    field: requestBody
    function: falsy
---