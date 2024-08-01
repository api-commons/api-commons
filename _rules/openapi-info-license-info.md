---
openapi-info-license-info:
  description: Has license object.
  message: License Object
  severity: info
  given: $.info
  then:
    field: license
    function: falsy
---