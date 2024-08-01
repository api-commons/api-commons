---
apis-json-description-negative:
  description: Description of APIs.json
  message: There MUST be a description.
  given: $
  severity: error
  then:
    field: description
    function: truthy
---