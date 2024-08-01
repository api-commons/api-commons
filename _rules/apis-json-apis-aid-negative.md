---
apis-json-apis-aid-negative:
  description: Unique Identifier of APIs
  message: APIs MUST have a aid.
  given: $.apis.*
  severity: error
  then:
    field: aid
    function: truthy
---