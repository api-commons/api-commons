---
openapi-parameters-schema-type-error:
  description: Require parameter schema type.
  message: Parameter Schema Type
  given: $.paths.*.*.parameters.*.schema
  then:
    field: type
    function: truthy
---