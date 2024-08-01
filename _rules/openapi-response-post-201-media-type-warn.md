---
openapi-response-post-201-media-type-warn:
  description: Require JSON media type for POST.
  message: JSON Media Type POST
  severity: warn
  given: $.paths.*.post.responses.201.content
  then:
    field: application/json
    function: truthy
---