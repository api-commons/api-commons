---
openapi-parameters-schema-oneof-info:
  description: Has parameter schema oneof.
  message: Parameter Schema OneOf
  severity: info
  given: $.paths.*.*.parameters.*.schema
  then:
    field: oneOf
    function: falsy
---