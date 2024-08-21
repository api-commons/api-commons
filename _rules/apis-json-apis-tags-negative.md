---
apis-json-apis-tags-error:
  description: Tags for API
  message: APIs MUST have a tags object.
  given: $.apis.*
  severity: error
  then:
    field: tags
    function: truthy
---