---
openapi-request-body-have-schema-properties-warn:
  description: Warn component request body schema.
  message: Request Body Schema Components
  given: $.paths.*.*.requestBody.content.*.schema.*
  severity: warn
  then:
    field: properties
    function: truthy
---