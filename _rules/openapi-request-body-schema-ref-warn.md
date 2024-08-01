---
openapi-request-body-schema-ref-warn:
  description: Warn request body schema should have $ref.
  message: Request Body Schema Ref
  given: $.paths.*.*.requestBody.content.*.schema
  severity: warn
  then:
    field: $ref
    function: truthy
---