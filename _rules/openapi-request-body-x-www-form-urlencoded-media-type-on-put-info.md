---
openapi-request-body-x-www-form-urlencoded-media-type-on-put-info:
  description: Requires request body content on PUT.
  message: Form URL Encoded Media Type PUT
  given: $.paths.*.put.requestBody.content
  severity: info
  then:
    field: application/x-www-form-urlencoded
    function: falsy
---