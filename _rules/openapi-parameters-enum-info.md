---
openapi-parameters-enum-info:
  description: Has parameter enum.
  message: Parameter Enum
  severity: info
  given: $.paths.*.*.parameters.*
  then:
    field: enum
    function: falsy
---