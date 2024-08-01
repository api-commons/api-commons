---
openapi-request-body-schema-properties-nullable-error:
  description: Warn request body schema properties format.
  message: Request Body Schema Properties Format
  severity: error
  given: $.paths.*.*.requestBody.content.*.schema.properties.*
  then:
    field: nullable
    function: truthy
---