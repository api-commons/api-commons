---
apis-json-apis-baseURL-positive:
  description: Base URL for APIs
  message: APIs has a base URL.
  given: $.apis.*
  severity: info
  then:
    field: baseURL
    function: falsy
---