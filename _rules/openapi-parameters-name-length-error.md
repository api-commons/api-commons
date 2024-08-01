---
openapi-parameters-name-length-error:
  description: Require parameter name length 25.
  message: Parameter Length
  given: $.paths.*.*.parameters[?(@.in=='path')].name
  then:
    field: summary
    function: length
    functionOptions:
      max: 25
---