---
openapi-schema-description-info:
  description: Ensure all schema properties should have a description.
  message: Schemas has a description.
  severity: info
  given: $.components.schemas.*
  then:
    field: description
    function: falsy
---