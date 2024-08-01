---
openapi-schema-properties-nullable-info:
  description: Has schema properties nullable.
  message: Schema Properties Nullable
  severity: info
  given: $.components.schemas.*.properties.*
  then:
    field: nullable
    function: falsy
---