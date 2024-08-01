---
openapi-parameters-schema-type-integer-maximum-warn:
  description: Warn parameter schema type integer maximum.
  message: Parameter Schema Type Integer Maximum
  given:
    - $.paths.*.*.parameters.[?(@.type=='integer')]
  severity: warn
  then:
    field: maximum
    function: truthy
---