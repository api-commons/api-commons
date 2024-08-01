---
apis-json-apis-description-positive:
  description: Description of APIs
  message: API has a description.
  given: $.apis.*
  severity: info
  then:
    field: description
    function: falsy
---