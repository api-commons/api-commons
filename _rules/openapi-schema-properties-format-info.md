---
openapi-schema-properties-format-info:
  description: Has schema properties format.
  message: Schema Properties Format
  severity: info
  given: $.components.schemas.*.properties.*
  then:
    field: format
    function: falsy
---