---
openapi-parameters-schema-type-info:
  description: Has parameter schema type.
  message: Parameter Schema Type
  severity: info
  given: $.paths.*.*.parameters.*.schema
  then:
    field: type
    function: falsy
---