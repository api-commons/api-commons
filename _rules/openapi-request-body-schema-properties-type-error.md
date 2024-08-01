---
openapi-request-body-schema-properties-type-error:
  description: Require request body schema properties type.
  message: Request Body Schema Properties Type
  severity: error
  given: $.paths.*.*.requestBody.content.*.schema.properties.*
  then:
    field: type
    function: truthy
---