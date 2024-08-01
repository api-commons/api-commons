---
openapi-response-get-200-schema-components-warn:
  description: Warn GET response 200 schema should use components.
  message: GET Response 200 Schema Components
  given: $.paths.*.get.responses.200.content.*.schema
  severity: warn
  then:
    field: properties
    function: truthy
---