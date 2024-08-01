---
openapi-schema-properties-names-pascal-case-error:
  description: Warn schema property names pascal case.
  message: Schema Property Names Pascal Case
  severity: warn
  given: $.components.schemas.*.properties
  then:
    field: '@key'
    function: casing
    functionOptions:
      type: pascal
---