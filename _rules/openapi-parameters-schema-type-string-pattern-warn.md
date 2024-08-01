---
openapi-parameters-schema-type-string-pattern-warn:
  description: Warn parameter schema type string pattern.
  message: Parameter Schema Type String Pattern
  given:
    - $.paths.*.*.parameters.[?(@.type=='string')]
  severity: warn
  then:
    field: pattern
    function: truthy
---