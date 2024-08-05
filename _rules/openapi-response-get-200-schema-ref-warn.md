---
openapi-response-get-200-schema-ref-warn:
  description: Warn GET response 200 schema should have $ref.
  message: GET Response 200 Schema Ref
  given: $.paths.*.get.responses.200.content.*.schema[?(@.allOf && @.anyOf && @.oneOf)]
  severity: warn
  then:
    field: $ref
    function: truthy
---