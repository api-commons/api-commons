---
openapi-info-license-name-info:
  description: Has info license name.
  message: Info License Name
  given: $.info.license
  severity: info
  then:
    field: name
    function: falsy
---