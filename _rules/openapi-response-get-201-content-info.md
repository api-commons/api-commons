---
openapi-response-get-201-content-info:
  description: Require content for POST.
  message: POST Content
  severity: info
  given: $.paths.*.post.responses.201
  then:
    field: content
    function: falsy
---