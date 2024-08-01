---
openapi-schema-properties-descriptions-error:
  description: Require schema description.
  message: Schema Description
  severity: error
  given: $.components.schemas.*.properties.*
  then:
    field: description
    function: falsy
---