---
apis-json-created-positive:
  description: Created for APIs.json
  message: There is a created date.
  given: $
  severity: info
  then:
    field: created
    function: falsy
---