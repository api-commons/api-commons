---
openapi-response-get-200-content-info:
  description: Require content for GET.
  message: GET Content
  severity: info
  given: $.paths.*.get.responses.200
  then:
    field: content
    function: falsy
---