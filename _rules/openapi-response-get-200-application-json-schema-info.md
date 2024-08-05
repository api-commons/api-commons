---
openapi-response-get-200-media-type-schema-info:
  description: Has schema for GET.
  message: Application JSON Schema for GET
  severity: info
  given: $.paths.*.get.responses.200.content.application/json
  then:
    field: schema
    function: falsy
---