---
openapi-request-body-schema-properties-names-snake-case-error:
  description: Warn schema property names snake case.
  message: Request Body Schema Property Names Snake Case
  severity: warn
  given: $.paths.*.*.requestBody.content.*.schema.properties
  then:
    field: '@key'
    function: casing
    functionOptions:
      type: snake
---