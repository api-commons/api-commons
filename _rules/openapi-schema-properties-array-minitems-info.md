---
openapi-schema-properties-array-minitems-info:
  description: Has schema property array minItems.
  message: Schema Property Array MinItems
  severity: info
  given: $.components.schemas.*.properties.[?(@.type=="array")]
  then:
    - field: minItems
      function: falsy
---