---
openapi-schema-properties-enum-casing-error:
  description: Require schema property enum casing.
  message: Schema Property Enum Casing
  severity: error
  given: $.components.schemas.*.properties.*.enum.*
  then:
    function: pattern
    functionOptions:
      match: ^[A-Z]+(?:_[A-Z]+)*$
---