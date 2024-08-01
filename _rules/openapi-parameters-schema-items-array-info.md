---
openapi-parameters-schema-items-array-info:
  description: Has schema type array items.
  message: Parameter Schema Type Array Items
  severity: info
  given: $.paths.*.*.parameters.schema[?(@.type=='array')]
  then:
    field: items
    function: falsy
---