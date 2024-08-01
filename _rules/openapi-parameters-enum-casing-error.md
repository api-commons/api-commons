---
openapi-parameters-enum-casing-error:
  description: Require parameter enum upper snake case.
  message: Parameter Enum Upper Snake Case
  severity: error
  given: $.paths.*.*.parameters.*.enum.*
  then:
    function: pattern
    functionOptions:
      notMatch: ^[A-Z]+(?:_[A-Z]+)*$
---