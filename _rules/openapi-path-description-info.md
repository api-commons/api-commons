---
openapi-path-description-info:
  description: Has path description.
  message: Path Description
  given: $.paths.*
  severity: info
  then:
    field: description
    function: falsy
---