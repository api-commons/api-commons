---
apis-json-apis-aid-positive:
  description: Unique Identifier of APIs
  message: API has a aid.
  given: $.apis.*
  severity: info
  then:
    field: aid
    function: falsy
---