---
openapi-request-body-schema-properties-descriptions-error:
  description: Require request body schema description.
  message: Schema Description
  severity: error
  given: $.paths.*.*.requestBody.content.*.schema.properties.*
  then:
    field: description
    function: falsy
---