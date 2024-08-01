---
apis-json-name-negative:
  description: Name of APIs.json
  message: There MUST be a name.
  severity: error
  given: $
  then:
    field: name
    function: truthy
---