---
openapi-schema-enum-casing-pascal-info:
  description: Has schema enum pascal casing.
  message: Schema Enum Pascal Casing
  severity: info
  given: $.components.schemas.*.enum.*
  then:
    function: pattern
    functionOptions:
      notMatch: ^[A-Z][a-z]+(?:[A-Z][a-z]+)*$
---