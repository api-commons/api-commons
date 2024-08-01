---
openapi-parameters-schema-info:
  description: Has parameter schema.
  message: Parameter Schema Type
  severity: info
  given: $.paths.*.*.parameters.*
  then:
    field: schema
    function: falsy
---