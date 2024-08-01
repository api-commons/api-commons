---
openapi-parameters-description-error:
  description: Require parameter description.
  message: Parameter Description
  given: $.paths.*.*.parameters.*
  then:
    field: description
    function: truthy
---