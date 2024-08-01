---
openapi-parameters-name-error:
  description: Require parameter name.
  message: Parameter Name
  given: $.paths.*.*.parameters.*
  then:
    field: name
    function: truthy
---