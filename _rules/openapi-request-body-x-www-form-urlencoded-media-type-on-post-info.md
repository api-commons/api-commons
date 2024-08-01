---
openapi-request-body-x-www-form-urlencoded-media-type-on-post-info:
  description: Requires request body content on POST.
  message: Form URL Encoded Media Type POST
  given: $.paths.*.put.requestBody.content
  severity: info
  then:
    field: application/x-www-form-urlencoded
    function: falsy
---