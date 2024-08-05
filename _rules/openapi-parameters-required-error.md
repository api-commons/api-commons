---
openapi-parameters-required-error:
  description: Parameters Required
  message: Parameters MUST have a required property.
  severity: error
  given: $.paths.*.*.parameters.*
  then:
    field: required
    function: truthy
---