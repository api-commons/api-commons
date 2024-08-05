---
openapi-parameters-name-info:
  description: Has parameter name.
  message: Parameter Name
  severity: info
  given: $.paths.*.*.parameters.*
  then:
    field: name
    function: falsy
---