---
openapi-schema-properties-names-camel-case-error:
  description: Warn schema property names camel case.
  message: Schema Property Names Camel Case
  severity: warn
  given: $.components.schemas.*.properties
  then:
    field: '@key'
    function: casing
    functionOptions:
      type: camel
---