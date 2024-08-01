---
openapi-response-post-201-schema-ref-error:
  description: Warn GET response 201 schema use $ref.
  message: GET Response 201 Schema Ref
  given: $.paths.*.post.responses.201.content.*.schema.*
  severity: error
  then:
    field: $ref
    function: truthy
---