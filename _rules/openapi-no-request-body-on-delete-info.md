---
openapi-no-request-body-on-delete-info:
  description: Has no request body on DELETE
  message: DELETE Request Body
  given: $.paths.*.delete
  severity: info
  then:
    field: requestBody
    function: truthy
---