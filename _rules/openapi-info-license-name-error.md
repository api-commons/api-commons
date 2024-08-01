---
openapi-info-license-name-error:
  description: Requires info license name.
  message: Info License Name
  given: $.info.license
  severity: error
  then:
    field: name
    function: truthy
---