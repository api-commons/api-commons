---
apis-json-tags-negative:
  description: Tags for APIs.json
  message: There MUST be a tags object..
  given: $
  severity: error
  then:
    field: tags
    function: truthy
---