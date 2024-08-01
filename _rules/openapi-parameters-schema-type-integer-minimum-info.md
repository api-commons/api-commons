---
openapi-parameters-schema-type-integer-minimum-info:
  description: Has parameter schema type integer minimum.
  message: Parameter Schema Type Integer Minimum
  given:
    - $.paths.*.*.parameters.[?(@.type=='integer')]
  severity: info
  then:
    field: minimum
    function: falsy
---