---
openapi-request-body-schema-ref-info:
  description: Has request body schema $ref.
  message: Request Body Schema Ref
  given: $.paths.*.*.requestBody.content.*.schema
  severity: info
  then:
    field: $ref
    function: falsy
---