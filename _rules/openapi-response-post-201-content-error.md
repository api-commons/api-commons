---
openapi-response-post-201-content-error:
  description: Require content for POST.
  message: POST Content
  severity: error
  given: $.paths.*.post.responses.201
  then:
    field: content
    function: truthy
---