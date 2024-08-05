---
openapi-parameters-name-error:
  description: Require parameter name.
  message: Parameter Name
  severity: error
  given: $.paths.*.*.parameters.*
  then:
    field: name
    function: truthy
---