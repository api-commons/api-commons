---
openapi-request-body-json-media-type-on-post-info:
  description: Has JSON media type on POST.
  message: JSON Media Type POST
  given: $.paths.*.post.requestBody.content
  severity: info
  then:
    field: application/json
    function: falsy
---