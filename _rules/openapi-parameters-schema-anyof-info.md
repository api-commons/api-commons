---
openapi-parameters-schema-anyof-info:
  description: Has parameter schema anyof.
  message: Parameter Schema AnyOf
  severity: info
  given: $.paths.*.*.parameters.*.schema
  then:
    field: anyOf
    function: falsy
---