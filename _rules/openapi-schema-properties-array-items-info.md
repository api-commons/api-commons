---
openapi-schema-properties-array-items-info:
  description: Require schema property array items.
  message: Schema Property Array Items
  severity: info
  given: $.components.schemas.*.properties.[?(@.type=="array")]
  then:
    field: items
    function: falsy
---