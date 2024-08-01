---
openapi-parameters-enum-casing-info:
  description: Has parameter enum upper snake case.
  message: Parameter Enum Upper Snake Case
  severity: info
  given: $.paths.*.*.parameters.*.enum.*
  then:
    function: pattern
    functionOptions:
      match: ^[A-Z]+(?:_[A-Z]+)*$
---