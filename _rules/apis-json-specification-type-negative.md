---
apis-json-specification-type-negative:
  description: Specification Type
  message: There MUST be a specification type.
  severity: error
  given: $
  then:
    field: type
    function: truthy
---