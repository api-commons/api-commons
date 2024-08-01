---
openapi-schema-properties-descriptions-info:
  description: Require schema description.
  message: Schema Description
  severity: info
  given: $.components.schemas.*.properties.*
  then:
    field: description
    function: falsy
---