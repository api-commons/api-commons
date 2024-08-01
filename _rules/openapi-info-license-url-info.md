---
openapi-info-license-url-info:
  description: Has info license URL.
  message: Info License URL
  given: $.info.license
  severity: info
  then:
    field: url
    function: falsy
---