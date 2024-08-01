---
openapi-schema-properties-anyof-info:
  description: Require schema properties anyof.
  message: Schema Properties AnyOf
  severity: info
  given: $.components.schemas.*.properties.*
  then:
    field: anyOf
    function: falsy
---