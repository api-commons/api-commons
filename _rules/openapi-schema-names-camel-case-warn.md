---
openapi-schema-names-camel-case-warn:
  description: Require schema name camel case.
  message: Schema Name Camel Case
  severity: warn
  given: $.components.schemas
  then:
    field: '@key'
    function: casing
    functionOptions:
      type: camel
---