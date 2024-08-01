---
openapi-response-get-200-content-error:
  description: Require content for GET.
  message: GET Content
  severity: error
  given: $.paths.*.get.responses.200
  then:
    field: content
    function: truthy
---