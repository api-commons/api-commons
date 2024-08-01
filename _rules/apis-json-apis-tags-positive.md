---
apis-json-apis-tags-positive:
  description: Tags for API
  message: API has tags object.
  given: $.apis.*
  severity: info
  then:
    field: tags
    function: falsy
---