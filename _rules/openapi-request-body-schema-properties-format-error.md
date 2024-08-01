---
openapi-request-body-schema-properties-format-error:
  description: Warn request body schema properties format.
  message: Request Body Schema Properties Format
  severity: error
  given: $.paths.*.*.requestBody.content.*.schema.properties.*
  then:
    field: format
    function: truthy
---