---
openapi-schema-enum-casing-pascal-warn:
  description: Warn schema enum pascal casing.
  message: Schema Enum Pascal Casing
  severity: warn
  given: $.components.schemas.*.enum.*
  then:
    function: pattern
    functionOptions:
      match: ^[A-Z][a-z]+(?:[A-Z][a-z]+)*$
---