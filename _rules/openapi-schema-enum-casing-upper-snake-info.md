---
openapi-schema-enum-casing-upper-snake-info:
  description: Has schema enum upper snake casing.
  message: Schema Enum Upper Snake Casing
  severity: info
  given: $.components.schemas.*.enum.*
  then:
    function: pattern
    functionOptions:
      notMatch: ^[A-Z]+(?:_[A-Z]+)*$
---