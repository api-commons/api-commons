---
openapi-schema-properties-nullable-error:
  description: Warn schema properties nullable.
  message: Schema Properties Format
  severity: error
  given: $.components.schemas.*.properties.*
  then:
    field: nullable
    function: truthy
---