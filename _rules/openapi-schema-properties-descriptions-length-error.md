---
openapi-schema-properties-descriptions-length-error:
  description: Require schema description length 250.
  message: Schema Description Length
  severity: error
  given: $.components.schemas.*.properties.*
  then:
    field: description
    function: length
    functionOptions:
      max: 250
---