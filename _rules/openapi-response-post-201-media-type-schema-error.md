---
openapi-response-post-201-media-type-schema-error:
  description: Require schema for POST.
  message: Schema POST
  severity: error
  given: $.paths.*.post.responses.201.content.application/json
  then:
    field: schema
    function: truthy
---