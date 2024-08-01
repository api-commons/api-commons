---
openapi-parameters-schema-error:
  description: Require parameter schema.
  message: Parameter Schema Type
  given: $.paths.*.*.parameters.*
  then:
    field: schema
    function: truthy
---