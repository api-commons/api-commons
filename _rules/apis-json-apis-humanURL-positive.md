---
apis-json-apis-humanURL-positive:
  description: Human URL for APIs
  message: APIs has a human URL.
  given: $.apis.*
  severity: info
  then:
    field: humanURL
    function: falsy
---