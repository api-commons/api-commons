---
openapi-response-get-default-media-type-error:
  description: Require JSON media type for default.
  message: JSON Media Type Default
  severity: error
  given: $.paths.*.*.responses.default.content
  then:
    field: application/json
    function: truthy
---