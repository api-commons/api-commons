---
openapi-schema-x-expandableFields-info:
  description: Has schema expansion fields.
  message: Schema X Expansion Fields
  severity: info
  given: $.components.schemas.*
  then:
    field: x-expandableFields
    function: falsy
---