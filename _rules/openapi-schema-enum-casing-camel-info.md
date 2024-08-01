---
openapi-schema-enum-casing-camel-info:
  description: Has schema enum camel casing.
  message: Schema Enum Camel Casing
  severity: info
  given: $.components.schemas.*.enum.*
  then:
    function: pattern
    functionOptions:
      notMatch: ^[a-z]+(?:[A-Z][a-z]+)*$
---