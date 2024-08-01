---
openapi-request-body-content-on-post-info:
  description: Requires request body content on POST.
  message: Request Body Content POST
  given: $.paths.*.post.requestBody
  severity: info
  then:
    field: content
    function: falsy
---