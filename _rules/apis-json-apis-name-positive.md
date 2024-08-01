---
apis-json-apis-name-positive:
  description: Name of APIs
  message: API has a name.
  given: $.apis.*
  severity: info
  then:
    field: name
    function: falsy
---