---
openapi-schema-description-error:
  description: Ensure all schema properties should have a description.
  message: Schema SHOULD have a description.
  severity: error
  given: $.components.schemas.*
  then:
    field: description
    function: truthy
---