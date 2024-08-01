---
apis-json-tags-positive:
  description: Tags for APIs.json
  message: There is a tags object.
  given: $
  severity: info
  then:
    field: tags
    function: falsy
---