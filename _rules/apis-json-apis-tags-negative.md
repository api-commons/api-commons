---
apis-json-apis-tags-negative:
  description: Tags for API
  message: APIs MUST have a tags object.
  given: $.apis.*
  severity: error
  then:
    field: tags
    function: truthy
---