---
openapi-schema-properties-type-info:
  description: Require schema properties type.
  message: Schema Properties Type
  severity: info
  given: $.components.schemas.*.properties.*
  then:
    field: type
    function: falsy
---