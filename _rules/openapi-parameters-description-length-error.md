---
openapi-parameters-description-length-error:
  description: Require parameter description length 500.
  message: Parameter Description Length
  given: $.paths.*.*.parameters.*
  then:
    field: summary
    function: length
    functionOptions:
      max: 500
---