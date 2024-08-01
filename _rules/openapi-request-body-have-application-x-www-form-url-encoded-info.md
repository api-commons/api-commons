---
openapi-request-body-have-application-x-www-form-url-encoded-info:
  description: Has request body application/x-www-form-urlencoded.
  message: Request Body Application X WWW Form URL Encoded
  given: $.paths.*.*.requestBody.content
  severity: info
  then:
    field: application/x-www-form-urlencoded
    function: falsy
---