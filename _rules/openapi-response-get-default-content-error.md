---
openapi-response-get-default-content-error:
  description: Require content for default.
  message: Default Content
  severity: error
  given: $.paths.*.*.responses.default
  then:
    field: content
    function: truthy
---