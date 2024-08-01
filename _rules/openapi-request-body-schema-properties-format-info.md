---
openapi-request-body-schema-properties-format-info:
  description: Has request body schema properties format.
  message: Request Body Schema Properties Format
  severity: info
  given: $.paths.*.*.requestBody.content.*.schema.properties.*
  then:
    field: format
    function: falsy
---