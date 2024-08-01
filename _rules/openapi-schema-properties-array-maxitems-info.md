---
openapi-schema-properties-array-maxitems-info:
  description: Has schema property array maxItems.
  message: Schema Property Array MaxItems
  severity: info
  given: $.components.schemas.*.properties.[?(@.type=="array")]
  then:
    - field: maxItems
      function: truthy
---