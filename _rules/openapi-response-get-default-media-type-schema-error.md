---
openapi-response-get-default-media-type-schema-error:
  description: Require schema for default.
  message: Schema Default
  severity: error
  given: $.paths.*.*.responses.default.content.application/json
  then:
    field: schema
    function: truthy
---