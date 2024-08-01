---
openapi-response-post-201-media-type-schema-info:
  description: Has schema for POST.
  message: Schema POST
  severity: info
  given: $.paths.*.post.responses.201.content.application/json
  then:
    field: schema
    function: falsy
---