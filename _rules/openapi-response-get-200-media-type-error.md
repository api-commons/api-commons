---
openapi-response-get-200-media-type-error:
  description: Require JSON media type for GET.
  message: JSON Media Type GET
  severity: error
  given: $.paths.*.get.responses.200.content
  then:
    field: application/json
    function: truthy
---