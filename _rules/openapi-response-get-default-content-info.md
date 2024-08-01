---
openapi-response-get-default-content-info:
  description: Require content for default.
  message: Default Content
  severity: info
  given: $.paths.*.*.responses.default
  then:
    field: content
    function: falsy
---