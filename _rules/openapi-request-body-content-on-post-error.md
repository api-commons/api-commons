---
openapi-request-body-content-on-post-error:
  description: Requires request body content on POST.
  message: Request Body Content POST
  given: $.paths.*.post.requestBody
  severity: error
  then:
    field: content
    function: truthy
---