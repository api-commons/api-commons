---
openapi-schema-names-length-error:
  description: Require schema name length 25.
  message: Schema Name Length
  severity: error
  given: $.components.schemas
  then:
    field: '@key'
    function: length
    functionOptions:
      max: 25
---