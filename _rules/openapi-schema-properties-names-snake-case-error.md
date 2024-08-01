---
openapi-schema-properties-names-snake-case-error:
  description: Warn schema property names snake case.
  message: Schema Property Names Snake Case
  severity: warn
  given: $.components.schemas.*.properties
  then:
    field: '@key'
    function: casing
    functionOptions:
      type: snake
---