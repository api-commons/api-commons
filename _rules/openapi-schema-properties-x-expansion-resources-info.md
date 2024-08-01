---
openapi-schema-properties-x-expansion-resources-info:
  description: Has schema properties expansion resources.
  message: Schema Properties X Expansion Resources
  severity: info
  given: $.components.schemas.*.properties.*
  then:
    field: x-expansionResources
    function: falsy
---