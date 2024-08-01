---
openapi-request-body-schema-properties-names-camel-case-error:
  description: Warn schema property names camel case.
  message: Request Body Schema Property Names Camel Case
  severity: warn
  given: $.paths.*.*.requestBody.content.*.schema.properties
  then:
    field: '@key'
    function: casing
    functionOptions:
      type: camel
---