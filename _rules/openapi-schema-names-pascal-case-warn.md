---
openapi-schema-names-pascal-case-warn:
  description: Require schema name pascal case.
  message: Schema Name Pascal Case
  severity: warn
  given: $.components.schemas
  then:
    field: '@key'
    function: casing
    functionOptions:
      type: pascal
---