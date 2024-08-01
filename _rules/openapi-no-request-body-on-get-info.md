---
openapi-no-request-body-on-get-info:
  description: Has no request body on DELETE
  message: GET Request Body
  given: $.paths.*.get
  severity: info
  then:
    field: requestBody
    function: truthy
---