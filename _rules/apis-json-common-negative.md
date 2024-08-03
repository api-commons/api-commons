---
apis-json-common-negative:
  description: Common property for APIs.json
  message: There MUST be a common property.
  given: $
  severity: error
  then:
    field: common
    function: truthy
---