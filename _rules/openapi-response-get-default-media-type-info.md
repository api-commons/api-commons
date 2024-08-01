---
openapi-response-get-default-media-type-info:
  description: Has JSON media type for default.
  message: JSON Media Type Default
  severity: info
  given: $.paths.*.*.responses.default.content
  then:
    field: application/json
    function: falsy
---