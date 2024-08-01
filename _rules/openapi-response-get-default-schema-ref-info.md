---
openapi-response-get-default-schema-ref-info:
  description: Has default response default schema has $ref.
  message: Default Response Schema Ref
  given: $.paths.*.*.responses.default.content.*.schema
  severity: info
  then:
    field: $ref
    function: falsy
---