---
openapi-schema-properties-names-length-error:
  description: Requires schema properties names length.
  message: Schema Properties Name Length
  severity: error
  given: $.components.schemas.*.properties
  then:
    field: '@key'
    function: length
    functionOptions:
      max: 25
---