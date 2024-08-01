---
openapi-schema-properties-type-error:
  description: Require schema properties type.
  message: Schema Properties Type
  severity: error
  given: $.components.schemas.*.properties.*
  then:
    field: type
    function: truthy
---