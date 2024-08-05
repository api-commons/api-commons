---
openapi-request-body-schema-ref-info:
  description: Has request body schema $ref.
  message: Request Body Schema Ref
  given: $.paths.*.*.requestBody.content.*.schema.$ref
  severity: info
  then:
    function: falsy
---