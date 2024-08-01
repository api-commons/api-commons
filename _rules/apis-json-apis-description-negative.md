---
apis-json-apis-description-negative:
  description: Description of APIs
  message: APIs MUST have a description.
  given: $.apis.*
  severity: error
  then:
    field: description
    function: truthy
---