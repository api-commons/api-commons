---
openapi-schema-type-info:
  description: Has schema type.
  message: Schema Type
  severity: info
  given: $.components.schemas.*
  then:
    field: type
    function: falsy
---