---
openapi-parameters-in-error:
  description: Require parameter in.
  message: Parameters In
  given: $.paths.*.*.parameters.*
  then:
    field: in
    function: truthy
---