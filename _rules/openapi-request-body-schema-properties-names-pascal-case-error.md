---
openapi-request-body-schema-properties-names-pascal-case-error:
  description: Warn schema property names pascal case.
  message: Request Body Schema Property Names Pascal Case
  severity: warn
  given: $.paths.*.*.requestBody.content.*.schema.properties
  then:
    field: '@key'
    function: casing
    functionOptions:
      type: pascal
---