---
openapi-info-version-info:
  description: Has info version.
  message: Info Version
  given: $.info
  severity: info
  then:
    field: version
    function: falsy
---