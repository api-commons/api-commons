---
apis-json-specification-version-positive:
  description: Specification Version
  message: There is a specification version.
  severity: info
  given: $
  then:
    field: specificationVersion
    function: falsy
---