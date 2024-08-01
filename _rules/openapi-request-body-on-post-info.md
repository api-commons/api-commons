---
openapi-request-body-on-post-info:
  description: Require request body on POST.
  message: Request Body POST
  given: $.paths.*.post
  severity: info
  then:
    field: requestBody
    function: falsy
---