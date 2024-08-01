---
openapi-request-body-schema-properties-enum-info:
  description: Has schema property enum.
  message: Request Body Schema Property Enum
  severity: info
  given: $.paths.*.*.requestBody.content.*.schema.properties.*
  then:
    - field: enum
      function: truthy
---