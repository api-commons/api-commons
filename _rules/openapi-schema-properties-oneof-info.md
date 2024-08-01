---
openapi-schema-properties-oneof-info:
  description: Require schema properties oneof.
  message: Schema Properties OneOf
  severity: info
  given: $.components.schemas.*.properties.*
  then:
    field: oneOf
    function: falsy
---