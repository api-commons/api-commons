---
openapi-response-get-default-schema-ref-warn:
  description: Warn default response default schema should have $ref.
  message: Default Response Schema Ref
  given: $.paths.*.*.responses.default.content.*.schema
  severity: warn
  then:
    field: $ref
    function: truthy
---