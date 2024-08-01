---
openapi-request-body-json-media-type-on-post-error:
  description: Warn JSON media type on POST.
  message: JSON Media Type POST
  given: $.paths.*.post.requestBody.content
  severity: warn
  then:
    field: application/json
    function: truthy
---