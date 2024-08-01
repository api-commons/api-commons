---
openapi-schema-properties-type-string-pattern-warn:
  description: Warn schema property type string pattern.
  message: Schema Property Type String Pattern
  given:
    - $.components.schemas.*.properties.[?(@.type=='string')]
  severity: warn
  then:
    field: pattern
    function: truthy
---