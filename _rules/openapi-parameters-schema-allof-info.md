---
openapi-parameters-schema-allof-info:
  description: Has parameter schema allof.
  message: Parameter Schema AllOf
  severity: info
  given: $.paths.*.*.parameters.*.schema
  then:
    field: allOf
    function: falsy
---