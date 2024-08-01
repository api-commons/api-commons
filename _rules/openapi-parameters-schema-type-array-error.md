---
openapi-parameters-schema-type-array-error:
  description: Require schema type array items.
  message: Parameter Schema Type Array Items
  given: $.paths.*.*.parameters.schema[?(@.type=='array')]
  then:
    field: items
    function: truthy
---