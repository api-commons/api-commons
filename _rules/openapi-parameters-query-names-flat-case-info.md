---
openapi-parameters-query-names-flat-case-info:
  description: Warn parameter query name flat case.
  message: Parameter Query Name Flat Case
  severity: info
  given: $.paths.*.*.parameters[?(@.in=='query')].*
  then:
    function: pattern
    functionOptions:
    match: ^[a-z]+$  
---