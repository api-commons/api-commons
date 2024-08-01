---
openapi-info-license-url-error:
  description: Require info license URL.
  message: Info License URL
  given: $.info.license
  severity: error
  then:
    field: url
    function: truthy
---