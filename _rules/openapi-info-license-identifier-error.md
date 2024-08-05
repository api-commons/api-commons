---
openapi-info-license-identifier-error:
  description: Require info license identifier.
  message: Info License identifier
  given: $.info.license
  severity: error
  then:
    field: identifier
    function: truthy
---