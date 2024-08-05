---
openapi-components-headers-info:
  description: Require components header.
  message: Components has a headers property.
  severity: info
  given: $.components
  then:
    field: headers
    function: falsy
---