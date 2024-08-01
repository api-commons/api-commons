---
apis-json-apis-humanURL-negative:
  description: Human URL for APIs
  message: APIs MUST have a human URL.
  given: $.apis.*
  severity: error
  then:
    field: humanURL
    function: truthy
---