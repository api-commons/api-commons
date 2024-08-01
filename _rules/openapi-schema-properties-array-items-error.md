---
openapi-schema-properties-array-items-error:
  description: Require schema property array items.
  message: Schema Property Array Items
  severity: error
  given: $.components.schemas.*.properties.[?(@.type=="array")]
  then:
    field: items
    function: truthy
---