---
openapi-info-description-info:
  description: Has info description.
  message: Info Description
  severity: info
  given: $.info
  then:
    field: description
    function: falsy
---