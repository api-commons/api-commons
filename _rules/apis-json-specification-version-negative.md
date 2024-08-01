---
apis-json-specification-version-negative:
  description: Specification Version
  message: There MUST be a specification version.
  severity: error
  given: $
  then:
    field: specificationVersion
    function: truthy
---