---
openapi-schema-x-expansion-resources-info:
  description: Has schema expansion resources.
  message: Schema X Expansion Resources
  severity: info
  given: $.components.schemas.*
  then:
    field: x-expansionResources
    function: falsy
---