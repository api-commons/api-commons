---
openapi-parameters-name-info:
  description: Has parameter name.
  message: Parameter Name
  given: $.paths.*.*.parameters.*
  then:
    field: name
    function: falsy
---