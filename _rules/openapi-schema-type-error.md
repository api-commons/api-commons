---
openapi-schema-type-error:
  description: Require schema type.
  message: Schema Type
  severity: error
  given: $.components.schemas.*
  then:
    field: type
    function: truthy
---