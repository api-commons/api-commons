---
openapi-parameters-in-info:
  description: Has parameter in.
  message: Parameters In
  severity: info
  given: $.paths.*.*.parameters.*
  then:
    field: in
    function: falsy
---