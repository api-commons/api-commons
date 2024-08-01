---
openapi-parameters-schema-type-string-pattern-info:
  description: Has parameter schema type string pattern.
  message: Parameter Schema Type String Pattern
  given:
    - $.paths.*.*.parameters.[?(@.type=='string')]
  severity: info
  then:
    field: pattern
    function: falsy
---