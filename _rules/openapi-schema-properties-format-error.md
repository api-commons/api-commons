---
openapi-schema-properties-format-error:
  description: Warn schema properties format.
  message: Schema Properties Format
  severity: error
  given: $.components.schemas.*.properties.*
  then:
    field: format
    function: truthy
---