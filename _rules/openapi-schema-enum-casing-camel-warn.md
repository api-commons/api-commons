---
openapi-schema-enum-casing-camel-warn:
  description: Warn schema enum camel casing.
  message: Schema Enum Camel Casing
  severity: warn
  given: $.components.schemas.*.enum.*
  then:
    function: pattern
    functionOptions:
      match: ^[a-z]+(?:[A-Z][a-z]+)*$
---