---
openapi-response-get-200-media-type-info:
  description: Has JSON media type for GET.
  message: JSON Media Type GET
  severity: info
  given: $.paths.*.get.responses.200.content
  then:
    field: application/json
    function: falsy
---