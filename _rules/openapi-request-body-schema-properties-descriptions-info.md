---
openapi-request-body-schema-properties-descriptions-info:
  description: Require request body schema description.
  message: Schema Description
  severity: info
  given: $.paths.*.*.requestBody.content.*.schema.properties.*
  then:
    field: description
    function: falsy
---