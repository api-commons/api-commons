---
openapi-request-body-have-schema-info:
  description: Has request body schema.
  message: Request Body Schema
  given: $.paths.*.*.requestBody.content.*
  severity: info
  then:
    field: schema
    function: falsy
---