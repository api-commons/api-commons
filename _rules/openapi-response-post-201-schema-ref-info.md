---
openapi-response-post-201-schema-ref-info:
  description: Has GET response 201 schema use $ref.
  message: GET Response 201 Schema Ref
  given: $.paths.*.post.responses.201.content.*.schema.*
  severity: warn
  then:
    field: $ref
    function: falsy
---