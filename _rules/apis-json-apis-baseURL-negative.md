---
apis-json-apis-baseURL-negative:
  description: Base URL for APIs
  message: APIs MUST have a base URL.
  given: $.apis.*
  severity: error
  then:
    field: baseURL
    function: truthy
---