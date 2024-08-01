---
openapi-request-body-schema-properties-type-info:
  description: Require request body schema properties type.
  message: Request Body Schema Properties Type
  severity: info
  given: $.paths.*.*.requestBody.content.*.schema.properties.*
  then:
    field: type
    function: falsy
---