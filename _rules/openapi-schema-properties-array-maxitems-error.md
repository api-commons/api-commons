---
openapi-schema-properties-array-maxitems-error:
  description: Require schema property array maxItems.
  message: Schema Property Array MaxItems
  severity: error
  given: $.components.schemas.*.properties.[?(@.type=="array")]
  then:
    - field: maxItems
      function: truthy
---