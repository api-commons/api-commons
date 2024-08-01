---
openapi-schema-names-snake-case-warn:
  description: Require schema name snake case.
  message: Schema Name Snake Case
  severity: warn
  given: $.components.schemas
  then:
    field: '@key'
    function: casing
    functionOptions:
      type: snake
---