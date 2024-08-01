---
openapi-response-get-default-media-type-schema-info:
  description: Has schema for default.
  message: Schema Default
  severity: info
  given: $.paths.*.*.responses.default.content.application/json
  then:
    field: schema
    function: falsy
---