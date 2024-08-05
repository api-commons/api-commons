---
openapi-response-get-200-media-type-schema-error:
  description: Application JSON Schema for GET
  message: Schema GET
  severity: error
  given: $.paths.*.get.responses.200.content.application/json
  then:
    field: schema
    function: truthy
---