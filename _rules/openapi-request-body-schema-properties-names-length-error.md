---
openapi-request-body-schema-properties-names-length-error:
  description: Requires schema properties names length.
  message: Schema Properties Name Length
  severity: error
  given: $.paths.*.*.requestBody.content.*.schema.properties
  then:
    field: '@key'
    function: length
    functionOptions:
      max: 25
---