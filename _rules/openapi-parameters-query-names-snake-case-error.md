---
openapi-parameters-query-names-snake-case-error:
  description: Warn parameter query name snake case.
  message: Parameter Query Name Snake Case
  severity: warn
  given: $.paths.*.*.parameters[?(@.in=='query')].*
  then:
    field: name
    function: casing
    functionOptions:
      type: snake
---