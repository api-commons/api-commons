---
openapi-response-get-200-schema-ref-info:
  description: Has GET response 200 schema has $ref.
  message: GET Response 200 Schema Ref
  given: $.paths.*.get.responses.200.content.*.schema[?(@.allOf && @.anyOf && @.oneOf)]
  severity: info
  then:
    field: $ref
    function: falsy
---