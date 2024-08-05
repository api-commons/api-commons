---
openapi-info-license-identifier-info:
  description: Has info license identifier.
  message: Info License identifier
  given: $.info.license
  severity: info
  then:
    field: identifier
    function: falsy 
---