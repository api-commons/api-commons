---
openapi-info-version-error:
  description: Requires info version.
  message: Info Version
  given: $.info
  severity: error
  then:
    field: version
    function: truthy
---