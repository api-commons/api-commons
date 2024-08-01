---
apis-json-modified-negative:
  description: Modified for APIs.json
  message: There COULD be a modified date.
  given: $
  severity: warn
  then:
    field: modified
    function: truthy
---