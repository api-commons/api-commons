---
openapi-schema-properties-x-expandableFields-info:
  description: Has schema properties expansion fields.
  message: Schema Properties X Expansion Fields
  severity: info
  given: $.components.schemas.*.properties.*
  then:
    field: x-expandableFields
    function: falsy
---