---
apis-json-name-positive:
  description: Name of APIs.json
  message: There is a name.
  severity: info
  given: $
  then:
    field: name
    function: falsy
---