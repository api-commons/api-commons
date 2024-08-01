---
openapi-schema-properties-type-string-pattern-info:
  description: Has schema property type string pattern.
  message: Schema Property Type String Pattern
  given:
    - $.components.schemas.*.properties.[?(@.type=='string')]
  severity: info
  then:
    field: pattern
    function: falsy
---