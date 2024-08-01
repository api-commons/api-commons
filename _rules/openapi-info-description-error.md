---
openapi-info-description-error:
  description: Requires info description.
  message: Info Description
  severity: error
  given: $.info
  then:
    field: description
    function: truthy
---