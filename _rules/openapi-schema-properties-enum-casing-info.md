---
openapi-schema-properties-enum-casing-info:
  description: Has schema property enum casing.
  message: Schema Property Enum Casing
  severity: error
  given: $.components.schemas.*.properties.*.enum.*
  then:
    function: pattern
    functionOptions:
      notMatch: ^[A-Z]+(?:_[A-Z]+)*$
---