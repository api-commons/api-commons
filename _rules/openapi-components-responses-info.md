---
openapi-components-responses-info:
  description: Require components responses.
  message: Components has a responses property.
  severity: info
  given: $.components
  then:
    field: responses
    function: falsy
---