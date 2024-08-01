---
openapi-parameters-schema-type-integer-maximum-info:
  description: Has parameter schema type integer maximum.
  message: Parameter Schema Type Integer Maximum
  given:
    - $.paths.*.*.parameters.[?(@.type=='integer')]
  severity: info
  then:
    field: maximum
    function: falsy
---