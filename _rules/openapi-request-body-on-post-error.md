---
openapi-request-body-on-post-error:
  description: Require request body on POST.
  message: Request Body POST
  given: $.paths.*.post
  severity: error
  then:
    field: requestBody
    function: truthy
---