---
openapi-parameters-schema-type-integer-minimum-warn:
  description: Warn parameter schema type integer minlength.
  message: Parameter Schema Type Integer Minimum
  given:
    - $.paths.*.*.parameters.[?(@.type=='integer')]
  severity: warn
  then:
    field: minimum
    function: truthy
---