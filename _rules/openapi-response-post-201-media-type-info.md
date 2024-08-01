---
openapi-response-post-201-media-type-info:
  severity: info
  description: Require JSON media type for POST response.
  message: JSON Media Type POST
  given: $.paths.*.post.responses.201.content
  then:
    field: application/json
    function: falsy
---