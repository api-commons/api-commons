---
openapi-schema-enum-casing-upper-snake-warn:
  description: Warn schema enum upper snake casing.
  message: Schema Enum Upper Snake Casing
  severity: warn
  given: $.components.schemas.*.enum.*
  then:
    function: pattern
    functionOptions:
      match: ^[A-Z]+(?:_[A-Z]+)*$
---