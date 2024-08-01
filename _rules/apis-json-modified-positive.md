---
apis-json-modified-positive:
  description: Modified for APIs.json
  message: There is a modified date.
  given: $
  severity: info
  then:
    field: modified
    function: falsy
---