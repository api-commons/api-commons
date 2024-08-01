---
openapi-request-body-schema-properties-descriptions-length-error:
  description: Require request body schema description length 250.
  message: Schema Description Length
  severity: error
  given: $.paths.*.*.requestBody.content.*.schema.properties.*
  then:
    field: description
    function: length
    functionOptions:
      max: 250
---