---
openapi-request-body-schema-properties-nullable-info:
  description: Has request body schema properties nullable.
  message: Request Body Schema Properties Nullable
  severity: info
  given: $.paths.*.*.requestBody.content.*.schema.properties.*
  then:
    field: nullable
    function: falsy
---