---
openapi-schema-enum-casing-lower-snake-warn:
  description: Warn schema enum lower snake casing.
  message: Schema Enum Lower Snake Casing
  severity: warn
  given: $.components.schemas.*.enum.*
  then:
    function: pattern
    functionOptions:
      match: ^(?:[a-z]++_)*+[a-z]++$
---