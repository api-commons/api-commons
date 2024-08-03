---
apis-json-common-positive:
  description: Common property for APIs.json
  message: There is an common property.
  given: $
  severity: info
  then:
    field: common
    function: falsy
---