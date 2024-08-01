---
openapi-schema-properties-array-minitems-error:
  description: Require schema property array minItems.
  message: Schema Property Array MinItems
  severity: error
  given: $.components.schemas.*.properties.[?(@.type=="array")]
  then:
    - field: minItems
      function: truthy
---