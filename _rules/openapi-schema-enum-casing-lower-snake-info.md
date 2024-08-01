---
openapi-schema-enum-casing-lower-snake-info:
  description: Has schema enum lower snake casing.
  message: Schema Enum Lower Snake Casing
  severity: info
  given: $.components.schemas.*.enum.*
  then:
    function: pattern
    functionOptions:
      notMatch: ^(?:[a-z]++_)*+[a-z]++$
---