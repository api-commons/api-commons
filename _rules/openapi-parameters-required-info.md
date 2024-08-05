---
openapi-parameters-required-info:
  description: Parameters Required
  message: Parameter has a required property.
  severity: info
  given: $.paths.*.*.parameters.*
  then:
    field: required
    function: falsy
---