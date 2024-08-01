---
apis-json-description-positive:
  description: Description of APIs.json
  message: There is a description.
  given: $
  severity: info
  then:
    field: description
    function: falsy
---