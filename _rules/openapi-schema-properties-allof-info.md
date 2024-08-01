---
openapi-schema-properties-allof-info:
  description: Require schema properties allof.
  message: Schema Properties AllOf
  severity: info
  given: $.components.schemas.*.properties.*
  then:
    field: allOf
    function: falsy
---