---
openapi-path-description-warn:
  description: Require path description.
  message: Path Description
  given: $.paths.*
  severity: warn
  then:
    field: description
    function: truthy
---