---
openapi-parameters-path-names-snake-case-error:
  description: Warn parameter path name snake case.
  message: Parameter Path Name Snake Case
  severity: warn
  given: $.paths.*.*.parameters[?(@.in=='path')].name
  then:
    field: '@key'
    function: casing
    functionOptions:
      type: snake
---