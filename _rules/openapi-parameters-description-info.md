---
openapi-parameters-description-info:
  description: Has parameter description.
  message: Parameter Description
  severity: info
  given: $.paths.*.*.parameters.*
  then:
    field: description
    function: falsy
---