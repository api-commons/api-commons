---
openapi-request-body-have-schema-error:
  description: Require request body schema.
  message: Request Body Schema
  given: $.paths.*.*.requestBody.content.*
  severity: error
  then:
    field: schema
    function: truthy
---