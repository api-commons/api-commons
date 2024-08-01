---
apis-json-apis-name-negative:
  description: Name of APIs
  message: APIs MUST have a name.
  given: $.apis.*
  severity: error
  then:
    field: name
    function: truthy
---