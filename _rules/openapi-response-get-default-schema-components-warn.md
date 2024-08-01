---
openapi-response-get-default-schema-components-warn:
  description: Warn default response default schema should use components.
  message: Default Response Schema Components
  given: $.paths.*.*.responses.default.content.*.schema
  severity: warn
  then:
    field: properties
    function: truthy
---