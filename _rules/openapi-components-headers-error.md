---
openapi-components-headers-error:
  description: Require components header.
  message: Components MUST have a headers property.
  severity: error
  given: $.components
  then:
    field: headers
    function: truthy
---