---
apis-json-created-negative:
  description: Created for APIs.json
  message: There MUST be a created date.
  given: $
  severity: error
  then:
    field: created
    function: truthy
---