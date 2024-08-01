---
openapi-info-license-error:
  description: Requires license object.
  message: License Object
  severity: error
  given: $.info
  then:
    field: license
    function: truthy
---