---
openapi-info-title-error:
  description: Require info title.
  message: Info Title
  severity: error
  given: $.info
  then:
    field: title
    function: truthy
---