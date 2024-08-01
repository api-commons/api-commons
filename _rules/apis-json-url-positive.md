---
apis-json-url-positive:
  description: URL for APIs.json
  message: There is a URL.
  given: $
  severity: info
  then:
    field: url
    function: falsy
---