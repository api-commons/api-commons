---
apis-json-specification-aid-negative:
  description: API Unique Identifier
  message: There MUST be a aid.
  severity: error
  given: $
  then:
    field: aid
    function: truthy
---