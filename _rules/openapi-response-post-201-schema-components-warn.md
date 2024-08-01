---
openapi-response-post-201-schema-components-warn:
  description: Warn GET response 201 schema should use components.
  message: GET Response 201 Schema Components
  given: $.paths.*.post.responses.201.content.*.schema.*
  severity: warn
  then:
    field: properties
    function: truthy
---